sent = input("Enter a sentence: ")

word = sent.split()

counter = 0

for i in word:
    counter+=len(i)

avg = counter / len(word)

print(f"The average length is: {avg}")