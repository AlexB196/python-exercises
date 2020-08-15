string ="1234567890"

# for char in string:
#     print(char)

# my_iterator = iter(string) - this only creates the iterator
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
#
# print(next(my_iterator))

#I can see when I run the code that it returns an error
#which is normal because there are no more elements
#This is exactly what happens in a "for" behind the scenes
#FOR uses next till there are no elements and an error is returned


###########

for char in string:
     print(char)
#ambele faca acelasi lucru - cea de jos actioneaza dupa modelul de sus
for char in iter(string):
    print(char)