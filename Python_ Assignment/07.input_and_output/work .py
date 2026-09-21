# Name=input("Enter a string: ").strip().lower()
# length=len(Name)
# sum=""
# for i in range(length-1,-1,-1):
#     sum=sum+Name[i]
# if Name==sum:
#     print("The string is a palindrome")
# else:
#     print("The string is not a palindrome")




# name = "racecar"
# for character in name:
#     print(character) 




# count = 0
# for character in name:
#     if evennumb == "a":
#         count += 1   





# for row in range(4):
#     print('#',end="")
#     for column in range(4):
#         print("*", end="")
#     print()


# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()



# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()

# for i in range (1,6):
#   print (" "* (5-i)+ "*"*i)


# for i in range (5,0,-1):
#    print (" "* (5-i)+ "*"*i)



# for i in range(5):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(5-i):
#         print("*",end=" ")
#     print()






total=0 
passed=True
grade=""
for i in range(5) :
    marks=int(input("Enter Marks:"))
    total+=marks
    if marks<35:
        passed=False
if passed:
    percentage=total/5
    if percentage>=90:
        grade="A+"
    elif percentage>=85:
        grade="A"
    elif percentage>=80:
        grade="B+"
    elif percentage>=75:
        grade="B"
    elif percentage>=50:
        grade="c"
    else:
        grade="d"
if passed==True:
    print("total marks:",total  )
    print("percentage",percentage)
    print("Grade",grade)
    print("yoy are passed")
else:
    print("you are fail")

    
        

        



