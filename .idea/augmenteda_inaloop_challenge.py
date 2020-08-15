number = 10
multiplier = 8
answer = 0

# add your loop after this comment
for i in range(multiplier):
    i = number
    answer += i
    #IMPORTANT! I don't have to use i above. I can simply type answer += number
    #the loop will end when the condidition becomes false, but I dont have to use that i

print(answer)

#in the code above, I want to print the answer which is number * multiplier
#but I want to do this by adding up the number for {multiplier} times - make the sum
#and I also wanna use augmented assignment