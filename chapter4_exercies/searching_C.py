userInput = input("Enter a string: ")

query = input("Enter a query string: ")

for i in userInput:
    if query == i:
        print(f"{query} exists within {userInput} and appears {userInput.count(query)} times")
        break
    else:
        print(f"{query} does not exist within {userInput} and appears {userInput.count(query)} times")
        break