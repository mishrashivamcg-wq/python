# for i in range (0,3):
#     for j in range (0,3):
#         print ("*",end=" ")
#     print()    



# for i in range (1,4):
#     for j in range (1,4):
#         print (j,end=" ")
#     print()  



# for i in range (1,4):
#     for j in range (1,4):
#         print (i,end=" ")
#     print() 




# for i in range (5):
#     for j in range(i+1):
#         print("*", end="")
#     print()   


# for i in range (5):
#     for j in range(5-i):
#         print("*", end="")
#     print()   



# for i in range (1,6):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()   


# for i in range (1,6):
#     for j in range(1,i+1):
#         print(i, end=" ")
#     print()   


# num=int(input("enter table:"))
# for i in range (1,11):
#      print(num*i, end=" ")




# for i in range(1,4):          
#     for j in range(1,6):      
#         print(i * j, end=" ") 
#     print()      



# for i in range(5):          
#     for j in range(1,6):      
#         print( j*j, end=" ") 
#     print()   


# for i in range(5):          
#     for j in range(i+1):      
#         print( j, end=" ") 
#     print()   


# for i in range(5):          
#     for j in range(i+1):      
#         print( i, end=" ") 
#     print()  

# for i in range(0,5):          
#     for j in range(i+1):      
#         print( (j*2+1), end=" ") 
#     print()  


# for i in range(0,5):          
#     for j in range(i+1):      
#         print( (j*2+2), end=" ") 
#     print()                   


# for i in range (5):
#     for j in range (5):
#         print("*",end=" ")
#     print()    


# for i in range (1,6):
#     for j in range (1,6):
#         print(j,end=" ")
#     print()   

# number=1
# for i in range (1,4):
#     for j in range (1,4):
#         print(number,end=" ")
#         number+=1
#     print()    



# for i in range (1,6):
#     for j in range (i-1):
#         print(i,end=" ")
#     print()    









#1
# a=int(input("enter a number:"))
# for i in range (0,a):
#     for j in range (0,a):
#         print ("*",end=" ")
#     print()    


#2

# for i in range (1,4):
#     for j in range (1,4):
#         print (j,end=" ")
#     print()  


#3

# for i in range (1,4):
#     for j in range (1,4):
#         print (i,end=" ")
#     print() 

#4


# for i in range (5):
#     for j in range(i+1):
#         print("*", end="")
#     print()   

#5

# for i in range (5):
#     for j in range(5-i):
#         print("*", end="")
#     print()   

#6

# for i in range (1,6):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()   

#7

# for i in range (1,6):
#     for j in range(1,i+1):
#         print(i, end=" ")
#     print()   

#8

# num=int(input("enter table:"))
# for i in range (1,11):
#      print(num*i, end=" ")


#2nd
# # Outer loop selects the table number (from 1 to 5)
# for outer in range(1, 6):
#     print(f"--- Multiplication Table of {outer} ---")
    
#     for inner in range(1, 11):
#         product = outer * inner
#         print(f"{outer} x {inner} = {product}")
        
#     print()



#9

# for i in range(1,4):          
#     for j in range(1,6):      
#         print(i * j, end=" ") 
#     print()      

#10

# for i in range(5):          
#     for j in range(1,6):      
#         print( j*j, end=" ") 
#     print()  


#11

# letters = "ABCDE"

# for i in range(1, 6):
#     for j in range(i):
#         print(letters[j], end=" ")
#     print()

#12

# letters = "ABCDE"

# for i in range(1, 6):
#     for j in range(i):
#         print(letters[i-1], end=" ")
#     print()

#13

#1st Method

# for i in range(0,5):          
#     for j in range(i+1):      
#         print( (j*2+1), end=" ") 
#     print()  

#2nd method

# n=int(input("enter number : "))
# for i in range(n+1):
#     for j in range(2*i+1):
#         if j%2!=0:
#             print(j,end=" ")
#     print()


#3rd Method
# for i in range(1,6):
#     a=1
#     for j in range(i):
#           print(a,end="")
#           a+=2
#     print()  

#14

# for i in range(0,5):          
#     for j in range(i+1):      
#         print( (j*2+2), end=" ") 
#     print()                   

#15

# for i in range (5):
#     for j in range (5):
#         print("*",end=" ")
#     print()    

#16

# for i in range (1,6):
#     for j in range (1,6):
#         print(j,end=" ")
#     print()   

#17

# number=1
# for i in range (1,4):
#     for j in range (1,4):
#         print(number,end=" ")
#         number+=1
#     print()    

#18

# n=0
# for i in range(4):
#     n+=1
#     for j in range(5*n-4,5*n+1):
#         print(j,end=" ")
#     print()

#19

# for i in range(1,4):
#     for j in range(1,4):
#         print((i,j),end=" ")
#     print()

#20

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)

#21

# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end=" ")
#     print()

#22

# for i in range(1,6):
#     for j in range(i):
#         print(i,end="")
#     print()

#23

# for i in range(1,6):
#     for j in range(1,6-i+1):
#         print(j,end=" ")
#     print()

#24

# for i in range(5):
#     for j in range(5,0+i,-1):
#         print(j,end=" ")
#     print()

#25

# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end=" ")
#     print()


# i=2
# while i <=20:
#     print(i)
#     i=i+2



# i = 0
# while i < 5:
#     print("Hello")
#     i += 1


# i=0
# while i<11:
#     print(i,end=" ")
#     i +=1     

# i=0
# while i<12:
#     print (i,end="")
#     i=+1



# choice = 2

# match choice:
#     case 1:
#         print("Add")
#     case 2:
#         print("Subtract")
#     case 3:
#         print("Multiply")
#     case 4:
#         print("Divide")
#     case _:
#         print("Invalid Choice")



# day = 8

# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case _:
#         print("Invalid Day")



# a = int(input("Enter choice 1: "))
# b = int(input("Enter choice: "))
# while match !=0:

#  choice = input("enter an operation of addition,substraction,multiplication,exit: ")


# match choice:
#     case "addition":
#         print(a+b)
#     case "substraction":
#         print(a-b)
#     case "multiplication":
#         print(a*b)
#     case "exit":
#         print()
#     case _:
#         print("Invalid Choice")




# day=int(input("enter a day:-"))

# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print("Weekday")
#     case 6 | 7:
#         print("Weekend")
#     case _:
#         print("Invalid Day")




# marks = 82

# match marks:
#     case x if x >= 90:
#         print("A")
#     case x if x >= 75:
#         print("B")
#     case x if x >= 60:
#         print("C")
#     case x if x >= 40:
#         print("D")
#     case _:
#         print("Fail")





# account = input("enter which type of LPG commerical/domestic:-")
# choice = 2
# choice=int(input("please enter your choice:-"))

# match account:

#     case "domestic":
#         choice=int(input("please enter your choice:-"))
#         match choice:
#             case 1:
#                 print("Book Refill (Subsidy Applicable)")
#             case 2:
#                 print("Check Subsidy Status")
#             case 3:
#                 print("Change Delivery Address")
#             case _:
#                 print("Invalid Choice for Domestic Account")

#     case "commercial":
#         choice=int(input("please enter your choice:-"))
#         match choice:    
#             case 1:
#                 print("Bulk Order Booking (Non-Subsidised)")
#             case 2:
#                 print("Download Tax Invoice")
#             case _:
#                 print("Invalid Choice for Commercial Account")

#     case _:
#         print("Invalid Account Type")
