#hourly wage variable
hourlyW = float(input("Enter an hourly rate: "))

#total hours variable
totHours = float(input("Enter total hours: "))

#overtime variable
totOT = float(input("Enter overtime: "))

#weekly pay
weekPay = hourlyW * totHours + ((hourlyW*1.5)*totOT)

#displays total pay for the week
print("The weekly pay is :" + str(weekPay))