for i in range(1,6):
    num = int(input("enter a number: "))
    if num%2 == 0:
        print(num, " is even")
    else:
        print(num, " is odd")

print("-"*30)
#--------------------------------------------------------

result = 0
for i in range(6):
    pos_neg = int(input("Enter a number"))
    if pos_neg > 0:
        result+=pos_neg

    else:
        print("Not positive")

print(result)

print("-"*30)
#--------------------------------------------------------

ls = []

for i in range(1,8):
    sm_lg = int(input("Enter a number: "))
    ls.append(sm_lg)

print("The largest number is ", max(ls))

print("-"*30)
#--------------------------------------------------------

n = int(input("How many times would you like to check the number"))

for i in range(n):
    userInp = int(input("Enter a number: "))
    if userInp%3 and userInp%5 == 0:
        print("Jumpy Joy")
    elif userInp%3 == 0:
        print("Jumpy")
    elif userInp%5 ==0:
        print("Joy")
    else:
        print(userInp)