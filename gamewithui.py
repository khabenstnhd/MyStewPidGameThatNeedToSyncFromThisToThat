import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk  # Import ttk for themed widgets (looks better)
#YEAH, ITS EASY TO PORT THE GAME.
# --- Game Data (from original code) ---
# (All your text1, startpoint, path1, path2, ..., endings dictionaries go here)
text1 = "You stand at the edge of the scorching Sahara Desert. The wind whips sand around you, stinging your eyes. Legend speaks of the Lost Amulet of Zerzura, a powerful artifact hidden within a forgotten oasis. You, a seasoned explorer, are determined to find it. Before you lie three paths, shrouded in the swirling sands:"
startpoint = """
You stand at the edge of the scorching Sahara Desert. The wind whips sand around you, stinging your eyes. Legend speaks of the Lost Amulet of Zerzura, a powerful artifact hidden within a forgotten oasis. You, a seasoned explorer, are determined to find it. Before you lie three paths, shrouded in the swirling sands:
1. Head straight into the dunes, following the faint tracks of a long-dead caravan.
2. Search for a nearby Bedouin encampment, hoping to gain information from the locals.
3. Climb the towering rock formation to your left, seeking a vantage point to survey the landscape.
"""

# Round 1 Paths
path1 = """
You trudge through the sand, the sun beating down mercilessly. The caravan tracks are fading, but you press on. You find the remnants of a shattered wagon.
1. Check inside the ruined caravan.
2. Continue on the same path as the caravan, despite the destruction.
3. Change course and try a new path through the dunes.
"""

path2 = """
You spot smoke in the distance and eventually reach a small Bedouin camp. The people are wary but offer you water and shade.
1. Politely inquire about the Amulet of Zerzura.
2. Offer them a valuable item from your pack in exchange for information.
3. Rest for a while and leave quietly in the night, figuring they know nothing.
"""

path3 = """
The climb is arduous, but you reach the top, breathless. The desert stretches before you, a vast ocean of sand. You notice a peculiar glint in the distance.
1. Carefully descend and head towards the glint.
2. Use your binoculars to get a closer look at the glint.
3. The height makes you dizzy. Descend and choose a different path at the base of the rocks.
"""

# Round 2 Paths
path11 = """
You rummage through the wreckage and find a tattered journal.
1. Read the journal, looking for clues.
2. Ignore the journal, searching for supplies instead.
3. The sight of the destroyed caravan unnerves you. Abandon the search and head back.
"""

path12 = """
You walk for hours, following the faint tracks. The sun is relentless, and your water is running low. You spot an oasis shimmer on air!
1. Approach the center, where a great ancient temple can be see.
2. Look on other thing the oasis has, like tree or the lake.
3. It can be a trap! retreat and leave is the better idea!
"""

path13 = """
You veer off the caravan path, striking out in a new direction. You stumble upon a partially buried stone marker.
1. Dig around the marker, hoping to find something.
2. Use the marker as a guide, heading in the direction it seems to point.
3. Ignore the marker; it's probably just a rock.
"""

path21 = """
The Bedouins listen to your story, their faces grave. An elder speaks.
1. Listen intently to the elder's warning about the dangers.
2. Dismiss the warning as superstition and press for details.
3. Thank the elder for their time and offer a small gift.
"""

path22 = """
You offer a silver compass. A young Bedouin's eyes light up, and he whispers to you.
1. Follow the young Bedouin as he leads you away from the camp.
2. Ask the young Bedouin to explain his knowledge in front of the others.
3. Decide the compass was too valuable and try to take it back.
"""

path23 = """
You slip away under the cover of darkness, feeling a bit guilty but determined.
1. Head east, believing the oasis lies in that direction.
2. Head west, thinking the Bedouins were trying to mislead you.
3. Circle back to the rock formation you saw earlier, rethinking your strategy.
"""

