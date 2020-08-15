name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

#if age >= 18:
#    print("You are old enough to vote!")
#    print("Please put an X in the box")
#else:
#    print("Please go back home! You can vote in {0} years.".format(18 - age))


if age < 18:
    #IMPORTANT! IF is testing "something"
    #usually when you see an IF, you think about
    #testing if that "something" is true or not - 1 or 0
    #this is how you need to view the IF statement
    print("You are not old enough to vote! Please come back in {0} years."
          .format(18 - age))

elif age == 500: #elif se foloseste mereu inaintea lui else
    #else reprezinta mereu ultima chestie "ramasa"
    #ultima chestie atunci cand nu mai ai nimic de verificat
    print("TOO OLD!")

else:
    print("You have the right no vote now! Enjoy!")



print()
