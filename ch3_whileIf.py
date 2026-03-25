while True:
    userInput = int(input("Enter a number: s"))
    
    if userInput % 2 and userInput == 0:
        print("even")
    elif userInput %2 == 1:
        print("odd")
    
    if userInput == 0:
        break
print("Goodbye")