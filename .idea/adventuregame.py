available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    #as soon as a valid input from the list is entered
    #the condition from while becomes false and the loop ends

    if chosen_exit.casefold() == "quit":
        #casefold face ca inputul sa nu conteze daca e scris cu uppercase or lower case
        print("Game Over!")
        break

    elif chosen_exit in available_exits:
        print("You finally got out of there!")
        break

