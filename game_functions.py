"""The functions utilized within my project"""

user_name = ""
user_weapon = ""
# Global variable initialized at 2, representing how many chances the user gets to save campus before they run out of health
user_health = 2


def ask(option):
    """Takes in user input as an option and compares it to see if it is one of the two answer options given during the entire game
    Parameters
    ----------
    option : str
    
    Returns
    -------
    choice : str
    """
    # The user's input is recognized by the function and is capitalized so that it may be checked by my while loop and run the rest of the functions
    choice = input(option).upper()
    # This while loops reiterates for the entirety of the game to check that the user input is only 'A' or 'B'
    while choice != "A" and choice != "B":
        print("Please choose A or B only \n")
        choice = input(option).upper()
    assert len(choice) == 1
    return choice


def set_the_scene():
    """Allows the user to play and runs the sequence of events down below
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    # Calls upon the global variable before introducing the variable again, or else it would be considered undefined
    global user_health
    user_health = 2
    print("Hi I'm Aster, a fairy that lives above campus in the clouds. It's been a year since everyone left campus in a panic. COVID left the campus in ruins and monsters have taken over. I can no longer hold off them off and need help! It's up to you and a companion who you'll meet later, to save campus from the monsters so everyone can return in the Fall. Choose A or B to progress your adventure.")
    choice = ask("Will you help me? \nA. Yes or B. No \n")
    assert isinstance(choice, str)
    # Compares if user input is A, if so it will continue onto the next task
    if choice == "A":
        get_name()
    # Compares if the user input is B, if so it will end the game
    elif choice == "B":
        no_play()

        
def get_name():
    """Asks the user for their name, which will be stored in a global variable and concatenates it with a message
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    print("Where are my manners, I totally forgot!")
    # Calls upon the global variable before it is listed again in my code so that it can change once inside my function and stores ther user's name
    global user_name
    # Takes what the user inputted and is reintroduced in this function 
    user_name = input("What's your name? \n")
    print("Alright " + user_name + ", let's get moving!")
    get_weapon()
    

def get_weapon():
    """Asks the user to choose which weapon they'd like and stores it to a global variable where it will be called during a battle later
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    print("A weapon will come in handy, choose your pick!")
    choice = ask("Would you like a trident I got from King Triton or would you like a wand forged with Sungod's energy? \nA. Trident or B. Wand\n")
    # Calls upon the global variable before it is listed again in my code and it will change to the choice the user picks once inside my function
    global user_weapon
    if choice == "A":
        print("Now you can rule the land and sea!")
        user_weapon = "trident"
    else:
        print("Bippity bopity boo, let's take on the school!")
        user_weapon = "wand"
    first_boss()

    
def first_boss():
    """Allows user to choose which action they'd like to perform as they continue on their adventure
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    print("You're walking down Library Walk when a lonely tabler begs you to take their last flyer.")
    choice = ask("What do you do? \nA. Debate with him or B. Take his flyer\n")
    if choice == "A":
        print("Nice work. With your argumentative skills, we quickly defeated our first monster!")
        second_boss()
    else:
        print("You end up talking to him for what seems like forever. We lost some time!")
        # Take_damage() passes in 1 because if a person chooses wrong here, they would lose one health and this amount is subtracted by their current total chances
        take_damage(1)
        if user_health <= 0:
            game_over()
        else:
            second_boss()
        
        
def second_boss():
    """Allows the user to choose how to fight the raccoon monster, while also calling back the user_weapon global variable
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    print("You continue on your mission. Walking up Peterson Hall Bike Lane, you encounter a second monster, a giant raccoon who is looking to fight.")
    choice = ask("What do you want to do? \nA. Use your weapon to conjure a giant cage or B. Toss the raccoon food\n")
    if choice == "A":
        print("Your " + user_weapon + " traps the raccoon! Monster two, down.")
        third_boss()
    else:
        print("The racoon took your food and beat you up.")
         # Take_damage() passes in 1 because if a person chooses wrong here, they would lose one health and this amount is subtracted by their current total chances 
        take_damage(1)
        if user_health <= 0:
            game_over()
        else:
            third_boss()
     
    
def third_boss():
    """Scene for the last mob that once again calls the global user_weapon variable
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    print("Quarantine 15 hit you hard and you're struggling to make it up the stairs by the Cognitive Science building. You turn to the right and see your worst nightmare. A giant 50 multiple choice question packet. To make it worse, its got an essay question too. You can't take down this opponent alone! You run into the Cog Sci bulding to look for help.")
    choice = ask("Who will you choose to help you take down this final boss?\nA. Professor Bardolph with her quick thinking skills or B. Professor Walker with her humor and wit\n")
    if choice == "A":
        print("Professor Bardolph uses her quick thinking skills to distract the exam mob and you utilize your " + user_weapon + " to finish off the mob!")
        celebration()
    else:
        print("Professor Walker distracted the exam mob with a funny joke and you utilize your " + user_weapon + " to finish off the mob!")
        celebration()
    
    
def celebration():
    """Creates the celebratory message concatenating a sentence with the user's name which was stored in a global variable
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    print("Splendid job " + user_name + "! You and the professor were able to save campus. Now everyone can return in the fall, I hope to meet you again soon hero.")

    
def game_over():
    """Gives the user the option to play again if they ran out of health. If they wanted to play again it runs the set_the_scene() again 
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    print("You ran out of health and weren't able to save campus. Would you like to play again?")
    choice = ask("A. Yes or B. No \n")
    if choice == "A":
    #if a choice is A then the game would restart 
        set_the_scene()
    else:
        print("Now who will save campus?")
        

def no_play():
    """Asks the user if they're sure that they want to play or not and then prints a sassy statement if they choose that they don't want to play. Also continues the storyline if they would like to play
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    print("We weren't able to save campus. Are you sure you don't want to play?")
    choice = ask("A. Yes play or B. No play \n")
    if choice == "A":
        set_the_scene()
    else:
        print("Suit yourself >:(")
        

    
def take_damage(damage):
    """Takes away the user's health each time they choose the wrong path and updates it as the game progresses
    Parameters
    ----------
    damage: int
        damage is initialized as 2 and is taken in to be subtracted by one if the player doesn't choose successfully
    
    Returns
    -------
    int
    """
    # Global variable is called before my user_health variable so that it is able to change once inside this function
    global user_health
    # Compares if current damage is less than or equal to 0
    if damage <= 0:
        print("Are you immortal? That's not allowed!")
    else:
        #The user_health variable is defined as the current user_health subtracted by the one damage taken during each bad choice
        user_health = user_health - damage
        assert user_health < 2
        if user_health > 0:
            print("We lost some health, but let's keep moving forward!")
            
            
set_the_scene()
