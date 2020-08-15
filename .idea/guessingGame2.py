import random
#Python are un random generator built-in
#you can access it from the random library which needs to be imported
highest = 10
answer = random.randint(1, highest)
print(answer) #TODO: remove after testing - user should not see the correct answer

#am ales sa folosim highest in loc de un numar pt a nu trebui
#sa schimb numarul respective peste tot in cod; asa trebuie sa fac o singura schimbare
guess = int(input("You can enter 0 to quit the game! \nPlease guess number between 1 and {}: "
                  .format(highest)))
print()
tries = 1 #the first input is counted as a try

while guess != answer:
    if guess == 0:
        break

    elif guess < answer:
        guess = int(input("You can enter 0 to quit the game! \nPls guess higher: "))
        tries = tries + 1
        print()

    else: #guess must be greater than the answer
        guess = int(input("You can enter 0 to quit the game! \nPlease guess lower: "))
        tries = tries + 1
        print()



if tries == 1 and guess == answer:
    print("You got it from the first try!")
elif guess == 0:
    print("You closed the game")
else:
    print("Congrats! You got it! It took you {} tries to guess it!".format(tries))


