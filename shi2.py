import time
import random

# --- Introduction ---

print("\n\nYou awaken in a cold, damp cell.  The air is heavy with the smell of mildew and something... else.")
print("A single flickering torch casts long, dancing shadows on the rough stone walls.")
print("You have no memory of how you got here. Your head throbs. Panic begins to set in.")

inventory = []
has_key = False
torch_lit = True
torch_fuel = 100  # Percentage

# --- Initial Choices ---

print("\nWhat do you do?")
print("1. Examine the cell.")
print("2. Try the cell door.")
print("3. Scream for help.")

choice = input("> ")

if choice == "1":
    print("\nYou search the cell.  The floor is cold and gritty under your bare feet.")
    print("You find a small, rusty KEY under a loose stone, and a rusty NAIL near the door.")
    inventory.append("key")
    inventory.append("nail")
    print("You add the key and nail to your inventory.")
    
    print("\nWhat do you do next?")
    print("1. Try the cell door.")
    print("2. Scream for help.")
    choice = input(">")

    if choice == "1":
      print("\nYou insert the key into the rusty lock. It turns with a loud *CLICK*.")
      has_key = True

    elif choice == "2":
        print("\nYou scream at the top of your lungs.  Your voice echoes down the dark corridors, but there is no response.")
        print("Only the drip, drip, drip of water answers you.  The silence is more terrifying than any sound.")
        print("\nYou feel even more alone than before.")

    else:
      print("Invalid choice. You stand there, frozen in indecision.")

elif choice == "2":
    print("\nYou try the cell door. It's locked, unsurprisingly.  The heavy iron bars feel cold and unyielding.")

    print("\nWhat now?")
    print("1. Examine the cell more closely.")
    print("2. Scream for help.")
    choice = input("> ")

    if choice == "1":
        print("\nYou search the cell.  The floor is cold and gritty under your bare feet.")
        print("You find a small, rusty KEY under a loose stone, and a rusty NAIL near the door.")
        inventory.append("key")
        inventory.append("nail")
        print("You add the key and nail to your inventory.")
        has_key = True # They found the key, so they have it.

    elif choice == "2":
      print("\nYou scream at the top of your lungs. Your voice echoes... but only silence answers.")
      print("The dripping water seems to mock your desperation.")

    else:
      print("Invalid choice. You stand there, paralyzed by fear.")


elif choice == "3":
    print("\nYou scream for help.  Your voice echoes down the dark corridors, but there is no response.")
    print("Only the drip, drip, drip of water answers you. The silence is more terrifying than any sound.")

    print("\nWhat next?")
    print("1. Examine the cell.")
    print("2. Try the cell door.")
    choice = input("> ")

    if choice == "1":
        print("\nYou search the cell.  The floor is cold and gritty under your bare feet.")
        print("You find a small, rusty KEY under a loose stone, and a rusty NAIL near the door.")
        inventory.append("key")
        inventory.append("nail")
        print("You add the key and the nail to your inventory.")
        has_key = True

    elif choice == "2":
      print("\nYou try the cell door.  It's locked, as expected.")

    else:
      print("Invalid choice. You waste precious moments.")

else:
    print("\nInvalid choice. You stumble around in the darkness, disoriented.")


