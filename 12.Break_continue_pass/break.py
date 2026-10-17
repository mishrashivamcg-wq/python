#question1
# for i in range(1, 8):
#     if i == 5:
#         break
#     print(i)
# print("Finished")
# # 1
# # 2
# # 3
# # 4
# # Finished

# # question2
# word = "skyline"

# for ch in word:
#     if ch in "aeiou":
#         break
#     print(ch)
# # s
# # k
# # y
# # l

# #question3
# n = 2

# while n <= 10:
#     print(n)
#     if n == 6:
#         break
#     n += 2
# # 2
# # 4
# # 6

# #question4
# limit = int(input("Enter limit: "))

# for i in range(1, limit + 1):
#     if i == 7:
#         break
#     print(i, end=" ")
# #1 2 3 4 5 6

# # question5
# word = input("Enter string: ")
# target = input("Enter target character: ")

# for ch in word:
#     print(ch, end=" ")
#     if ch == target:
#         break

# #c om p

# #question6
# numbers = list(map(int, input().split()))

# for n in numbers:
#     if n < 0:
#         break
#     print(n, end=" ")
# # 4 8 n2 

# for row in range(1, 4):
#     for col in range(1, 5):
#         if col == 3:
#             break
#         print(row, col)

# #1 1   1 2  2 1   2 2   3 1  3 2

# #questyion7
# sentence = input().split()
# target = input()

# for word in sentence:
#     if word == target:
#         print("Found")
#         break
# else:
#     print("Not found")


# #question9
# for i in range(1, 7):
#     if i == 4:
#         continue
#     print(i)
# # 1 2 3 5 6 




# #question10
# for ch in "education":
#     if ch in "aeiou":
#         continue
#     print(ch, end="")
# # dctn

# #question11
# n = 0

# while n < 5:
#     n += 1
#     if n == 3:
#         continue
#     print(n)
# #1245

# #question12
# n = int(input())

# for i in range(1, n + 1):
#     if i % 3 == 0:
#         continue
#     print(i, end=" ")
# # 1 2 4 5 7 8

# #question13
# word = input()
# target = input()

# for ch in word:
#     if ch == target:
#         continue
#     print(ch, end="")
# # miippi

# #question15
# for i in range(1, 5):
#     if i == 2:
#         continue
#     print("A", i)
#     print("B", i)

# # A 1 B 1 A 3 B 3 A 4 B 4

# #question16
# n = 0

# while n < 5:
#     n += 1
#     if n == 3:
#         continue
#     print(n)
# #1 2 3 4 5 

# #question17
# word = input()
# count = 0

# for ch in word:
#     if ch in "aeiou":
#         continue
#     count += 1

# print(count)


# #question18
# for i in range(1, 4):
#     print(i)
# else:
#     print("Done")

# #question19
# for i in range(1, 5):
#     if i == 2:
#         continue
#     print(i)
# else:
#     print("Completed")
# #1 3 4 complete

# #question20
# for i in range(1, 5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("Completed")

# print("Outside loop")
# #1 2 outside

# #question21
# for item in []:
#     print("Inside")
# else:
#     print("Else block")
# #Else block

# #question22
# numbers = list(map(int, input().split()))
# target = int(input())

# for n in numbers:
#     if n == target:
#         print("Found")
#         break
# else:
#     print("Not found")

# #question23
# text = input("Enter a string: ")
# target = input("Enter target character: ")

# for char in text:
#     if char == target:
#         print("Character exists")
#         break
# else:
#     print("Character missing")

# #question24
# n = int(input("Enter a number: "))

# for i in range(2, n):
#     if n % i == 0:
#         print("Not prime")
#         break
# else:
#     print("Prime")

# #question25
# values = [2, 4, 6, 8]

# for value in values:
#     if value % 2 != 0:
#         print("Odd found")
#         break
# else:
#     print("All are even")

# # question26
# case 1
# for x in range(3):
#     continue
# else:
#     print("A")
# case2
# for x in range(3):
#     break
# else:
#     print("B")
# case3
# for x in range(0):
#     print(x)
# else:
#     print("C")


# # question27
# text = input("Enter a string: ")

# for char in text:
#     if text.count(char) >= 2:
#         print(char)
#         break
# else:
#     print("No repeated character")


# # question28
# for i in range(1, 4):
#     if i == 2:
#         pass
#     print(i)

# #question29
# x = 10

# if x > 5:
#     pass

# print("Finished")

# # question30
# for letter in "cat":
#     pass

# print("Loop ended")

# # question31
# for i in range(1, 6):
#     if i % 2 == 0:
#         pass
#     print(i)

# # question32
# choice = int(input("Enter your choice: "))

# if choice == 1:
#     print("Option 1 selected")
# elif choice == 2:
#     pass
# else:
#     print("Invalid choice")

# print("Program closed")

# # question33
# case A
# for i in range(1, 5):
#     if i == 3:
#         pass
#     print(i)
# case B
# for i in range(1, 5):
#     if i == 3:
#         continue
#     print(i)
# question34
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

# #question35
# for i in range(1, 6):
#     if i == 2:
#         continue
#     if i == 4:
#         break
#     print(i)
# else:
#     print("Finished")

# # question36
# numbers = input("Enter numbers: ").split()
# target = int(input("Enter target: "))

# for i in numbers:
#     num = int(i)
#     if num < 0:
#         continue

#     if num == target:
#         print("Target found")
#         break

# else:
#     print("Target not found")

# # question37
# numbers = input("Enter numbers: ").split()

# for i in numbers:
#     num = int(i)
#     if num == 0:
#         continue
#     if num == -1:
#         break
#     print(num)
# else:
#     print("All values processed")

# #question38
# for row in range(1, 4):
#     for column in range(1, 4):
#         if column == 2:
#             continue
#         if row == 3:
#             break
#         print(row, column)
#     else:
#         print("inner loop completed")

# # question39
# numbers = input("Enter numbers: ").split()

# for i in numbers:
#     numbers = int(i)

#     if numbers < 0:
#         continue

#     if numbers % 4 == 0 and numbers % 6 == 0:
#         print("Found:", numbers)
#         break
# else:
#     print("No matching number")