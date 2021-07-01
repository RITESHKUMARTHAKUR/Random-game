#import random library
import random  

#Heading
print("\n\t-: THIS IS THE GUESS THE NUMBER GAME :-") 
# preventing variable [a] from garbage value    
a = None

# While case for repeating loop until [q] is Pressed 
while True:
    #Selecting the range for random function
    h = int(input("\nENTER THE RANGE: "))  

    # using randint function to select a number      
    n = random.randint(1, h)                     
    print("\nENTER A NUMBER BETWEEN 1 to %d OR PRESS [q] TO EXIT :- " % h)

    # creating [a] variable to check the given number is integer
    a = input("Enter your choice: ")   

    # if and elif conditions to check datatype 
    # End of while loop 
    if a == "q":
        # Exit message
        print("THANKS FOR PLAYING !!\n")
        break
    
    # Alphabetical character is encountered 
    elif a[0].isalpha():
        # Alpha character message
        # Continuing the game 
        print("invalid character, TRY ANOTHER TIME !! ")
        continue

    # Integer input is encountered
    elif a[0].isdigit():
        # Min body of the Game
        # Repeating While loop until choosen [n] value is equal to the number choosen by the player 
        while True:
            # First statement
            a = input("YOUR TRY: ")
            # Initialising [a] as Integer 
            # On creating [a] was a String by Defualt
            a = int(a)

            # Low case if player enters number lower than Choosen Number 
            if a < n:
                print("too low")
            # High case if player enters number Greater than Choosen Number
            if a > n:
                print("too high")
            # Equal casee when the player Enters The same Number as Choosen
            if a == n:
                # End statement
                print("Congratulations, You won !!")
                break

    # Invalid case 
    # IF the Player enters an Special character 
    else:
        # Invalid statement 
        print("invalid character, IF YOU Want to exit press [q] or press [c] to continue !! ")

        # Taking input weather to continue or Exit
        b = input()

        # Exit statement 
        if b == "q":
            print("THANKYOU !!")
            # To exit from the while loop
            break
        
        # Continue statement to continue to the while loop 
        else:
            continue
