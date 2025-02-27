#Text storange #i don't want the whole code below to be a pile of sh##, so, here we go. And, im not good at story writing, so, i get a bit of assits with Grammarly: Free AI Writing Assistance

#Grammarly
#https://www.grammarly.com
#Grammarly makes AI writing convenient. Work smarter with personalized AI guidance and text generation on any app or website.

#lol u got ads in source code 
text1 = "You stand at the edge of the scorching Sahara Desert. The wind whips sand around you, stinging your eyes. Legend speaks of the Lost Amulet of Zerzura, a powerful artifact hidden within a forgotten oasis. You, a seasoned explorer, are determined to find it. Before you lie three paths, shrouded in the swirling sands:"
startpoint = """
1. Head straight into the dunes, following the faint tracks of a long-dead caravan.
2. Search for a nearby Bedouin encampment, hoping to gain information from the locals.
3. Climb the towering rock formation to your left, seeking a vantage point to survey the landscape.
"""

# Round 1 Paths
path1 = """
You trudge through the sand, the sun beating down mercilessly. The caravan tracks are fading, but you press on. You find the remnants of a shattered wagon.
Check inside the ruined caravan. (Leads to Round 2, Path 1-1)
Continue on the same path as the caravan, despite the destruction. (Leads to Round 2, Path 1-2)
Change course and try a new path through the dunes. (Leads to Round 2, Path 1-3)
"""

path2 = """
You spot smoke in the distance and eventually reach a small Bedouin camp. The people are wary but offer you water and shade.
Politely inquire about the Amulet of Zerzura. (Leads to Round 2, Path 2-1)
Offer them a valuable item from your pack in exchange for information. (Leads to Round 2, Path 2-2)
Rest for a while and leave quietly in the night, figuring they know nothing. (Leads to Round 2, Path 2-3)
"""

path3 = """
The climb is arduous, but you reach the top, breathless. The desert stretches before you, a vast ocean of sand. You notice a peculiar glint in the distance.
Carefully descend and head towards the glint. (Leads to Round 2, Path 3-1)
Use your binoculars to get a closer look at the glint. (Leads to Round 2, Path 3-2)
The height makes you dizzy. Descend and choose a different path at the base of the rocks. (Leads to Round 2, Path 3-3)
"""

# Round 2 Paths
path11 = """
You rummage through the wreckage and find a tattered journal.
Read the journal, looking for clues. (Leads to Round 3, Path 1-1-1)
Ignore the journal, searching for supplies instead. (Leads to Round 3, Path 1-1-2)
The sight of the destroyed caravan unnerves you. Abandon the search and head back. (Leads to Round 3, Path 1-1-3)
"""

path12 = """
You walk for hours, following the faint tracks. The sun is relentless, and your water is running low. You spot an oasis shimmer on air!
Approach the center, where a great ancient temple can be see.
Look on other thing the oasis has, like tree or the lake.
It can be a trap! retreat and leave is the better idea!
"""

path13 = """
You veer off the caravan path, striking out in a new direction. You stumble upon a partially buried stone marker.
Dig around the marker, hoping to find something. (Leads to Round 3, Path 1-3-1)
Use the marker as a guide, heading in the direction it seems to point. (Leads to Round 3, Path 1-3-2)
Ignore the marker; it's probably just a rock. (Leads to Round 3, Path 1-3-3)
"""

path21 = """
The Bedouins listen to your story, their faces grave. An elder speaks.
Listen intently to the elder's warning about the dangers. (Leads to Round 3, Path 2-1-1)
Dismiss the warning as superstition and press for details. (Leads to Round 3, Path 2-1-2)
Thank the elder for their time and offer a small gift. (Leads to Round 3, Path 2-1-3)
"""

path22 = """
You offer a silver compass. A young Bedouin's eyes light up, and he whispers to you.
Follow the young Bedouin as he leads you away from the camp. (Leads to Round 3, Path 2-2-1)
Ask the young Bedouin to explain his knowledge in front of the others. (Leads to Round 3, Path 2-2-2)
Decide the compass was too valuable and try to take it back. (Leads to Round 3, Path 2-2-3)
"""

path23 = """
You slip away under the cover of darkness, feeling a bit guilty but determined.
Head east, believing the oasis lies in that direction. (Leads to Round 3, Path 2-3-1)
Head west, thinking the Bedouins were trying to mislead you. (Leads to Round 3, Path 2-3-2)
Circle back to the rock formation you saw earlier, rethinking your strategy. (Leads to Round 3, Path 2-3-3)
"""

path31 = """
You scramble down the rocks and head towards the glint. It's a small, metal box reflecting the sunlight.
Carefully open the metal box. (Leads to Round 3, Path 3-1-1)
Bury the box, thinking it might be a trap. (Leads to Round 3, Path 3-1-2)
Take the box with you but don't open it yet. (Leads to Round 3, Path 3-1-3)
"""

path32 = """
You focus your binoculars. You see what appears to be a ruined temple, half-buried in the sand.
Make your way towards the ruined temple, using the binoculars as a guide. (Leads to Round 3, Path 3-2-1)
Decide the temple is too far and look for a closer landmark. (Leads to Round 3, Path 3-2-2)
You spot a sandstorm brewing. Seek shelter immediately. (Leads to Round 3, Path 3-2-3)
"""

path33 = """
You climb down and choose a path leading away from the rock formation, towards a cluster of date palms in the distance.
Head directly towards the date palms, hoping for water and shade. (Leads to Round 3, Path 3-3-1)
Approach the date palms cautiously, wary of potential dangers. (Leads to Round 3, Path 3-3-2)
Decide the palms are a mirage and head in a different direction. (Leads to Round 3, Path 3-3-3)
"""
# Round 3 Endings (as a dictionary for easy access)
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


# print(endings["1-1-1"])




















print("""
 ######      ###    ##     ## ######## 
##    ##    ## ##   ###   ### ##       
##         ##   ##  #### #### ##       
##   #### ##     ## ## ### ## ######   
##    ##  ######### ##     ## ##       
##    ##  ##     ## ##     ## ##       
 ######   ##     ## ##     ## ######## 

""")
print(text1)

choice = input(startpoint) 
if choice == "1":

    choice = input(path1) 
    if choice == "1":

        choice = input(path11) 
        if choice == "1":
            print("Layer 1.2") 
        elif choice == "2":
            print("Layer 1.2") 
        elif choice == "3":
            print("Layer 1.2") 
        else:
            print("Error PlaceHolder")



    elif choice == "2":
        
        choice = input(path12) 
        if choice == "1":
            print("Layer 1.2") 
        elif choice == "2":
            print("Layer 1.2") 
        elif choice == "3":
            print("Layer 1.2") 
        else:
            print("Error PlaceHolder")

    elif choice == "3":

        choice = input(path13) 
        if choice == "1":
            print("Layer 1.2") 
        elif choice == "2":
            print("Layer 1.2") 
        elif choice == "3":
            print("Layer 1.2") 
        else:
            print("Error PlaceHolder")

    else:
        print("Error PlaceHolder")

elif choice == "2":

    choice = input(path2) 
    if choice == "1":
        print("Layer 1.2") 
    elif choice == "2":
        print("Layer 1.2") 
    elif choice == "3":
        print("Layer 1.2") 
    else:
        print("Error PlaceHolder")

elif choice == "3":

    choice = input(path3) 
    if choice == "1":
        print("Layer 1.2") 
    elif choice == "2":
        print("Layer 1.2") 
    elif choice == "3":
        print("Layer 1.2") 
    else:
        print("Error PlaceHolder")

else:
    print("Error PlaceHolder")