#Exercise 5

word = "Hello everyone"

for i in word:
    print(i, " ", end=str(ord(i)) + "; ")

#exercise combining loops, inputs and formating

i = 0
total = 0
while i < 4:
    itemPrice = float(input("\nEnter a price for an item: "))

    total += itemPrice

    i+=1

print(round(total,2))

