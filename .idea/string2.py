parrot = "Norwegian Blue"

print(parrot)

#numaratoarea in string incepe de la 0
print(parrot[3])
print(parrot[4])
print() #aici pot sa folosesc si [5] care este spatiul liber
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

#daca folosesc nr negative, citesc invesr - cand citesc invesr, incepe de la -1

print(parrot[-1])
print(parrot[-14])

print()

print(parrot[-11])
print(parrot[-10])
print()
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])
print()


#slicing
#IMPORTANT! [0:6] - slicing-ul incepede de la pozitia 0
#se termina la pozitia 6, dar nu include pozitia 6

print(parrot[0:6]) #imi printeaza Norweg
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])
print()
print(parrot[:6] + parrot[6:])
print(parrot[:])

#negative slicing
print(parrot[-4:-2]) #rezultat: Bl
print(parrot[-4:12]) #rezultat: Bl

#slicing backwards
print(parrot[14:0:-1]) #am nevoie de -1 ca sa imi afiseze descrescator
#daca scot 0, o sa imi afiseze si N de la inceput. deoarece nu mai
#are pozitia de oprire