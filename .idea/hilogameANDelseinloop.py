#in the program I am thinking about a number and the program needs to guess it
#the program uses binary search to find what I am thinking about
#this is the best/fastest way to find a number in an order list

low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Please ENTER to start")

guesses = 1

while low != high: #puteam scrie guess!=answer, dar nu stim in cazul asta care este answer
    #print("\tGuessing the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2 #formula pt binary search
    high_low = input("My guess is {}. Should I guess high or lower? "
                    "Enter h or l, or c if my guess was correct "
                     .format(guess)).casefold()

    if high_low == "h":
        #guess higher. The low end of the range becomes 1 greater than the guess
        low = guess + 1

    elif high_low == "l":
        #guess lower. The high end of the range becomes 1 less than the guess
        high = guess - 1

    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break

    else:
        print("Please enter h, l or c")

    #guesses = guesses + 1

    guesses += 1 # same as above, but it works a little different. This is more efficient


else: #in caz ca nu o sa atinga niciodata break, adica low sa nu fie egal cu high, decat la sfarsit de tot
     print("You thought of the number {}".format(low))
     print("I got it in {} guesses".format(guesses))