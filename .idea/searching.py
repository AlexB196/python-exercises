shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
found_at = None
#None is a constat to show that a variable has to value

#Mai jos este o secventa pt item_to_find = "spam"
# for index in range(len(shopping_list)): #from 0 to lenght - lenght is 6 in this case as we have 6 items
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break #as soon as the value is found, we end the program
#
# print("Item found at position: {0}".format(found_at))

#Aici avem pt cazul in care item_to_find nu se afla in lista
# for index in range(len(shopping_list)): #from 0 to lenght - lenght is 6 in this case as we have 6 items
#      if shopping_list[index] == item_to_find:
#         found_at = index
#         break #as soon as the value is found, we end the program

#Python is a complex language. We can write the for we got above in a
#much simple way, because Python has the capability

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)


if found_at is not None:
    print("Item found at position: {}".format(found_at))
else:
    print("{} not found".format(item_to_find))

