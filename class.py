
# for i in range(1, 21):
#     if i % 2 == 0:
#         continue
#     print(i)



# numbers = [10, -2, 30, -5, 40, -8]

# for num in numbers:
#     if num <= 0:
#         continue
#     print(num)




# for i in range(1, 21):
#     if i % 3 == 0:
#         continue
#     print(i)





# numbers = [5, 12, 8, 21, 30, 7]

# for num in numbers:
#     if num <= 10:
#         continue
#     print(num)




# num = int(input("Enter a number: "))

# if num > 0:
#     pass
# else:
#     print("Number is not positive")


# for i in range(1, 6):
#     if i == 3:
#         break

#     print(i)


# for i in range(1, 6):
#     if i == 3:
#         continue

#     print(i)


# for i in range(1, 6):
#     if i == 3:
#         pass

#     print(i)


# i = 1

# while i <= 5:
#     if i == 3:
#         continue

#     print(i)
#     i += 1


# for i in range(1, 5):
#     if i == 2:
#         pass
#     elif i == 3:
#         continue
#     elif i == 4:
#         break

#     print(i)



# for i in range(1, 6):
#     if i == 3:
#         break
# else:
#     print("Done")



# while True:
#     number=int(input("Enter number:-"))
#     if number==0:
#         break
#     if number<0:
#         continue
#     print(number)



# found = False

# for i in range(3):
#     for j in range(3):
#         if i == 1 and j == 1:
#             found = True
#             break

#     if found:
#         break



# i = 1

# while i <= 5:
#     if i == 3:
#         continue

#     print(i)
#     i += 1










# for i in range(1, 5):
#     if i == 2:
#         pass
#     elif i == 3:
#         continue
#     elif i == 4:
#         break

#     print(i)



#challenge Problem


# while True:
#     num = int(input("Enter a number: "))

#     if num == 0:
#         break

#     if num < 0:
#         continue

#     print(num)






# numbers = [12, 5, -4, 18, 0, 25, 30]

# for num in numbers:
#     if num < 0:
#         continue

#     if num == 0:
#         break

#     print(num)





# numbers = [10, 20, 30, 40, 50]

# a = int(input("Enter number to search: "))

# for num in numbers:
#     if num == a:
#         print("Number found")
#         break
# else:
#     print("Number not found")




# for i in range(1, 5):
#     if i == 2:
#         pass
#     elif i == 3:
#         continue
#     elif i == 4:
#         break
#     print(i)
# else:
#     print("Completed")
# print("Outside")




# i = 1

# while i <= 10:
#     if i % 2 != 0:
#         print(i)

#     i += 1



 


# for i in range (1,6):
#     for j in range (5,i-1,-1):
#         print(j,end=" ") 
#     print() 
# 


# def add_numbers(a, b):
#     return a + b


# result = add_numbers(5, 3)
# print(f"The sum is: {result}")




# def addition():
#     a=5
#     b=7
#     print(a+b)
# addition()



# def add():
#     print(10 + 20)

# add()
    


# def addition(a, b):
#     print("Addition:", a + b)

# def subtraction(a, b):
#     print("Subtraction:", a - b)

# def multiplication(a, b):
#     print("Multiplication:", a * b)

# def floor_division(a, b):
#     print("Floor Division:", a // b)



# addition(10, 3)
# subtraction(10, 3)
# multiplication(10, 3)
# floor_division(10, 3)






# def check_even(number):
#     if number % 2 == 0:
#         print(number, "is Even")
#     else:
#         print(number, "is Odd")



# check_even(10)
# check_even(7)









# for a in range (1,100):
#     num=a
#     shivam =""
#     while num>0:
#         rem =num%2
#         shivam=str(rem) + shivam
#         num = num//2
#     print(shivam)    




# num=int(input("enter a number:-"))
# a=""
# while num>0:
#     mishra=num%2
#     num=num//2
#     a=str(mishra)+a
# print(a)    


# num=int(input("enter a number:-"))
# # a=""
# while num>0:
#     mishra=""
#     mishra=num%2
#     num=num//2
#     print(mishra[:-1],end="")
    







# num = int(input("enter a number : "))
# mishra = ""  

# while num > 0:
#     remainder = num % 2
#     mishra = str(remainder) + mishra  
#     num = num // 2

# print((mishra))  




# a = "Mishra"
# print(len(a))



# def add(a, b):
#     return a + b

# print(add(5,8 ))



# def introduce(name, age, city):
#     print(name, age, city)

# introduce("Shivam", 18, "Gurugram")



# def add(a, b):
#     print(a + b)

# answer = add(2, 3)
# print(answer)

# def add():
#     print( 5 + 6)

# # answer = add(2, 3)
# # print(answer)
# for i in range(1,9):
#     print(add())





# a = 10
# b = 20
# c = 40

# def add(a, b):
#     c = a + b
#     return c

# def sub(a, b):
#     return a - b

# def mul(a, b):
#     return a * b

# result = mul(sub(a, b), add(b, c))
# # result = mul(sub(add(a,b),c),a)
# print(result)





# Q20. FizzBuzz challenge
# 1 se 50 tak numbers print karo:
# - 3 aur 5 dono se divisible → FizzBuzz
# - Sirf 3 se divisible → Fizz
# - Sirf 5 se divisible → Buzz
# - Otherwise number print karo.


# for i in range(1, 51):
#   if i % 3 == 0 and i % 5 == 0:
#     print("FizzBuzz")
#   elif i % 3 == 0:
#     print("Fizz")
#   elif i % 5 == 0:
#     print("Buzz")
#   else:
#     print(i)



# def multiply(a, b):
#     return a * b

# product = multiply(4, 5)
# print(product)


# def square(n):
#     return n * n

# print(square(3) + square(4))


# def is_even(n):
#     return n % 2 == 0

# if is_even(8):
#     print("Even")
# else:
#     print("Odd")


# def double(n):
#     return n * 2

# def add_five(n):
#     return n + 5

# result = add_five(double(10))
# print(result)


# def calculate(a, b):
#     return a + b, a - b

# answer = calculate(10, 4)
# print(answer)



# def check():
#     print("Before return")
#     return 10
#     print("After return")

# value = check()
# print(value)
 


# def double(number):
#     return number *2
# def add_five(number):
#     return number + 5
# result = add_five(double(10))
# print(result)



# def greet(name):
#     print("Hello", name)

# greet()
# # greet("Shivam")



# def order(item, quantity=1):
#     print(item, quantity)

# order("Pizza")
# order("Burger", 3)

#keyword arguments

# def student(name, age):
#     print(name, age)

# student(age=18, name="Shivam")


def example():
    return 5
    print("Hello")  # Never reached



     
