exit = False

def main():
    global exit

    while not exit:
        choice = main_menu()

        if choice == 1:
            start()
            #vi skal have lave en run.exe funktion her
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
    print("(1) Start")
    print("(2) Options")
    print("(3) Exit")
    choice = int(input("Vælg: "))
    return choice

def start():
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

    save_character(gender, age)
    character_overview()

def save_character(gender, age):
    char = Character(gender, age)
    char.introduce()
    
def character_overview():
    start_game()

def start_game():
    global exit
    exit = True

class Character:
    gender = "gender"
    age = "age"

    def __init__(self, gender, age):
        self.gender = gender
        self.age = age
    
    def introduce(self):
        print("Characters's age is " + self.age + " and it's gender is " + self.gender) 

    

# Mål; lave et power creep rpg

# Integer (int): Heltal 1 2 3 -1 0 = et valg
# String (str, String): Række tegn, ord, sætning, gåseøjne omkring = infomation / en række tegn men har ikke noget med programmet at gøre
# "hej", "wow", "123"
# Float (float): Decimaltal, double er det samme (i de fleste sammenhænge) =samme som hvad?
# Boolean (bool): Ja/Nej, True/False, er lotte et køn?= nej hun er køn
# Null/nil: Intet

# rør ikke ved denne!! udråbstegn 
if __name__ == "__main__":
    main()