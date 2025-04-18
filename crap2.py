import threading
import time
import requests
import json
import logging
import tkinter as tk
from functools import lru_cache

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

API_URL = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
CACHE_TTL = 60  # Cache time-to-live in seconds

class BitcoinPriceFetcher:
    def __init__(self):
        self.price = None
        self.lock = threading.Lock()
        self.last_updated = 0
    
    @lru_cache(maxsize=1)
    def fetch_price(self):
        with self.lock:
            if time.time() - self.last_updated < CACHE_TTL:
                logging.info("Using cached price.")
                return self.price
            try:
                response = requests.get(API_URL)
                data = response.json()
                self.price = data['bpi']['USD']['rate']
                self.last_updated = time.time()
                logging.info(f"Fetched Bitcoin price: ${self.price}")
            except Exception as e:
                logging.error(f"Failed to fetch Bitcoin price: {e}")
            return self.price

class BitcoinPriceGUI:
    def __init__(self, root, fetcher):
        self.root = root
        self.fetcher = fetcher
        self.root.title("Bitcoin Price Checker")
        self.label = tk.Label(root, text="Fetching...", font=("Arial", 20))
        self.label.pack(pady=20)
        self.update_price()
    
    def update_price(self):
        def fetch_and_update():
            price = self.fetcher.fetch_price()
            self.label.config(text=f"Bitcoin Price: ${price}")
            self.root.after(5000, self.update_price)  # Refresh every 5 seconds
        threading.Thread(target=fetch_and_update, daemon=True).start()

if __name__ == "__main__":
    fetcher = BitcoinPriceFetcher()
    root = tk.Tk()
    app = BitcoinPriceGUI(root, fetcher)
    root.mainloop()
