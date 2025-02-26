print("""You are a goblin from Florida and you try to get to DC. 
Your quest: To steal the Declaration of Independence and replace it with a love letter to gators.
""")

choice = input("""
How do you travel?
1. By Car (borrowed...permanently)
2. By Plane (sneaking on is an option)
3. On foot (gotta love those scenic routes)
""")

if choice == "1":
    choice = input("""
You "borrowed" a beat-up pickup truck. After a few hours, smoke billows from the engine! You're stranded in rural Georgia.
1. Try to fix the truck yourself. (You know...goblin engineering!)
2. Hitchhike with a sign that says "DC or Bust! Will Work for Gas."
3. Abandon the truck and try to steal a bicycle.
""")
    if choice == "1":
        choice = input("""
You tinker with the engine, hitting it with a rock and spitting on it. Miraculously, it sputters back to life! But now there's a strange knocking sound...
1. Ignore the knocking and floor it! (Hope for the best!)
2. Try to figure out what's causing the knocking. (Probably a snake.)
3. Pull over and trade the truck to some local moonshiners for a donkey and wagon.
""")
        if choice == "1":
            print("The engine explodes spectacularly a few miles later. You lose...and smell like burnt rubber.")
        elif choice == "2":
            print("The 'knocking' turns out to be a family of squirrels who are very unhappy with your engine modifications. They bite you repeatedly. Game Over.")
        elif choice == "3":
            print("The donkey, Bessie, is surprisingly fast! You arrive in DC, albeit smelling strongly of manure. You manage to evade security due to the distraction of your smell, replace the documents, and ride bessie back to Florida. You win!")
        else:
            print("Invalid choice. A gator eats you out of confusion. You lose.")
    elif choice == "2":
        choice = input("""
A kindly old lady picks you up. She seems a bit...eccentric.
1. Try to subtly convince her to drive you all the way to DC.
2. Tell her the truth about your mission (maybe she's a secret goblin sympathizer?).
3. "Accidentally" spill motor oil on her seat and demand she take you to DC to compensate.
""")
        if choice == "1":
            print("She drops you off at a bingo hall three towns over and thinks that you're crazy, a waste of a ride. You are far from your goal. Game Over.")
        elif choice == "2":
            print("She screams, pulls over, and calls the police. You are arrested and deported back to Florida. Game Over.")
        elif choice == "3":
            print("She is enraged and kicks you out of the car. You lose.")
        else:
            print("Invalid choice. A gator eats you out of confusion. You lose.")
    elif choice == "3":
        choice = input("""
You find a rusty, one-wheeled bicycle leaning against a barn. It's better than nothing!
1. Start pedaling towards DC! (Ignore the wobbly wheel.)
2. Try to find another wheel (maybe from a passing lawnmower?).
3. Use the bicycle as a weapon to steal a better bicycle from a child.
""")
        if choice == "1":
            print("You fall off the bicycle every few minutes and get eaten by an animal. You lose.")
        elif choice == "2":
            print("A lawnmower wheel doesn't fit! You waste valuable time and get eaten by a gator. Game Over.")
        elif choice == "3":
            print("The child's parents are not happy. They call the police. Game Over.")
        else:
            print("Invalid choice. A gator eats you out of confusion. You lose.")
    else:
        print("Invalid choice. A gator eats you out of confusion. You lose.")

elif choice == "2":
    choice = input("""
You arrive at the airport, looking decidedly...un-airport-like. Security is tight. Which airline do you try to sneak onto?
1. United Airlines (They seem perpetually confused, good for sneaking!)
2. Delta Airlines (Maybe you can blend in with the business travelers?)
3. American Airlines (Go big or go home, right?)
""")
    if choice == "1":
        print("You get on the plane. While switching the documents, you are confronted by security. Game Over.")
    elif choice == "2":
        print("You get on the plane. While switching the documents, you are confronted by security. Game Over.")
    elif choice == "3":
        print("You get on the plane. While switching the documents, you are confronted by security. Game Over.")
    else:
        print("Invalid choice. A gator eats you out of confusion. You lose.")
elif choice == "3":
    choice = input("""
You decide to walk. 919 miles! You're tougher than you look (probably).
1. Try to scavenge for food and supplies along the way.
2. Rely on the kindness of strangers (good luck with that).
3. Embrace your inner goblin and raid gas stations for snacks and road maps.
""")
    if choice == "1":
        print("You starve to death miles away. Game Over.")
    elif choice == "2":
        print("People avoid you at all costs. Game Over.")
    elif choice == "3":
        print("You become a legend. The local news reports about a tiny green bandit terrorizing the southeast. You get on the news and are stopped. Game Over.")
    else:
        print("Invalid choice. A gator eats you out of confusion. You lose.")

else:
    print("Invalid choice. A gator eats you out of confusion. You lose.")
