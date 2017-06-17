import random

print("Welcome to a simple random number generator!")

while True:
    try:
        rangelower =int(input("Please enter your smallest number >> "))
    except ValueError:
        clear()
        print("This is not a number, please enter a number")
    else:
        try:
            rangehigher =int(input("Now, enter your bigger number >> "))        
        except ValueError:
           clear()
            print("This is not a number, please enter a number")
        else:
            if rangehigher < rangelower:
                clear()
                print("Your number is too small!")
            else:
                clear()
                randomnumber = random.randint(rangelower, rangehigher)
                print("Your random number is: ", randomnumber)

        
            
            


