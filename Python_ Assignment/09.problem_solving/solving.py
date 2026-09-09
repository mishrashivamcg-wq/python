# Q1
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Q2
num = int(input("Enter a number: "))
if num == 0:
    print("Zero")
elif num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    if num % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")


# Q3
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest =", a)
elif b > a:
    print("Largest =", b)
else:
    print("Both are equal")


# Q4
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a <= b and a <= c:
    print("Smallest =", a)
elif b <= a and b <= c:
    print("Smallest =", b)
else:
    print("Smallest =", c)


# Q5
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)


# Q6
num = int(input("Enter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
elif num % 5 == 0:
    print("Divisible by 5 only")
elif num % 11 == 0:
    print("Divisible by 11 only")
else:
    print("Not divisible by 5 or 11")


# Q7
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 7 == 0:
    print("Divisible by both 3 and 7")
elif num % 3 == 0:
    print("Divisible by 3")
elif num % 7 == 0:
    print("Divisible by 7")
else:
    print("Not divisible by 3 or 7")


# Q8
marks = int(input("Enter marks: "))
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")


# Q9
marks = int(input("Enter marks: "))
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 40:
    print("Grade E")
else:
    print("Fail")


# Q10
age = int(input("Enter age: "))
if age < 0:
    print("Invalid age")
elif age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# Q11
year = int(input("Enter year: "))
if year % 400 == 0:
    print("Leap Year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap Year")
else:
    print("Not a Leap Year")


# Q12
ch = input("Enter a character: ")
if ch >= 'A' and ch <= 'Z':
    print("Uppercase")
elif ch >= 'a' and ch <= 'z':
    print("Lowercase")
elif ch >= '0' and ch <= '9':
    print("Digit")
else:
    print("Special Character")


# Q13
ch = input("Enter a character: ")
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
    print("Vowel")
elif (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
    print("Consonant")
else:
    print("Invalid character")


# Q14
cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))
if sp > cp:
    print("Profit =", sp - cp)
elif cp > sp:
    print("Loss =", cp - sp)
else:
    print("No Profit No Loss")


# Q15
cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))
if cp <= 0:
    print("Invalid Cost Price")
elif sp > cp:
    profit = sp - cp
    percentage = (profit / cp) * 100
    print("Profit =", profit)
    print("Profit Percentage =", percentage)
elif cp > sp:
    loss = cp - sp
    percentage = (loss / cp) * 100
    print("Loss =", loss)
    print("Loss Percentage =", percentage)
else:
    print("No Profit No Loss")


# Q16
units = int(input("Enter units: "))
if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 5
    print("Bill =", bill)
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
    print("Bill =", bill)
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10
    print("Bill =", bill)


# Q17
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator: ")
if op == '+':
    print("Answer =", a + b)
elif op == '-':
    print("Answer =", a - b)
elif op == '*':
    print("Answer =", a * b)
elif op == '/':
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("Answer =", a / b)
else:
    print("Invalid operator")


# Q18
temp = float(input("Enter temperature: "))
if temp < 0:
    print("Freezing")
elif temp <= 15:
    print("Very Cold")
elif temp <= 25:
    print("Cold")
elif temp <= 35:
    print("Normal")
else:
    print("Hot")


# Q19
num = int(input("Enter a number: "))
if num < 0:
    print("Negative")
elif num <= 10:
    print("Between 0 and 10")
elif num <= 50:
    print("Between 11 and 50")
elif num <= 100:
    print("Between 51 and 100")
else:
    print("Above 100")


# Q20
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))
if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
else:
    print("Invalid Triangle")


# Q21
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))
if a <= 0 or b <= 0 or c <= 0:
    print("Invalid Triangle")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Invalid Triangle")
elif a == b and b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")


# Q22
balance = float(input("Enter balance: "))
withdraw = float(input("Enter withdrawal amount: "))
if withdraw <= 0:
    print("Invalid withdrawal amount")
elif withdraw % 100 != 0:
    print("Amount must be divisible by 100")
elif withdraw > balance:
    print("Insufficient balance")
elif balance - withdraw < 500:
    print("Minimum ₹500 must remain")
else:
    balance = balance - withdraw
    print("Withdrawal Successful")
    print("Remaining Balance =", balance)


# Q23
username = input("Enter username: ")
password = input("Enter password: ")
if username != "admin":
    print("User not found")
elif password != "python123":
    print("Wrong password")
else:
    print("Login successful")


# Q24
amount = float(input("Enter purchase amount: "))
if amount < 0:
    print("Invalid amount")
elif amount < 500:
    discount_percent = 0
elif amount < 1000:
    discount_percent = 5
elif amount < 2000:
    discount_percent = 10
elif amount < 5000:
    discount_percent = 15
else:
    discount_percent = 20

if amount >= 0:
    discount = amount * discount_percent / 100
    final_amount = amount - discount
    print("Discount =", discount)
    print("Final Amount =", final_amount)


# Q25
m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))

if m1 < 0 or m1 > 100 or m2 < 0 or m2 > 100 or m3 < 0 or m3 > 100:
    print("Invalid marks")
elif m1 < 35 or m2 < 35 or m3 < 35:
    print("Fail")
else:
    average = (m1 + m2 + m3) / 3
    print("Average =", average)

    if average >= 75:
        print("Distinction")
    elif average >= 60:
        print("First Class")
    elif average >= 50:
        print("Second Class")
    else:
        print("Pass")


# Q26
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if year <= 0:
    print("Invalid Date")
elif month < 1 or month > 12:
    print("Invalid Date")
else:
    if month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            max_days = 29
        else:
            max_days = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        max_days = 30
    else:
        max_days = 31

    if day >= 1 and day <= max_days:
        print("Valid Date")
    else:
        print("Invalid Date")


# Q27
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

if hours >= 0 and hours <= 23 and minutes >= 0 and minutes <= 59 and seconds >= 0 and seconds <= 59:
    print("Valid Time")
else:
    print("Invalid Time")


# Q28
name1 = input("Enter name 1: ")
age1 = int(input("Enter age 1: "))
name2 = input("Enter name 2: ")
age2 = int(input("Enter age 2: "))
name3 = input("Enter name 3: ")
age3 = int(input("Enter age 3: "))

if age1 < age2 and age1 < age3:
    print(name1, "is the youngest")
elif age2 < age1 and age2 < age3:
    print(name2, "is the youngest")
elif age3 < age1 and age3 < age2:
    print(name3, "is the youngest")
elif age1 == age2 and age2 == age3:
    print("All have the same age")
elif age1 == age2:
    print(name1, "and", name2, "are youngest")
elif age1 == age3:
    print(name1, "and", name3, "are youngest")
else:
    print(name2, "and", name3, "are youngest")


# Q29
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a > b and a < c) or (a < b and a > c):
    print("Second Largest =", a)
elif (b > a and b < c) or (b < a and b > c):
    print("Second Largest =", b)
else:
    print("Second Largest =", c)


# Q30
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance: "))
income = float(input("Enter family income: "))

if age >= 18 and age <= 25 and marks >= 85 and attendance >= 75 and income <= 300000:
    print("Scholarship Approved")
else:
    print("Scholarship Rejected")