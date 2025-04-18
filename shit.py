import base64

# Base64 encoded game data (replace with your actual game content)
game_data_encoded = """
  SGVsbG8gVGltZSB0cmF2ZWxlci4gWW91IGZpbmQgeW91cnNlbGYgbmV4dCB0byBhIHRpbWUgbWFjaGluZSAuLi4gWW91IGNhbiBkbwoKICAxLiBJbnZlc3RpZ2F0ZSB0aGUgbWFjaGluZQogIDIzLiBEb24ndCBpbnZlc3RpZ2F0ZSAgdGhlIG1hY2hpbmUKCk4gQWx3YXlzIGJldCB3aXRoIG9uZS4K
  """

try:
    game_data = base64.b64decode(game_data_encoded).decode("utf-8")
except Exception as e:
    print(f"Error decoding game data: {e}")
    exit()
print(game_data)

choice = input("Enter choice: ")

if choice == "1":
    print("You examine the machine. It has a complex control panel.")
    print("You see options for destination year and a 'GO' button.")
    print("Do you:\n1. Enter a year and go.\n2. Try to understand the machine first.\n3. Leave the machine alone")
    choice2 = input("Enter choice: ")
    if choice2 == "1":
        print("You enter the year 2077 and press GO.")
        print("You are hurtled through time and land in a futuristic city.")
        print("You see flying cars and neon lights.")
        print("Do you:\n1. Explore the city.\n2. Try to find a way back.\n3. Try to understand the machine first.")
        choice3 = input("Enter choice: ")
        if choice3 == "1":
            print("You explore the city. You are amazed and overwhelmed.")
            print("You encounter a group of rebels fighting against a corporation.")
            print("Do you:\n1. Join the rebels.\n2. Try to stay neutral.\n3. Find a way back to your time.")
            choice4 = input("Enter choice: ")
            if choice4 == "1":
                print("You join the rebels and fight for their cause. You become a hero!")
                print("Ending 1: The Hero of 2077")
            elif choice4 == "2":
                print("You observe the conflict, attempting to not to make enemies.")
                print("You find your time machine and return to your time.")
                print("Ending 2: The Observer")
            elif choice4 == "3":
                print("You look for a way to get back home and succeed!")
                print("Ending 3: Back Home")
            else:
                print("Invalid choice. Ending 4: Failure")
        elif choice3 == "2":
            print("You try to understand the machine. You find the control panel complex")
            print("You are starting to lose hope.")
            print("Do you:\n1. Find a way back to your time.\n2. Try to understand the machine first.\n3. Explore the city.")
            choice4 = input("Enter choice: ")
            if choice4 == "1":
                print("You look for a way to get back home and succeed!")
                print("Ending 5: Back Home")
            elif choice4 == "2":
                print("The machine is too complex. You are losing time and mind!")
                print("Ending 6: Madness in 2077")
            elif choice4 == "3":
                print("You go to explore the city. You are amazed and overwhelmed.")
                print("You encounter a group of rebels fighting against a corporation.")
                print("Do you:\n1. Join the rebels.\n2. Try to stay neutral.\n3. Find a way back to your time.")
                choice5 = input("Enter choice: ")
                if choice5 == "1":
                    print("You join the rebels and fight for their cause. You become a hero!")
                    print("Ending 7: The Hero of 2077")
                elif choice5 == "2":
                    print("You observe the conflict, attempting to not to make enemies.")
                    print("You find your time machine and return to your time.")
                    print("Ending 8: The Observer")
                elif choice5 == "3":
                    print("You look for a way to get back home and succeed!")
                    print("Ending 9: Back Home")
                else:
                    print("Invalid choice. Ending 10: Failure")
            else:
                print("Invalid choice. Ending 11: Failure")
        elif choice3 == "3":
            print("You give up the machine and explore the city.")
            print("You are amazed and overwhelmed.")
            print("You encounter a group of rebels fighting against a corporation.")
            print("Do you:\n1. Join the rebels.\n2. Try to stay neutral.\n3. Find a way back to your time.")
            choice4 = input("Enter choice: ")
            if choice4 == "1":
                print("You join the rebels and fight for their cause. You become a hero!")
                print("Ending 12: The Hero of 2077")
            elif choice4 == "2":
                print("You observe the conflict, attempting to not to make enemies.")
                print("You find your time machine and return to your time.")
                print("Ending 13: The Observer")
            elif choice4 == "3":
                print("You look for a way to get back home and succeed!")
                print("Ending 14: Back Home")
            else:
                print("Invalid choice. Ending 15: Failure")
        else:
            print("Invalid choice. Ending 16: Failure")
    elif choice2 == "2":
        print("You spend hours studying the machine. You learn some basic functions.")
        print("Do you:\n1. Enter a year and go.\n2. Decide the machine is too dangerous. \n3. Explore your surroundings.")
        choice3 = input("Enter choice: ")
        if choice3 == "1":
            print("You set the year to 1945 and hit GO!")
            print("You arrive in a war-torn city, the aftermath of a bombing.")
            print("Do you:\n1. Help the wounded.\n2. Try to return to your time.")
            choice4 = input("Enter choice: ")
            if choice4 == "1":
                print("You help the wounded, but get caught in a crossfire and...")
                print("Ending 17: The Hero")
            elif choice4 == "2":
                print("You try to return to your time and fail!")
                print("Ending 18: Stranded in 1945")
            else:
                print("Invalid choice. Ending 19: Failure")
        elif choice3 == "2":
            print("You decide the machine is too dangerous, and you leave it. You never travel back to your time, but neither do you die.")
            print("Ending 20: The Cautious")
        elif choice3 == "3":
            print("You explore your surroundings. You see a friendly dog.")
            print("Do you:\n1. Pet the dog.\n2. Get back to the machine")
            choice4 = input("Enter choice: ")
            if choice4 == "1":
                print("The dog is happy and follows you around.")
                print("You suddenly wake up with a shock!")
                print("You return to your time.")
                print("Ending 21: Dog is the Best Companion.")
            elif choice4 == "2":
                print("You get back to the machine and hit GO!")
                print("You set the year to 1945 and hit GO!")
                print("You arrive in a war-torn city, the aftermath of a bombing.")
                print("Do you:\n1. Help the wounded.\n2. Try to return to your time.")
                choice5 = input("Enter choice: ")
                if choice5 == "1":
                    print("You help the wounded, but get caught in a crossfire and...")
                    print("Ending 22: The Hero")
                elif choice5 == "2":
                    print("You try to return to your time and fail!")
                    print("Ending 23: Stranded in 1945")
                else:
                    print("Invalid choice. Ending 24: Failure")
            else:
                print("Invalid choice. Ending 25: Failure")
        else:
            print("Invalid choice. Ending 26: Failure")
    elif choice2 == "3":
        print("You decide the machine is too dangerous, and you leave it. You never travel back to your time, but neither do you die.")
        print("Ending 27: The Cautious")
    else:
        print("Invalid choice. Ending 28: Failure")
elif choice == "23":
  print("You decide not to interact with the time machine and leave.")
  print("You are never able to return to your own time.")
  print("Ending 28: The Coward")
else:
    print("Invalid choice. Ending 29: Failure")