'''A password generator is a useful tool that generates
strong and random passwords forusers. This project aims to
create a password generator application using Python, allowing users to specify
the length and complexity of the password.
User Input: Prompt the user to specify the desired length of the password.
Generate Password: Use a combination of random characters to generate a password ofthe specified length.
Display the Password: Print the generated password on the screen'''

import random
def alpha():
    alph = ['q','w','e','r','t','y','u','i','o','p','l','k','j','h','g','f','d','s','a','z','x','c','v','b','n','m']
    rand_alpha = random.choice(alph)
    return rand_alpha

def number():
    num = ['1','2','3','4','5','6','7','8','9','0']
    rand_num = random.choice(num)
    return rand_num

def special():
    spec = ['~','!','@','#','$','%','^','&','*','?']
    rand_spe = random.choice(spec)
    return rand_spe


def strength(stg):
    if stg == "easy":
        choice = 1
        return choice
    elif stg == "mod":
        choice = random.randint(1, 2)
        return choice
    elif stg == "hard":
        choice = random.randint(1, 3)
        return choice
    

def chooser(choice):    
    if choice == 1:
        ch= alpha()
    elif choice == 2:
        ch = number()
    else:
        ch = special()

    return ch

def generator():
    len = int(input("\nEnter the length of the password: "))
    stg = input("Enter strength of password (easy, mod or hard): ").lower()
    string = ''
    
    for i in range(0 , len):
        choice = strength(stg)
        str = chooser(choice)
        string = string + str
        
    return string         

#MAIN CODE

while True:
    print ("\n-----------------------------------------------")
    print(f"\nDo you want a new Password?(y/n)\nPress any other key to quit the program")
    choice = input("").upper()
    repeat = ''
    if choice == "Y":
        print ("\nPassword generated is: ", generator())
    else:
        break
