# 1


# ads=input("Enter a string : ")
# uper=0
# lower=0
# digit=0
# space=0
# special=0
# for i in ads:
#     if i.isupper():
#         uper+=1
#     elif i.islower():
#         lower+=1
#     elif i.isdigit():
#         digit+=1
#     elif i.isspace():
#         space+=1
#     else:
#         special+=1

# print(f"Uper case caracter in string is {uper}")
# print(f"lower case caracter in string is {lower}")
# print(f"digit caracter in string is {digit}")
# print(f"spaces caracter in string is {space}")
# print(f"special caracter in stringis {special}")

# 2

# total=0
# flag=True

# for i in rannge(10):
#     marks=int(input("Enter your marks: "))
#     total+=marks
#     if marks<35:
#         flag=False
# percentage=total/5
# if flag:
    
#     if percentage>=75:
#         print("Excellent")
#     elif percentage>=50:
#         print("Good")
#     elif percentage>=35:
#         print("Pass")
#     else:
#         print("Fail")
# else:
#     print("Fail")

# if flag==True:
#     print("You're pass !!")
# else:
#     print("You're fail !!")
 

# 3

# vowel=0
# consonant=0
# digit=0
# Special_character=0
# string=input("Enter any string").lower()
# for i in string:
#     if i == "aeiou":
#         vowel+=2
        
#     elif "a"<=i<="z":
#         consonant+=1
       
#     elif "0"<=i<="9":
#         digit+=3
       
#     else: 
#         Special_character+=4
# total=vowel+consonant+digit+Special_character
# print(total)

# 4

# for i in range(1,6):
#     password=input(f"Enter a password {i} : ")

#     length=False
#     upper=False
#     lower=False
#     digit=False
#     special=False
#     count=0
#     if len(password)>=8:
#         length=True
    
#     for ch in password:
#         if password.isupper():
#             upper=True
#             count+=1
#         elif password.islower():
#             lower=True
#             count+=1
#         elif password.isdigit():
#             digit=True
#             count+=1
#         else:
#             special=True
#             count+=1
    
# if count==5:
#     print("Strong password")
# elif count>=3:
#     print("Mediam password")
# else:
#     print("Weak password")

# 5

# sent=input("Enter a sentence: ")
# length=len(sent)

# if length>=6:
#     print("long")
# elif length>=4:
#     print("Medium")
# else:
#     print("Short")

# 6

# odd=0
# even=0
# for i in range(1,6):
#     num=int(input(f"Enter a number {i} : "))


#     for ch in str(num):
#         if int(num)%2==0:
#             even+=1
#         elif int(num)%2!=0:
#             odd+=1
# print(f"Even number is {even}")
# print(f"Odd number is {odd}")

# if even>odd:
#     print("Last digit is Even")
# elif even<odd:
#     print("Last digit is Odd")
# else:
#     print("Both digit are equal")

# 7 dought

# Str=input("Enter a string: ")
# x=0
# for char in Str:
#     count=0
#     y=0
#     for j in Str:
#         if(char==j ):
#             if(y<x):
#                 break
#             else:
#                 count+=1
#         y+=1
#     if(count>4):
#         print(char)
#         print("Highly repetated")
#     elif(count>2):
#         print(char)
#         print("Repeated")
#     elif(count==2):
#         print(char)
#         print("Duplicate")
#     x+=1

# 8

# total=0

# Budget=0
# regular=0
# Premium=0
# Luxury=0

# for i in range(1,9):
#     price=float(input(f"Enter a price {i} :"))
#     total+=price
#     if price<500:
#         print("Budget")
#         Budget+=1
#     elif 500<=price<1999:
#         print("Regular")
#         regular+=1
#     elif 1999<=price<4999:
#         print("Premium")
#         Premium+=1
#     else:
#         print("Luxury")
#         Luxury+=1  

# Average=total/8
# print(f"Budget is {Budget}") 
# print(f"Regular is {regular}") 
# print(f"Premiun is {Premium}") 
# print(f"Luxury is {Luxury}") 
# print(f" Average amount is {Average}")

#9

# string=input("enter the string of your choices :")
# vowels=0
# consonant=0
# digit=0
# special=0

# for i in range(len(string)):
#     ch=string[i]

#     if i%2==0:
#         position_type="Even" 
#     else:
#         position_type="Odd"

#     if ch.lower() in "aeiou":
#         char_type="Vowel"
#         vowels+=1

#     elif ch.isalpha():
#         char_type="consonant" 
#         consonant+=1

#     elif ch.isdigit():
#         char_type="digit"
#         digit+=1 

#     else:
#         char_type="special"
#         special+=1

    
# print("\n--- Character Category Count ---")
# print("Vowels:", vowels)
# print("Consonants:", consonant)
# print("Digits:", digit)
# print("Special Characters:", special) # note : space included

