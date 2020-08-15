#create a list of items (strings or numbers)
#then create an iterator using the iter() function.
#
#Use a for loop to loop "n" times, where n is the number of items in your list
#Each time round the loop, use the next() on your list to print the next text

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

the_iterator = iter(list) # asta imi creaza iteratorul. atat!

for i in range(len(list)):
    print(next(the_iterator))