path31 = """
You scramble down the rocks and head towards the glint. It's a small, metal box reflecting the sunlight.
1. Carefully open the metal box.
2. Bury the box, thinking it might be a trap.
3. Take the box with you but don't open it yet.
"""

path32 = """
You focus your binoculars. You see what appears to be a ruined temple, half-buried in the sand.
1. Make your way towards the ruined temple, using the binoculars as a guide.
2. Decide the temple is too far and look for a closer landmark.
3. You spot a sandstorm brewing. Seek shelter immediately.
"""

path33 = """
You climb down and choose a path leading away from the rock formation, towards a cluster of date palms in the distance.
1. Head directly towards the date palms, hoping for water and shade.
2. Approach the date palms cautiously, wary of potential dangers.
3. Decide the palms are a mirage and head in a different direction.
"""
# Round 3 Endings (as a dictionary for easy access) and for who ever read this code,
#i don't want to type out "path113 = "Blah Blah Blah" 27 time
# Equation: Scene^Option = Ending
# Very gud equation. 
endings = {
    "1-1-1": "The journal reveals a secret passage! You find the Amulet, but a sandstorm traps you. You use the Amulet's power to survive, becoming a legend. (Ending 1: Legend)",
    "1-1-2": "You find some dried meat and water, but no Amulet. You survive, but your quest fails. (Ending 2: Survival)",
    "1-1-3": "You give up and return home, forever haunted by what might have been. (Ending 3: Regret)",
    "1-2-1": "You reach at the main chamber. Where the amulet is rest. (Ending 4: Victory)",
    "1-2-2": "While check tree and lake. You didn't notice snake, that posionus. (Ending 5: Game Over)",
    "1-2-3": "While retreat a sand storm blow away, the path is gone now (Ending 6: Lost)",
    "1-3-1": "You unearth a small, stone tablet with ancient carvings. It's a map to a hidden spring, not the Amulet. (Ending 7: Oasis Found)",
    "1-3-2": "The marker leads you on a long, circular trek. You end up back where you started, exhausted and disillusioned. (Ending 8: Circle of Despair)",
    "1-3-3": "You wander aimlessly, eventually succumbing to the desert's harsh conditions. (Ending 9: Desert's Embrace)",
    "2-1-1": "You heed the warning and learn valuable desert survival skills, but never find the Amulet. You become a respected desert guide. (Ending 10: The Guide)",
    "2-1-2": "The elder reluctantly reveals a cryptic riddle about the Amulet's location, but it's too confusing. You fail. (Ending 11: Riddle of Failure)",
    "2-1-3": "The elder smiles and offers you a pouch of special herbs that protect you from the desert's harshness. You find water, but no Amulet. (Ending 12: Desert Survivor)",
    "2-2-1": "The youth leads you to a hidden cave where a band of thieves is hiding. They capture you. (Ending 13: Captured)",
    "2-2-2": "The youth is forced to confess. He reveals a false location for the Amulet, leading you on a wild goose chase. (Ending 14: Deception)",
    "2-2-3": "The Bedouins are angered by your distrust. They banish you from their camp. (Ending 15: Banishment)",
    "2-3-1": "You wander east for days, eventually collapsing from dehydration. (Ending 16: Thirst's End)",
    "2-3-2": "You stumble upon a small, abandoned well. You find water, but no sign of the Amulet. (Ending 17: Well of Hope)",
    "2-3-3": "You reach the rock formation again, but with renewed knowledge. You spot a different clue you missed before, leading you to a secret canyon...and the Amulet! But you are weak. (Ending 18: Almost There!)",
    "3-1-1": "The box contains a key and a small map. It leads to a hidden chamber in the ruined temple you saw from above! You almost there.(Ending 19: The Key)",
    "3-1-2": "You bury the box, feeling uneasy. Later, you regret your decision and can never find it again. (Ending 20: Lost Chance)",
    "3-1-3": "You carry the box, unsure of its contents. You later encounter a sandstorm, are the box are gone. (Ending 21: Burdened)",
    "3-2-1": "You reach the temple and find it guarded by a magical sand creature! You fight, but are defeated. (Ending 22: Sand Guardian)",
    "3-2-2": "You find a small oasis with a single, ancient tree. Beneath it, you discover a scroll hinting at a test of worthiness, but not the Amulet itself. (Ending 23: The Test)",
    "3-2-3": "You take shelter in a small cave. When the storm passes, you find ancient carvings on the cave walls, revealing the true history of Zerzura, but no Amulet. (Ending 24: Historian)",
    "3-3-1": "You reach the palms and find water, but also a group of hostile nomads who take you prisoner. (Ending 25: Nomad Captives)",
    "3-3-2": "You carefully scout the area and find tracks leading away from the palms, towards a hidden crevice in the rocks. You found where the location is.(Ending 26: Cautious Success)",
    "3-3-3": "You realize the palms were a mirage and wander in the wrong direction, losing your way completely. (Ending 27: Mirage's Betrayal)",
}

