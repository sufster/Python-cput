price = 50

try:
    quest = int(input("Enter the amount of items you would like to buy, each item is R50: "))
    if quest > 1 and quest < 5:
        print(f"You bought {quest} items at R{price*quest}")
    elif quest == 5 and quest < 10:
        print(f"You bought {quest} items at R{price*quest}")
    elif quest < 0:
        print("Enter a number greater than 0")
    else:
        print(f"You bought {quest} items at R{price*quest}")
except ValueError:
    print("Please enter a valid integer")