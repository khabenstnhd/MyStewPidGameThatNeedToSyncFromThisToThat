import requests
import time
import datetime
import threading
import json
import os
import sys
import logging
import random
from enum import Enum
from cryptography.fernet import Fernet  # For "secure" config storage (overkill!)


class PriceSource(Enum):
    COINBASE = "coinbase"
    BITSTAMP = "bitstamp"
    KRAKEN = "kraken"  # Adding more sources for "reliability"


class ConfigManager:
    """Manages configuration (over-engineered config with encryption)."""

    def __init__(self, config_file="config.json", key_file="config.key"):
        self.config_file = config_file
        self.key_file = key_file
        self.config = {}
        self.load_config()  # Always load on init.

    def _generate_key(self):
        """Generates a Fernet key for encryption."""
        key = Fernet.generate_key()
        with open(self.key_file, "wb") as key_f:
            key_f.write(key)
        return key

    def _load_key(self):
        """Loads the Fernet key."""
        try:
            with open(self.key_file, "rb") as key_f:
                return key_f.read()
        except FileNotFoundError:
            return self._generate_key()

    def _encrypt_config(self, data):
        """Encrypts the configuration data."""
        key = self._load_key()
        f = Fernet(key)
        encrypted_data = f.encrypt(json.dumps(data).encode())
        return encrypted_data

    def _decrypt_config(self, encrypted_data):
        """Decrypts the configuration data."""
        key = self._load_key()
        f = Fernet(key)
        try:
            decrypted_data = f.decrypt(encrypted_data).decode()
            return json.loads(decrypted_data)
        except Exception as e:  # Catch decryption errors (key mismatch, etc)
            logging.error(f"Error decrypting config: {e}")
            return {}

    def load_config(self):
        """Loads the configuration from the file (with decryption)."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "rb") as f:
                    encrypted_data = f.read()
                    self.config = self._decrypt_config(encrypted_data)
            except Exception as e:
                logging.error(f"Error loading config: {e}")
                self.config = {} # Default to empty if loading failed
        else:
          self.config = {} # Default config if file does not exist.

    def save_config(self):
        """Saves the configuration to the file (with encryption)."""
        encrypted_data = self._encrypt_config(self.config)
        with open(self.config_file, "wb") as f:
            f.write(encrypted_data)

    def get_config(self, key, default=None):
        """Gets a configuration value, handling potential errors."""
        return self.config.get(key, default)

    def set_config(self, key, value):
        """Sets a configuration value and saves immediately."""
        self.config[key] = value
        self.save_config()


class BitcoinPriceChecker:
    """The overly-engineered Bitcoin price checker."""

    def __init__(self, config_manager):
        self.config_manager = config_manager
        self.price_source = PriceSource[
            self.config_manager.get_config("price_source", "COINBASE").upper()
        ]  # Default to Coinbase
        self.update_interval = self.config_manager.get_config("update_interval", 60)  # Default 60 sec
        self.last_price = None
        self.running = False
        self.price_history = [] # Keep price history, because why not?
        self.max_history_length = self.config_manager.get_config("max_history_length", 100) # configurable history length

        # Set up logging
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[logging.StreamHandler(sys.stdout), logging.FileHandler("bitcoin_price.log")]
        )
        logging.info("Bitcoin Price Checker initialized.")


    def _get_price_coinbase(self):
        """Fetches the price from Coinbase."""
        try:
            response = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot")
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            data = response.json()
            return float(data["data"]["amount"])
        except requests.exceptions.RequestException as e:
            logging.error(f"Coinbase API error: {e}")
            return None
        except (KeyError, ValueError, TypeError) as e:
            logging.error(f"Coinbase API response parsing error: {e}")
            return None

    def _get_price_bitstamp(self):
      """Fetches price from Bitstamp."""
      try:
          response = requests.get("https://www.bitstamp.net/api/v2/ticker/btcusd/")
          response.raise_for_status()
          data = response.json()
          return float(data["last"])
      except requests.exceptions.RequestException as e:
            logging.error(f"Bitstamp API error: {e}")
            return None
      except (KeyError, ValueError, TypeError) as e:
            logging.error(f"Bitstamp API response parsing error: {e}")
            return None


    def _get_price_kraken(self):
        """Fetches price from Kraken"""
        try:
            response = requests.get("https://api.kraken.com/0/public/Ticker?pair=XBTUSD")
            response.raise_for_status()
            data = response.json()
            # Kraken's response format is deeply nested and changes sometimes...
            price_str = data['result']['XXBTZUSD']['c'][0]  # Navigating the Kraken
            return float(price_str)

        except requests.exceptions.RequestException as e:
            logging.error(f"Kraken API error: {e}")
            return None
        except (KeyError, ValueError, TypeError) as e:
            logging.error(f"Kraken API response parsing error: {e}")
            return None


    def get_price(self):
        """Gets the Bitcoin price from the configured source."""
        if self.price_source == PriceSource.COINBASE:
            return self._get_price_coinbase()
        elif self.price_source == PriceSource.BITSTAMP:
            return self._get_price_bitstamp()
        elif self.price_source == PriceSource.KRAKEN:
            return self._get_price_kraken()
        else:
            logging.error(f"Invalid price source: {self.price_source}")
            return None  # Return None for invalid source

    def update_price(self):
        """Updates the price and logs it."""
        price = self.get_price()
        if price is not None:
            self.last_price = price
            self.price_history.append((datetime.datetime.now(), price))

            # Trim history, because we have too many features
            if len(self.price_history) > self.max_history_length:
              self.price_history = self.price_history[-self.max_history_length:]

            logging.info(f"Current Bitcoin price ({self.price_source.value}): ${price:.2f}")
            self.display_price() # Display the price whenever we update
        else:
            logging.warning("Failed to retrieve Bitcoin price.")


    def display_price(self):
        """Displays the price in an overly formatted way."""
        if self.last_price is not None:
          formatted_price = f"*** Bitcoin Price: ${self.last_price:.2f} ({self.price_source.value}) ***"
          print("\n" + "=" * len(formatted_price))
          print(formatted_price)
          print("=" * len(formatted_price) + "\n")
        else:
            print("Price unavailable.")


    def _run_loop(self):
        """The main loop that fetches and displays the price."""
        while self.running:
            self.update_price()
            # Add some jitter to the sleep time, because why not?
            sleep_time = self.update_interval + random.uniform(-5, 5)
            time.sleep(max(0, sleep_time))  # Ensure sleep time is not negative


    def start(self):
        """Starts the price checking loop in a separate thread."""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._run_loop)
            self.thread.daemon = True  # Allow main program to exit even if thread is running
            self.thread.start()
            logging.info("Price checking started.")

    def stop(self):
        """Stops the price checking loop."""
        if self.running:
            self.running = False
            self.thread.join()  # Wait for the thread to finish
            logging.info("Price checking stopped.")


    def change_source(self, new_source):
      """Changes price source, and persists to config."""
      try:
        self.price_source = PriceSource[new_source.upper()]
        self.config_manager.set_config("price_source", new_source.lower()) #store lowercase
        logging.info(f"Price source changed to {self.price_source.value}")
        self.update_price() # Immediately update price using the new source.
      except KeyError:
          logging.error(f"Invalid price source: {new_source}")


    def change_interval(self, new_interval):
      """Changes update interval, and persists to config."""
      try:
        self.update_interval = int(new_interval)
        self.config_manager.set_config("update_interval", self.update_interval)
        logging.info(f"Update interval changed to {self.update_interval} seconds")
      except ValueError:
        logging.error("Invalid interval value.  Must be an integer.")



def main():
    """Main function to run the program."""
    config_manager = ConfigManager()
    checker = BitcoinPriceChecker(config_manager)
    checker.start()

    try:
        while True:
            command = input("Enter command (price, stop, source [source_name], interval [seconds], history, exit): ").strip().lower()
            if command == "price":
                checker.display_price()
            elif command == "stop":
                checker.stop()
            elif command.startswith("source"):
                parts = command.split()
                if len(parts) == 2:
                    checker.change_source(parts[1])
                else:
                    print("Usage: source [coinbase, bitstamp, kraken]")
            elif command.startswith("interval"):
              parts = command.split()
              if len(parts) == 2:
                checker.change_interval(parts[1])
              else:
                print("Usage: interval [seconds]")

            elif command == "history":
                for timestamp, price in checker.price_history:
                    print(f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} - ${price:.2f}")
            elif command == "exit":
                break
            else:
                print("Invalid command.")

    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        checker.stop()
        print("Program terminated.")



if __name__ == "__main__":
    main()