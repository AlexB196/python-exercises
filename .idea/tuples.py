# t = ("a", "b", "C") #it can be without parantheses, but it is recommended to put them
#
# print(t)
#
# print("a", "b", "c")
# print(("a", "b", "c"))

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

#metallica[0] = "Master of puppets" #this will return error

imelda = imelda[0], "Imelda May", imelda[2] #we created a new tuple, which replaced the first tuple
print(imelda)

metallica2 = ["Ride the lightning", "Metallica", 1984]
print(metallica2)

metallica2[0] = "Master of puppets"
print(metallica2)

#mai sus vedem ca ne putem juca cu elementele

title, artist, year = imelda #it process the data from the right
#this is called tuple unpacking
print(title)
print(artist)
print(year)