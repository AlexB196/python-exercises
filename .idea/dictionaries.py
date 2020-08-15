#this is a dictionary - a way to store info about things
fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit",
         "apple": "round and crunchy"}
#above I got apple twice. but only the last value will be printed
#because it overrides the first value

print(fruit)
print()

# print(fruit["lemon"])
# print()
# fruit["pear"] = "an odd shaped apple" #by this we add an entry to a dictionary
# print(fruit)
#
# fruit["pear"] = "great with tequila" #asa schimb valoarea unui entry
# print(fruit)

# del fruit["lemon"] #this is the command to remove an entry from a dictionary
#
# print(fruit)
#
# fruit.clear() # remove everything from a dictionary

#--------------------------
# key = entries
#values = the decription of the entries
#vbelow we can check if an item is in the dictionary
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description =   fruit.get(dict_key, "We do not have a " + dict_key)  # ce e comentat mai jos mai poate fi scris si asa
#     print(description)
#

    # if dict_key in fruit:
    #     description = fruit.get(dict_key)
    #     print(description)

    # else:
    #     print("We do not have a " + dict_key)
#---------------------------

#create a list from a dictionary and order it

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()

#sau se mai poate scrie sub o singura linie

ordered_keys = sorted(list(fruit.keys()))

for f in ordered_keys:
    print(f + "-" + fruit[f])