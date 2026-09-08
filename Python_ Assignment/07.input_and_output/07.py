# # 7. Name, city and college
# name = input("7. Enter name: ")
# city = input("Enter city: ")
# college = input("Enter college: ")

# print(name)
# print(city)
# print(college)
# Marks=90
# if Marks>=90:
#     print("A")
# elif Marks>=60:
#     print("B")
# else:
#     print("Fail")


operator = input("Enter operator (+, -, *, /): ")
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
if operator == "+":
    print(number1+number2)
if operator == "-":
    print(number1-number2)
if operator == "*":
    print(number1*number2)
if operator == "/":
    print(number1/number2)
else:
    print("Invalid operator")                