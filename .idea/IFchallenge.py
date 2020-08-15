name = input("Please enter your name: ")

age = int(input("Please enter your age too: "))

if age >= 18 and age < 31:
    print("Perfect! You are in the age range for the trip, {0}!"
          .format(name))
else:
    print("I am sorry! You are not in the age range for this!")


