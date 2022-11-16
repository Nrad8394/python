#we call the random module to generate a random number
import random 

def inital():
    initializer = input("Press Enter to generate a random number(to quit press anycharacter then Enter): ")

    if initializer == "":
        print(random.random())
        inital()
    else:
        exit()

inital()