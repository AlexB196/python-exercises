# for i in range(10):
#     print("i is now {}".format(i))

i = 0 #the condition must be initialized first before going to the while
while i < 10: #while checks if the condition is true
    #as soon as the condition is false, the while ends
    #in while avem nevoie sa facem in asa fel incat conditia sa devina falsa
    #altfel loop-ul va rula la nesfarsit pt ca nu ajunge conditia sa fie falsa
    print("i is now {}".format(i))
    i = i + 1