#10 Question Error

#11

# for i in range(5):
#     name=input("Enter your Username{i} : ").strip()
#     length=len(name)
#     first_character=name[0] 
#     digit=0
#     underscore=0
#     special=0
#     alp=0
#     for ch in name:   
#         if ch.isdigit():
#             digit+=1
#         elif ch=="_":
#             underscore+=1
#         elif ch.isalpha():
#             alp+=1
#         else:
#             special+=1
#     print(length)
#     print(f"First character of username is {name} first charcher is :-{first_character} ")
#     print("no. of digit in username: ",digit)
#     print("no. of total underscore in username: ",underscore)
#     print("invalid special character :",special)
#     print(f"no. of alphabest is :- {alp}")

#12

# sen=input("Enter a sentence: ").lower()
# vowels=0
# consonants=0
# for ch in sen:
#     if ch=="aeiou":
#         vowels+=1
#     else:
#         consonants+=1
# if vowels>consonants:
#     print("Vowels win")
# elif consonants>vowels:
#     print("Consonants win")
# else:
#     print("Draw")   

#13

# for i in range(5):
#     units=int(input("Enter units number : "))
#     if units<=100:
#         print(f"total : {units*5}")
#     elif units<=200:
#         first_hundred=100*5
#         next100_hundred=(units-100)*7
#         print(f"total: {first_hundred+next100_hundred}")
#     elif units<=400:
#         first_hundred=100*5
#         next100_hundred=(units-100)*7
#         next200_hundred=(units-200)*10
#         print(f"total: {first_hundred+next100_hundred+next200_hundred}")
#     else:
#         first_hundred=100*5
#         next100_hundred=(units-100)*7
#         next200_hundred=(units-200)*10
#         next400_hundred=(units-400)*15
#         print(f"total: {first_hundred+next100_hundred+next200_hundred+next400_hundred}")

#14

# sen=input("Enter a sentence: ").lower()
# vowels=0
# consonants=0
# for ch in sen:
#     if ch=="aeiou":
#         vowels+=1
#     else:
#         consonants+=1
# if vowels>consonants:
#     print("Vowels Heavy")
# elif consonants>vowels:
#     print("Consonants Heavy")
# else:
#     print("Balanced")   

#15 baki


#16

# password=input("Enter a password : ")
# Uppercase=0
# Lowercase=0
# Digits=0
# Special_character=0
# for ch in password:
#     if ch.isupper():
#         Uppercase+=1
#     elif ch.islower():
#         Lowercase+=1
#     elif ch.isdigit():
#         Digits+=1
#     else:
#         Special_character+=1
# print(f"Uppercase letters in Password : {Uppercase}")
# print(f"Lowercase letters in Password : {Lowercase}")
# print(f"Digits in Password : {Digits}")
# print(f"Special character in Password : {Special_character}")

#17

# for i in range(1): /// i make mastake in this code.
#     name=input("Enter your Name : ")
#     length=len(name)
#     Uppercase=0
#     Lowercase=0
#     Digits=0
#     Special_character=0
#     total=0
#     vowels=0
#     consonants=0
#     for ch in name:
#         if ch.lower()=="aeiou":
#             vowels+=1
#         else:
#             consonants+=1
        
#     flag=True
#     for j in range(5):
#         mark=int(input(f"Enter your marks {j}: "))
#         total+=mark
#         if mark<35:
#             flag=False
#         percentage=total/5
        
#     if flag:       
#         if percentage>=75:
#             print("Excellent")
#         elif percentage>=50:
#             print("Good")
#         elif percentage>=35:
#             print("Pass")
#         else:
#             print("Fail")
#     else:
#         print("Fail")

#     if flag==True:
#         print("You're pass !!")
#     else:
#         print("You're fail !!")
#         for ch in name:
#             if ch.isupper():
#                 Uppercase+=1
#             elif ch.islower():
#                 Lowercase+=1
#             elif ch.isdigit():
#                 Digits+=1
#             else:
#                 Special_character+=1
#     if vowels>consonants:
#         print("Vowels Heavy")
#     elif consonants>vowels:
#         print("Consonants Heavy")
#     else:
#         print("Balanced")   
# print(f"Given name has {length} charactars")

#17

# highest_marks = -1
# highest_student = ""

# for i in range(5):

#     name = input(f"\nEnter name of student {i + 1}: ")

#     total = 0
#     vowels = 0
#     consonants = 0

#     for ch in name:
#         if ch.lower() in "aeiou":
#             vowels += 1
#         elif ch.isalpha():
#             consonants += 1

   
#     for j in range(5):
#         mark = int(input(f"Enter marks {j + 1}: "))
#         total += mark

