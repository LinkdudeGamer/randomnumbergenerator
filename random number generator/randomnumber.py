import random

def cls():
    print('\n' *100)

print("Welcome to a simple random number generator!")

while True:
    try:
        rangelower =int(input("Please enter your smallest number >> "))
    except ValueError:
        cls()
        print("This is not a number, please enter a number")
    else:
        try:
            rangehigher =int(input("Now, enter your bigger number >> "))        
        except ValueError:
            cls()
            print("This is not a number, please enter a number")
        else:
            if rangehigher < rangelower:
                cls()
                print("Your number is too small!")
            else:
                randomnumber = random.randint(rangelower, rangehigher)
                print("Your random number is: ", randomnumber)

        
            
            


