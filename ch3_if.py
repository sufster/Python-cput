#exercise on if statements 1 to 7

num = int(input("enter a number: "))

ans = num%5

if ans ==1:
    print(str(num)," is not divisible by 5")
else:
    print(str(num)," is divisible by 5")

#--------------------------------------------------------
print("-"*30)

mark = int(input("Enter your mark: "))

if mark >= 90:
    print("distinction")
elif mark >=50:
    print("pass")
else:
    print("fail")

#--------------------------------------------------------
print("-"*30)

age = int(input("Enter your age: "))

if age >= 20:
    print("adult")
elif age > 13 or age ==19:
    print("teen")
else:
    print("child")

print("-"*30)
#--------------------------------------------------------

year = int(input("Enter the year: "))

leap_y = year%4

if leap_y != 0:
    print(year, " is not a leap year")
else:
    print(year, " is a leap year")

print("-"*30)
#--------------------------------------------------------

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 > num2:
    print(num1, " is greater than ", num2)
elif num1 < num2:
    print(num2, " is greater than ", num1)
else:
    print(num1, " and ", num2, " are equal")

print("-"*30)
#--------------------------------------------------------

firstNum = int(input("Enter a number: "))
secNum = int(input("Enter another number: "))
thirdNum = int(input("Enter another number: "))

if firstNum > secNum > thirdNum:
    print(firstNum, " > ", secNum, " > ", thirdNum)
elif secNum > firstNum > thirdNum:
    print(secNum, " > ", firstNum, " > ", thirdNum)
else:
    print(thirdNum, " > ", secNum, " > ", firstNum)

print("-"*30)
#--------------------------------------------------------

password = "1!23%"

attempt = input("enter the password: ")

if attempt == password:
    print("Thats correct")
else:
    print("Try again")