#     percentage = total / 5

    
#     if percentage >= 75:
#         grade = "Excellent"
#     elif percentage >= 50:
#         grade = "Good"
#     elif percentage >= 35:
#         grade = "Pass"
#     else:
#         grade = "Fail"

    
#     print("\n----- Student Details -----")
#     print("Name:", name)
#     print("Characters:", len(name))
#     print("Vowels:", vowels)
#     print("Consonants:", consonants)

#     if vowels > consonants:
#         print("Name is Vowels Heavy")
#     elif consonants > vowels:
#         print("Name is Consonants Heavy")
#     else:
#         print("Name is Balanced")

#     print("Total Marks:", total)
#     print("Percentage:", percentage)
#     print("Grade:", grade)


#     if total > highest_marks:
#         highest_marks = total
#         highest_student = name


# print("\n==============================")
# print("Student with Highest Marks")
# print("Name:", highest_student)
# print("Marks:", highest_marks)
# print("==============================")

#18 dought


#19

# sentence = input("Enter a sentence: ")

# has_digit = False
# has_dot = False
# has_at = False
# password_like = False
# repeated_special = False

# special_count = 0
# previous_special = ""

# for ch in sentence:

#     if ch.isdigit():
#         has_digit = True

#     if ch == ".":
#         has_dot = True

#     if ch == "@":
#         has_at = True

#     if not ch.isalnum() and ch != " ":

#         special_count += 1

#         if ch == previous_special:
#             repeated_special = True

#         previous_special = ch

#     else:
#         previous_special = ""


# if has_digit and has_at and len(sentence) >= 8:
#     password_like = True

# if password_like or repeated_special:
#     classification = "Suspicious"

# elif has_digit or has_dot or has_at:
#     classification = "Review"

# else:
#     classification = "Safe"



# print("Contains digits:", has_digit)
# print("Contains URL-like '.' :", has_dot)
# print("Contains '@':", has_at)
# print("Password-like:", password_like)
# print("Repeated special characters:", repeated_special)
# print("Security Classification:", classification)

#20

# n=int(input("Enter a number : "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         result=i*j

#         if result%5==0:
#             print("F" , end=" ")
#         elif result%2==1:
#             print("O",end=" ")
#         else:
#             print("E",end=" ")
#     print()

#21

# total=0
# for i in range(1,11):
#     price=int(input(f"Enter price of product {i}: "))
#     total+=price
# if total>=5000:
#     print(f"Your total amount of price is {total}")
#     print(f"Your final value after appling 20% discount is {total-(total*0.2)}")
# elif total>=3000:
#     print(f"Your total amount of price is {total}")
#     print(f"Your final value after appling 15% discount is {total-(total*0.15)}")
# elif total>=1000:
#     print(f"Your total amount of price is {total}")
#     print(f"Your final value after appling 10% discount is {total-(total*0.1)}")
# else:
#     print(f"Your total amount of price is {total}")
#     print(f"Your final value after not appling discount is {total}")

#22

# st="aaabbccccdd"
# ca=0
# cb=0
# cc=0
# cd=0
# for ch in st:
#     if ch=="a":
#         ca+=1
#     elif ch=="b":
#         cb+=1
#     elif ch=="c":
#         cc+=1
#     else:
#         cd+=1
# print(f"a{ca}b{cb}c{cc}d{cd}")

#23

# total=0
# for i in range(1,9):
#     sallary=int(input(f"Enter your sallary {i} : "))
#     total+=sallary
#     Averege=total/8
#     if sallary>=100000:
#         print("You are our Execulative Employee")
#     elif sallary>=50000:
#         print("You are our Senior Employee")
#     elif sallary>=25000:
#         print("You are our Mid level Employee")
#     else:
#         print("You are our Junior level Employee")
# print(f"Average Sallary of our Employees have {Averege}")

#24

# sen=input("Enter a sentence : ")
# secret=input("Enter a secret word : ")
# for ch in sen:
    


#25

n=int(input("Enter a number : "))
num=1
for i in range(1,n+1):
    for j in range(i):
        if num%3==0 and num%5==0:
            print("F",end=" ")
        elif num%3==0:
            print("E",end=" ")
        elif num%2==0:
            print("T",end=" ")
        else:
            print("O",end=" ")
        num+=1
    print()

# n = int(input("Enter n: "))

# num = 1

# for i in range(1, n + 1):
#     for j in range(i):
        
#         if num % 3 == 0 and num % 5 == 0:
#             print("F", end=" ")
#         elif num % 3 == 0:
#             print("T", end=" ")
#         elif num % 2 == 0:
#             print("E", end=" ")
#         else:
#             print("O", end=" ")
        
#         num += 1
    
#     print()