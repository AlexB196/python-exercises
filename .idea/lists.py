# ipAddress = input("Please enter an IP address: ")
# print(ipAddress.count("."))

# parrot_list = ["non pinin", "no more", "a stiff", "berefit of life"]
#
# parrot_list.append("A Norwegian Blue")
#
# for state in parrot_list:
#     print("This parrot is " + state)
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = even + odd
# #numbers.sort() #asta imi ia lista deja existenta si o sorteaza
# print(sorted(numbers)) #asta imi creaza o lista noua care este deja sortata

########

#add to the program below so that if it finds a meal without spam
#it prints out each of the ingredients of the meal.
#You wil need to set up the menu as we did in lines 24-31

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

#print(menu)

for meal in menu:
    if not "spam" in meal:
        # print(*meal) #print each element of the list separately
        # print(*meal, sep=',')
        # print(*meal, sep="->")
        #above is a simpler, "advanced" way

        #below is the most intuitive way
        for item in meal:
            print(item)