import random

num = int(input("how many choices do you want?  "))
n = num 
choices = []

for j in range(n):
	choice = (input("what is your option?  "))
	choices += [choice]

k = n - 1

i = random.randint(0, k)

choose = choices[i]

print(choose)
