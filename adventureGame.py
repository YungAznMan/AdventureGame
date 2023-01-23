def OpeningScene():
    directions = ["left", "right", "forward"]
    print("You find yourself starting at a cross in the road, you can choose to go any direction.")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right/backward/forward")
        userInput = input()
        if userInput == "left":
            trapDoor()
        elif userInput == "right":
            prayerRoom()
        elif userInput == "forward":
            smallOpening()
        elif userInput == "backward":
            boobyDeath()
        else:
            print("Please enter a valid choice.")
            

def trapDoor():
    directions = ["left", "forward"]
    print("Oh no!!!")
    print("You trip a wire! The floor falls beneath you; as you're falling you manage to catch yourself on a ledge.")
    print("Back to firm footing, you are ready to keep moving.")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right/backward")
        userInput = input()
        if userInput == "left":
            scorpionSceneOne()
        elif userInput == "right":
            slideScene()
        elif userInput == "backward":
            OpeningScene()
        else:
            print("Please enter a valid choice.")

def scorpionSceneOne():
    directions = ["left", "right"]
    print("You come to a room that is completely overrun with deadly venomous scorpions.")
    print("Looking around you see tiles, that the scorpions do not rest on. They make a path leading to the next room.")
    print("Would you like to take the left or right path of tiles?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right")
        userInput = input()
        if userInput == "left":
            scorpionSceneTwo()
        elif userInput == "right":
            print("The tile collapses and you begin to fall...")
            deathScene()
        else:
            print("Please enter a valid choice.")

def scorpionSceneTwo():
    directions = ["left", "right"]
    print("The tile manages to take your weight completely, two more tiles appear in front of you...")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right")
        userInput = input()
        if userInput == "left":
            print("The tile collapses and you begin to fall...")
            deathScene()
        elif userInput == "right":
            scorpionSceneThree()
        else:
            print("Please enter a valid choice.")

def scorpionSceneThree():
    directions = ["forward"]
    print("You only have one more jump to make.")
    userInput = ""
    while userInput not in directions:
        print("Options: forward")
        userInput = input()
        if userInput == "forward":
            print("You find a way out and have made it out to freedom. Congratulations!")
            winningScene()
        else:
            print("Please enter a valid choice.")

def prayerRoom():
    directions = ["backward"]
    print("You enter a sacred prayer room...")
    print("You feel a heavy gaze upon you")
    print("Starting to feel uneasy, you must turn back.")
    userInput = ""
    while userInput not in directions:
        print("Options: backward")
        userInput = input()
        if userInput == "backward":
            print("As you leave, you feel your vigour come back.")
            OpeningScene()
        else:
            print("Please enter a valid choice.")

def smallOpening():
    directions = ["yes", "no"]
    print("You find a large room with a small opening at the end.")
    print("Would you like to try and squeeze through?")
    userInput = ""
    while userInput not in directions:
        print("Options: yes/no")
        userInput = input()
        if userInput == "yes":
            print("You try to squeeze you body through the small opening...")
            deathScene()
        elif userInput == "no":
            print("You have decided to turn back.")
            OpeningScene()
        else:
            print("Please enter a valid choice.")

def boobyDeath():
    print("You begin to walk down a long and narrow corridor.")
    print("You seem to have stepped on a booby trap!")
    print("Suddenly, darts are being shot from the walls as spiders are dropping from the ceiling.")
    deathScene()
    quit()

def slideScene():
    directions = ["left", "right"]
    print("A sheer drop is presented in front of you, with two paths that lead to a slide.")
    print("There is a slide to the left and a slide to the right.")
    print("Which would you like to take?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right")
        userInput = input()
        if userInput == "left":
            print("Wheeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            print("*Splat*")
            deathScene()
        if userInput == "right":
            print("Wheeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            print("The slide appears to have been an emergency exit, used by the workers at the time.")
            winningScene()


def deathScene():
    print("It appears you have made a grave error.")
    print("You are dead.")
    quit()

def winningScene():
    print("Well done, you have escaped with your life!")
    print("Shame there was no treasure.")
    quit()

if __name__ == "__main__":
    while True:
        print("Welcome to The Pharoah's Tomb!")
        print("As an adventurer, you have entered the first of the catacombs leading to riches, only heard of in stories.")
        print("You take one turn too many, and have found yourself lost from the group.")
        print("There are different directions you can take to begin this journey.")
        print(" 'You here a faint and eerie noise' ")
        print("What... is your... name?...")
        name = input()
        print("The crown... shall fall... to you... " + name + ".")
        OpeningScene()