# --- Out of the Cell ---
if has_key:
    print("\nYou unlock the door and step out into a dark corridor.")
    print("The torch in your cell is your only source of light.")

    print("\nWhich way do you go?")
    print("1. Left")
    print("2. Right")

    choice = input("> ")

    if choice == "1":
        print("\nYou walk down the corridor to the left.  The air grows colder.")
        torch_fuel -= 10
        print(f"Your torch flickers.  Fuel: {torch_fuel}%")
        print("You hear a faint SCRATCHING sound ahead.")

        print("\nWhat do you do?")
        print("1. Continue forward.")
        print("2. Go back.")
        choice = input(">")

        if choice == "1":
            print("\nYou creep closer to the sound.  The scratching gets louder.")
            print("Suddenly, a large, grotesque RAT jumps out of the shadows!")
            if "nail" in inventory:
              print("You quickly grab the NAIL and impale the rat, killing it. You are safe, for now...")
              inventory.remove("nail")
            else:
              print("You have nothing to defend yourself with! The rat bites you repeatedly.")
              print("You feel a searing pain as the rat's teeth sink into your flesh. You fall to the floor.")
              print("You have died.")
              exit()

            print("\nShaken, but alive, you continue down the corridor.")
            torch_fuel -= 15
            print(f"Your torch flickers. Fuel: {torch_fuel}%")
            print("You reach a dead end.  There's a small, wooden CHEST on the floor.")

            print("\nWhat do you do?")
            print("1. Open the chest.")
            print("2. Go back.")
            choice = input("> ")

            if choice == "1":
              print("\nYou open the chest. Inside, you find a small vial of OIL.")
              print("You pour the oil on your torch, replenishing its fuel.")
              torch_fuel = 100
              print(f"Your torch burns brightly. Fuel: {torch_fuel}%")

              print("You return to the main corridor.")


            elif choice == "2":
              print("\nYou decide to go back, retracing your steps to the main corridor.")
            else:
              print("Invalid choice. You waste time.")

        elif choice == "2":
          print("You turn back and walk quickly away from the sound.")

        else:
            print("\nInvalid choice.  You hesitate, and the scratching sound grows louder.")

    elif choice == "2":
        print("\nYou walk down the corridor to the right.")
        torch_fuel -= 10
        print(f"Your torch flickers.  Fuel: {torch_fuel}%")
        print("The corridor twists and turns. You feel like you're going in circles.")
        print("You hear a low GROWL behind you.")

        print("\nWhat do you do?")
        print("1. Turn around.")
        print("2. Run!")
        choice = input("> ")

        if choice == "1":
          print("\nYou turn around slowly. A pair of glowing red eyes appear in the darkness.")
          print("A monstrous creature lunges at you!.")

          if "nail" in inventory:
            print("\nYou have a rusty nail... it's not much, but it's something.")
            print("You stab at the creature with the nail.  It howls in pain, but...")
            if random.randint(1, 2) == 1: #50% chance.
              print("...the nail breaks!  The creature overwhelms you.")
              print("You have died.")
              exit()

            else:
              print("... you manage to drive the creature back! It retreats into the shadows.")
              inventory.remove("nail")

          else:
            print("\nYou are unarmed! The creature tears you apart.")
            print("You have died.")
            exit()


        elif choice == "2":
            print("\nYou run as fast as you can, the growls echoing behind you.")
            torch_fuel -= 20  # Running uses more fuel.
            print(f"Your torch flickers wildly. Fuel: {torch_fuel}%")
            print("You stumble and nearly fall, but manage to keep running.")
            print("You finally reach a large, open chamber.")

        else:
          print("Invalid choice. The creature attacks while you hesitate.")
          print("You have died.")
          exit()

    else:
        print("\nInvalid choice. You stumble in the darkness, wasting precious torch fuel.")
        torch_fuel -= 5
        print(f"Your torch flickers.  Fuel: {torch_fuel}%")

else:
    print("\nThe cell door remains locked. You are trapped.")
    print("Despair washes over you. You sink to the floor, defeated.")
    print("You have died... of despair.")
    exit()

# --- The Chamber ---

print("\nThe chamber is vast and echoing. Several passages lead off in different directions.")
print("In the center of the chamber, you see a flickering PEDESTAL.")
print("Your torchlight barely penetrates the gloom.")

print("\nWhat do you do?")
print("1. Approach the pedestal.")
print("2. Explore the passages.")
choice = input("> ")

if choice == "1":
  print("\nYou approach the pedestal cautiously.  As you get closer, you see that there is a BOOK on it.")
  print("The book is ancient and bound in leather. Strange symbols are etched on the cover.")

  print("\nWhat do you do?")
  print("1. Open the book.")
  print("2. Leave the book alone.")

  choice = input ("> ")
  if choice == "1":
    print("As soon as you open it, the book starts speaking, and you hear: \"You have gone so far, and the last step will be a test\".")
    print("The pedestal starts spinning, opening a secret passage to the final room, there you see a sword on the ground.")
    print("You take it, and suddenly a giant shadow comes out of the darkness.")

    print("\nWhat do you do?")
    print("1. Attack the shadow.")
    print("2. Run for your life.")
    choice = input ("> ")

    if choice == "1":
        print("You jump towards the shadow, with your sword pointing at it. You go through the shadow, as if it was smoke.")
        print("The shadow desappears. You find yourself, back at your home, as if all of this was just a dream")
        print("THE END.")
    elif choice == "2":
          print("You try to run, but it is no use. The shadow catches you, and you feel as if your soul is being torn apart.")
          print("You have died.")
          exit()
    else:
        print("Invalid Choice")
        exit()

  elif choice == "2":
        print("You leave the book alone.")
        exit()
  else:
        print("Invalid Choice")
        exit()

elif choice == "2":
    print("The passages are to dark to explore.")
    exit()
else:
  print("Invalid Choice.")
  exit()