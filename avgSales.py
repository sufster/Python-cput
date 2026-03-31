import matplotlib.pyplot as plt
from datetime import datetime

lis = []
prodLis = []

SENTINEL = "exit"

userSent = input("Would you like to proceed: ")

while userSent != SENTINEL:
    userInp = input("Would you like to add an amount or product: ").lower()

    if userInp == "amount":
        userAmount = float(input("enter an ammount: "))
        lis.append(userAmount)
        print("products: ", len(prodLis))
        print("products: ", len(lis))
    
    elif userInp == "product":
        userProd = input("Enter a product: ")
        print("products: ", len(prodLis))
        print("sales: ", len(lis))
        prodLis.append(userProd)
    
    else:
        print("Please come again")
        break

plt.plot(prodLis, lis, color='red', marker='*')
plt.bar(prodLis, lis)
plt.title(f"Sales for {datetime.now().strftime("%B %Y")}")
plt.show()