# --- GUI and Game Logic --- 75% stackoverflow.
# https://docs.python.org/3/library/tk.html
# fuck Goblin Tinkerer for turn my Zenith into a Broken Zenith
# credit to https://www.youtube.com/watch?v=F-QjKc4aEIw this video for help me firgure out what the actual fuk im doing
# the 3d model in the video up there kinda horror =))
import colorsys #RGB BOIIII , i still don't know why i import it

class SaharaGame:
    def __init__(self, master):
        self.master = master
        master.title("Ben_AdventureGame.py")
        master.geometry("800x600")  # Set a reasonable window size, good luck play on 4k
        master.configure(bg="#F0E68C")  # Desert-like background color also look like a old crap program from the past

        # Use a better font
        self.custom_font = tkFont.Font(family="Arial", size=12) # meh, pull a request and tell me should i use arial or switch to time new roman

        # --- Main Text Area ---
        self.text_area = tk.Text(master, wrap=tk.WORD, width=70, height=15, font=self.custom_font, bg="#F5F5DC", bd=5, relief=tk.GROOVE)  # Added border/relief
        self.text_area.pack(pady=20, padx=20, fill=tk.BOTH, expand=True) # Fill and expand
        self.text_area.insert(tk.END, text1)
        self.text_area.config(state=tk.DISABLED)  # Make it read-only. 


        # --- Button Frame (for better layout) ---
        self.button_frame = tk.Frame(master, bg="#F0E68C")
        self.button_frame.pack(pady=10)

        # --- Buttons (use grid for placement within the frame)---
        self.buttons = []  # Store button references
        self.create_buttons(startpoint)


        # --- Status/Message Label (NEW) ---
        self.status_label = tk.Label(master, text="", font=("Arial", 10, "italic"), bg="#F0E68C", fg="darkred") #Added color
        self.status_label.pack(pady=5)

    def create_buttons(self, prompt):
        # Clear previous buttons
        for button in self.buttons:
            button.destroy()
        self.buttons = []

        # Update text area
        self.update_text(prompt)

        # Extract choices from the prompt
        choices = [line.strip() for line in prompt.split("\n") if line.strip().startswith(tuple(str(i) + "." for i in range(10)))]


        for i, choice_text in enumerate(choices):
           #Correctly remove number prefix
            button_text = choice_text[2:].strip()
            button = ttk.Button(self.button_frame, text=button_text, command=lambda idx=i+1: self.make_choice(str(idx))) # Use ttk for styling
            button.grid(row=i // 2, column=i % 2, padx=5, pady=5) # 2 buttons per row, adjust as needed.
            self.buttons.append(button)

    def update_text(self, new_text):
        self.text_area.config(state=tk.NORMAL)  # Temporarily enable
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, new_text)
        self.text_area.config(state=tk.DISABLED)  # Disable again
        self.text_area.see(tk.END)  # Scroll to the end

    def make_choice(self, choice):
        self.status_label.config(text="")  # Clear any previous status messages


