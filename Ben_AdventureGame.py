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
path11 = """
You rummage through the wreckage and find a tattered journal.
Read the journal, looking for clues. (Leads to Round 3, Path 1-1-1)
Ignore the journal, searching for supplies instead. (Leads to Round 3, Path 1-1-2)
The sight of the destroyed caravan unnerves you. Abandon the search and head back. (Leads to Round 3, Path 1-1-3)
"""























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
        print("Layer 1.2") 
    elif choice == "3":
        print("Layer 1.2") 
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