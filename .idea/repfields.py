age = 23
print("My age is {0} years" .format(age))

print("My age is " + str(age) + " yeras") #acelasi lucru cu ce este mai sus
print()

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
#se poate scrie si in continuare, dar daca e linia prea mare
#preferabil sa se scrie asa
print()

print("Jan: {2}, Feb: {0}, Mar: {1}".format(28, 30, 31))
print()
print()
print()

print("""Jan: {2}
Feb: {0}
Mar: {1}""".format(28, 30, 31)) #we use triple quotes to write on different lines 
