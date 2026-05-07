userText = input("Enter a word:")

constant = "k"
constantCap ="K"

for i in userText:
    if i == constant or i == constantCap:
        print(f"{userText} contains K")
        break
    else:
        print(f"{userText} does not contain K")
        break