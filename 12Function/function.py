#1
def welcome():
    print("Welcome to Python")

welcome()
welcome()
welcome()


#2
def greet(name):
    print("Hello", name)

greet("Shivam")


#3
def show_number(number):
    print(number)

show_number(10)


#4
def add(a, b):
    return a + b

result = add(10, 20)
print(result)


#5
def square(number):
    return number * number

result = square(5)
print(result)


#6
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

result = is_even(8)
print(result)


#7
def get_full_name(first_name, last_name):
    return first_name + " " + last_name

name = get_full_name("Shivam", "Mishra")
print(name)


#8
def introduce(name, city="Pune"):
    print("My name is", name, "and I live in", city)

introduce("Shivam")
introduce("Rahul", "Delhi")


#9
def subtract(a, b):
    return a - b

result = subtract(10, 5)
print(result)

result = subtract(5, 10)
print(result)


#10
def get_min_max(a, b):
    if a < b:
        return a, b
    else:
        return b, a

small, large = get_min_max(10, 20)
print("Smaller:", small)
print("Larger:", large)


#11
def calculate(a, b):
    total = a + b
    difference = a - b
    product = a * b
    quotient = a / b

    return total, difference, product, quotient

result = calculate(10, 5)
print(result)


#12
def count_digits(number):
    count = len(str(number))
    return count

result = count_digits(12345)
print(result)


#13
def classify_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

result = classify_number(-5)
print(result)


#14
def calculate_total(price, quantity=1):
    return price * quantity

print(calculate_total(100))
print(calculate_total(100, 3))


#15
def create_email(username, domain="example.com"):
    return username + "@" + domain

print(create_email("shivam"))
print(create_email("rahul", "gmail.com"))


#16
def format_name(first, last, uppercase=False):
    name = first + " " + last

    if uppercase:
        return name.upper()
    else:
        return name

print(format_name("Shivam", "Mishra"))
print(format_name("Shivam", "Mishra", True))


#17
def percentage(marks, total=100):
    return (marks / total) * 100

result = percentage(80)
print(result)


#18
def convert_minutes(minutes, seconds_per_minute=60):
    return minutes * seconds_per_minute

result = convert_minutes(5)
print(result)


#19
def student_details(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

student_details(city="Gurugram", name="Shivam", age=18)


#20
def bill(item, quantity=1, price=100):
    total = quantity * price
    return total

print(bill("Pen"))
print(bill("Book", 2, 50))
print(bill(item="Bag", quantity=3, price=200))