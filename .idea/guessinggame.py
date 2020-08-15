answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Pls guess higher")
    else: #guess must be greater than the answer
        print("Pls guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it!")
    else:
        print("Sorry, you have not guessed it!")
else:
    print("You got it first time!")

# pt a comenta un paragraf, fara sa punem # la fiecare linie
#dam drag peste tot paragraful si apoi folosim CTRL + /
#si imi va pune # la toate liniile cuprinse


# if guess < answer:
#     print("Pls guess higher!")
#     guess = int(input())
#     if guess == answer:
#         print("Good job! You guessed it!")
#     else:
#         print("Sorry! You did not guess correctly!")
#
# elif guess > answer:
#     print("Pls guess lower!")
#     guess = int(input())
#     if guess == answer:
#         print("Good job! You guessed it!")
#     else:
#         print("Sorry! You did not guess correctly!")
#
# else:
#     print("You got it!")

#U use if when you want the program to evaluate something
#elif is a method to make the program evaluate a second thing
#else for example does not evaluate anything - it just jumps to the output