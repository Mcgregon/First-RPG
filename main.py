exit = False

gender = "not defined"
age = "not defined"

def main():
    global exit

    while not exit:
        choice = main_menu()

        # Choices:
        # (1): continue game
        # (2): new character
        # (2): options
        # (3): exit
        if choice == 1:
            new_character()
        elif choice == 2:
            print("You chose options")
            #hvordan linker man infomationer til spille gennem en anden tab(option)
        elif choice == 3:
            print("You chose exit")
            exit = True
        else:
            print("Du valgte forkert eller noget")

def main_menu():
    # Her vælger vi en retning
    print("(1) New Character")
    print("(2) Options")
    print("(3) Exit")
    choice = int(input("Vælg: "))
    return choice

def new_character():
    global gender
    global age

    gender = "not chosen"
    while not (gender == "man" or gender == "woman"):
        gender = input("Choose gender (man/woman): ")
    
    print("You chose a " + gender)
    
    age = "not chosen"
    while not (age == "young" or age == "adult" or age == "old" or age == "ancient"):
        age = input("Choose age group (young/adult/old/ancient): ")
    
    print("You have chosen to be " + age )
    
    if age == "young":
        print("You're a " + age + " " + gender)
    else:
        print("You're an " + age + " " + gender)

    exit_game()

def exit_game():
    global exit
    exit = True

# Mål; lave et power creep rpg

# Integer (int): Heltal 1 2 3 -1 0 = et valg
# String (str, String): Række tegn, ord, sætning, gåseøjne omkring = infomation / en række tegn men har ikke noget med programmet at gøre
# "hej", "wow", "123"
# Float (float): Decimaltal, double er det samme (i de fleste sammenhænge) =samme som hvad?
# Boolean (bool): Ja/Nej, True/False, er lotte et køn?= nej hun er køn
# Null/nil: Intet, hvis en variabel ikke er sat til noget er den det her

# rør ikke ved denne!! udråbstegn 
if __name__ == "__main__":
    main()