# myList = ["a", "b", "c", "d"]
#
# newString = ", ".join(myList)
#
# print(newString)

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = [{"Q": 0},
        {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
        {"N": 5, "Q": 0},
        {"W": 1, "Q": 0},
        {"N": 1, "W": 2, "Q": 0},
        {"W": 2, "S": 1, "Q": 0}]

#we can convert exsts into a list like this
# exits = { 0: {"Q": 0},
#           1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#           2: {"N": 5, "Q": 0},
#           3: {"W": 1, "Q": 0},
#           4: {"N": 1, "W": 2, "Q": 0},
#           5: {"W": 2, "S": 1, "Q": 0} }



loc = 1

while True:
    availableExists = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exists are " + availableExists).upper()
    print()

    if direction in exits[loc]:
        loc = exits[loc][direction]

    else:
        print("You cannot go in that direction")