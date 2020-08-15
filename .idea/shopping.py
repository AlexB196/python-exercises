shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
#list is created with square brackets

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

#CONTINUE! - mai jos
# for item in shopping_list:
#     if item == "spam": #cand gaseste "spam", il sare si trece la urmatorul item
#         continue #cand ajunge sa fie executed, tot ce este in loop va fi ignorat
#     print("Buy " + item)


#BREAK - mai jos
for item in shopping_list:
    if item == "spam":
        break #cand ajunge sa fie executat, loop-ul se termina
    print("Buy " + item)