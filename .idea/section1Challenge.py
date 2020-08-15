print("""Please choose an option from the list below:
1. Learn Python
2. Learn Javascript
3. Watch a movie
4. Go to the gym
5. Do nothing
0. Exit""")


#below is my first attempt
# print()
# choice = int(input("Type the number associated with the option you choose: "))
# print()
#
# while choice < 6:
#     if choice == 0:
#         print("You closed the program!")
#         break
#
#     elif choice == 1:
#         print("You chose option number {}\nThat is a great choice! Python is cool!".format(choice))
#
#
#
#     elif choice == 2:
#         print("You chose option number {}\nNice choice! Javascript is the power of Web Dev.".format(choice))
#
#
#     elif choice == 3:
#         print("You chose option number {}\nOkay! Hope you'll choose a nice movie!".format(choice))
#
#
#     elif choice == 4:
#         print("You chose option number {}\nTime for some gains! Yee boyy!".format(choice))
#
#
#     else:
#         print("You chose option number {}\nYou lazy bastard!".format(choice))
#
#     print()
#     choice = int(input("If you want you can choose another option: "))
#     print()
# else:
#     print("Please choose a valid option, by choosing one of the associated numbers!")

#below is the code after checking the solution
#this one is better - it also repeats the menu if an invalid option is chosen
while True:
    choice = input()

    if choice == "0":
        break

    elif choice in "12345":
        print("You chose {}".format(choice))

    else:
        print("""Please choose an option from the list below:
1. Learn Python
2. Learn Javascript
3. Watch a movie
4. Go to the gym
5. Do nothing
0. Exit""")
