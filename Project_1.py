import random


def compare(user_input,com_input) :
    if user_input == com_input :
        print("It's tie")

    elif  user_input  not  in ["Snak","Water","Gun"] :
             print("invalid input..")

    elif (user_input == "Snak" and com_input == "Water") or \
         ( user_input == "Water" and com_input == "Gun" ) or \
         ( user_input == "Gun" and com_input == "Snak" ) :
        print("You are win !!")

    else    :
        print("You are lose")
         
    return 1

def play() :
    user_input = input("Enter input (Snak,Water,Gun)").capitalize()
    com_input = random.choice(["Snak","Water","Gun"])

    
    compare(user_input,com_input)

play()