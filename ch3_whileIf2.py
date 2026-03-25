password = "Hello123"

i = 3

while i > 0:
    attempt = input("enter a password")

    if attempt == password:
        print("access granted")
        break
    elif attempt != password and i != 0:
        print("Try again")
    
    i-=1
    if i == 0:
        print("access denied")