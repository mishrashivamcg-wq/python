# i=2
# while i<=20:
#     print(i)
#     i+=2

# # task 1
# i=1
# while i <=5:
#     print("Hello")
#     i+=1

# # task 2
# i=0
# while i <10:
#     print(i,end=" ")
#     i+=1

# # task 3
# i=1
# while i<=10:
#     print(i)
#     i+=1

# # task 4
# i=10
# while i>=1:
#     print(i)
#     i-=1

# # task 5
# i=5
# while i <=50:
#     print(i)
#     i+=5

# # task 6
# i=1
# while i <=10:
#         print(i*2)
#         i+=1

# # task 7
# i=0
# while i<10:
#     print(i*2+1)
#     i+=1

# # task 8
# i=1
# while i <=6:
#     print(i*3)
#     i+=1

# # task 9 
# i=20
# while i >1:
#     print(i)
#     i-=2

# # task 10
# a=int(input("Enter a number : "))
# i=0
# while i<a:
#     i+=1
#     print(i)

# # task 11
# a=int(input("Enter a number : "))
# i=0
# while i<=a:
#     print(i*2)
#     i+=1

# # task 12
# a=int(input("Enter a number : "))
# i=0
# while i<=a:
#     print(i*2+1)
#     i+=1

# # task 13
# a=int(input("Enter a number : "))
# i=1
# while i<=a:
#         print(i*3)
#         i+=1


# while True:
#     s = input("Enter a string: ")
#     i = 0
#     j = len(s) - 1
#     flag = True

#     while i < j:
#         if s[i] == s[j]:
#             i += 1
#             j -= 1
#             print("Palindrome")
#             break
#         else:
#             flag = False
#             print("Not a palindrome")
#             break
#     if flag == True:
#         break


# number = 472

# while number > 0:
#     digit = number % 10
#     print(digit)
#     number = number // 10


# number = 47.25
# while number != int(number):
#     number = round(number * 10, 10)
# number = int(number)
# if number == 0:
#     print("0")
# else:
#     while number > 0:
#         digit = number % 10
#         print(digit)
#         number = number // 10



# row = 1

# while row <= 3:
#     column = 1

#     while column <= 4:
#         print("*", end="")
#         column = column + 1

#     print()
#     row = row + 1



# row = 1

# while row <= 4:
#     column = 1

#     while column <= row:
#         print(column, end="")
#         column = column + 1

#     print()
#     row = row + 1




s = input("Enter a string: ")

result = ""

for ch in s:
    if not ch.isdigit():
        result += ch

print(result)
