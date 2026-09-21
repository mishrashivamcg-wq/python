# Problem 1: Sum of Two Numbers

# IPO Model
# ---------
# Input   : Two numbers - num1, num2
# Process : Add num1 and num2
# Output  : The sum of the two numbers
#
# Algorithm
# ---------
# 1. Start
# 2. Read num1
# 3. Read num2
# 4. Compute total = num1 + num2
# 5. Print total
# 6. Stop
 
print("\n--- Problem 1: Sum of Two Numbers ---")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
 
total = num1 + num2
print("The sum is:", total)
 
 

# Problem 2: Even or Odd

# IPO Model
# ---------
# Input   : A number - num
# Process : Check if num % 2 == 0
# Output  : "Even" or "Odd"
#
# Algorithm
# ---------
# 1. Start
# 2. Read num
# 3. If num % 2 == 0, print "Even"
# 4. Else, print "Odd"
# 5. Stop
 
print("\n--- Problem 2: Even or Odd ---")
num = int(input("Enter a number: "))
 
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
 
 
# Problem 3: Largest of Three Numbers

# IPO Model
# ---------
# Input   : Three numbers - a, b, c
# Process : Compare all three to find the greatest
# Output  : The largest of the three numbers
#
# Algorithm
# ---------
# 1. Start
# 2. Read a, b, c
# 3. If a >= b and a >= c, then largest = a
# 4. Else if b >= a and b >= c, then largest = b
# 5. Else, largest = c
# 6. Print largest
# 7. Stop
 
print("\n--- Problem 3: Largest of Three Numbers ---")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
 
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
 
print("The largest number is:", largest)
 
 

# Problem 4: Voting Eligibility

# IPO Model
# ---------
# Input   : Age - age
# Process : Check if age >= 18
# Output  : "Eligible to vote" or "Not eligible to vote"
#
# Algorithm
# ---------
# 1. Start
# 2. Read age
# 3. If age >= 18, print "Eligible to vote"
# 4. Else, print "Not eligible to vote"
# 5. Stop
 
print("\n--- Problem 4: Voting Eligibility ---")
age = int(input("Enter your age: "))
 
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
 
 

# Problem 5: Discount Calculation

# IPO Model
# ---------
# Input   : Price - price
# Process : If price >= 2000, subtract 20% as discount
# Output  : The final price
#
# Algorithm
# ---------
# 1. Start
# 2. Read price
# 3. If price >= 2000: discount = price * 20 / 100, final_price = price - discount
# 4. Else: final_price = price
# 5. Print final_price
# 6. Stop
 
print("\n--- Problem 5: Discount Calculation ---")
price = float(input("Enter the price of the item: "))
 
if price >= 2000:
    discount = price * 20 / 100
    final_price = price - discount
else:
    final_price = price
 
print("The final price is:", final_price)
 
 

# Problem 6: Pass or Fail Based on Average Marks

# IPO Model
# ---------
# Input   : Three marks - m1, m2, m3
# Process : Calculate average, check if average >= 40
# Output  : "Pass" or "Fail"
#
# Algorithm
# ---------
# 1. Start
# 2. Read m1, m2, m3
# 3. Compute average = (m1 + m2 + m3) / 3
# 4. If average >= 40, print "Pass"
# 5. Else, print "Fail"
# 6. Stop
 
print("\n--- Problem 6: Pass or Fail Based on Average Marks ---")
m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
 
average = (m1 + m2 + m3) / 3
 
if average >= 40:
    print("Pass")
else:
    print("Fail")