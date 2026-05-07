userInput = input("enter a sentence: ")
startInp = int(input("Enter the start: "))
endInp = int(input("Enter the end: "))

for i in range(startInp, endInp):
    print(f"Substring: {userInput[startInp:endInp]}")
    break