#Main Code
        # --- Decision Tree (using original logic, but adapted) ---
        # Round 1
        if self.current_prompt == startpoint:
            if choice == "1":
                self.current_prompt = path1
                self.create_buttons(path1)
            elif choice == "2":
                self.current_prompt = path2
                self.create_buttons(path2)
            elif choice == "3":
                self.current_prompt = path3
                self.create_buttons(path3)
            else:
                self.show_error("Invalid choice. Please select a valid option.") #go Fug yourself, THERE IS 3 BUTTON, HOW TF U HAVE A FOURTH TO TRIGGER THE FUCKING ERROR. 

        # Round 2 (Path 1)
        elif self.current_prompt == path1:
            if choice == "1":
                self.current_prompt = path11
                self.create_buttons(path11)
            elif choice == "2":
                self.current_prompt = path12
                self.create_buttons(path12)
            elif choice == "3":
                self.current_prompt = path13
                self.create_buttons(path13)
            else:
                self.show_error("Invalid choice.") #Go fug yourself

        # Round 2 (Path 2)
        elif self.current_prompt == path2:
            if choice == "1":
                self.current_prompt = path21
                self.create_buttons(path21)
            elif choice == "2":
                self.current_prompt = path22
                self.create_buttons(path22)
            elif choice == "3":
                self.current_prompt = path23
                self.create_buttons(path23)
            else:
                self.show_error("Invalid choice.") #go fug yourself

        # Round 2 (Path 3)
        elif self.current_prompt == path3:
            if choice == "1":
                self.current_prompt = path31
                self.create_buttons(path31)
            elif choice == "2":
                self.current_prompt = path32
                self.create_buttons(path32)
            elif choice == "3":
                self.current_prompt = path33
                self.create_buttons(path33)
            else:
                self.show_error("Invalid choice.") #go fug yourself

        # --- Round 3 and Endings ---
        elif self.current_prompt == path11: #meh, good enough
            self.display_ending(choice, "1-1")
        elif self.current_prompt == path12:
            self.display_ending(choice, "1-2")
        elif self.current_prompt == path13:
            self.display_ending(choice, "1-3")
        elif self.current_prompt == path21:
            self.display_ending(choice, "2-1")
        elif self.current_prompt == path22:
            self.display_ending(choice, "2-2")
        elif self.current_prompt == path23:
            self.display_ending(choice, "2-3")
        elif self.current_prompt == path31:
            self.display_ending(choice, "3-1")
        elif self.current_prompt == path32:
            self.display_ending(choice, "3-2")
        elif self.current_prompt == path33:
             self.display_ending(choice, "3-3")
        else:
            self.show_error("Unexpected game state. Please restart.") # Should not happen.
#End of main code. 
    def display_ending(self, choice, base_path):
        ending_key = f"{base_path}-{choice}"
        if ending_key in endings:
            self.update_text(endings[ending_key])
            self.game_over()  # Game over after displaying the ending
        else:
            self.show_error("Invalid ending key.  Game logic error.")
            self.game_over()


    def game_over(self):
        # Disable all buttons
        for button in self.buttons:
            button.config(state=tk.DISABLED)
        self.status_label.config(text="Game Over.  Thanks for playing!") # A nice message for who bored enough to read.

        # Add a "Play Again" button for you to explored the game.
        play_again_button = ttk.Button(self.button_frame, text="Play Again", command=self.restart_game)
        play_again_button.grid(row=len(self.buttons) // 2, column=0, columnspan=2, pady=10)
        self.buttons.append(play_again_button)



    def restart_game(self):
        # Reset the text area and current prompt
        self.update_text(text1)  # Show the initial text
        self.current_prompt = startpoint
        self.create_buttons(startpoint)  # Recreate initial buttons
        self.status_label.config(text="")  # Clear status label 

    def show_error(self, message):
        self.status_label.config(text=message)


root = tk.Tk()
game = SaharaGame(root)
game.current_prompt = startpoint  # Initialize current_prompt
root.mainloop()