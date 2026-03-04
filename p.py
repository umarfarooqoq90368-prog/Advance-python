#promblem 1
"""name=input("enter you name")
age=int(input("enter you age"))
pasword=input("enter you password")
if len(name)<5:
    print("your name is invalied")
    for i in pasword:
        if "@" not in i:
           print("your password is weak")
elif age<18:
    print("your age is less than 18")
else:
    print("login complet")
#problem 2
sentes=input("enter you sentence")
print(len(sentes))
print(sentes.split())
print(sentes.count("a"))
print(sentes[::1])
num=int (input("enter number"))
for i in num:
    if i%2==0:
        print(f"{num} is an even number")
    elif num%2!=0:
        print(f"{num} is an odd number")
    else:
           for p in range(2,i):
               if i%p==0:
                   print(f"{num} is an prime number")
               else:
                   print(f"{num} is not a prime number")
#problem 3

username = input("Enter your username: ")

if len(username) < 6:
    print("Your username length is less than 6")

else:
    has_digit = False
    for i in username:
        if i.isdigit():
            has_digit = True
    if has_digit:
        print("Your username is valid")
    else:
        print("Username must contain at least 1 digit")
#promblem 5

students = {
    "Ali": 45,
    "Umar": 82,
    "Ahmed": 30,
    "Hamza": 90,
    "Saad": 55}
totalmarks = 0
highmarks = 0
toper = ""
for name, marks in students.items():
    if marks < 50:
        print(f"{name} has less than 50 marks")
    if marks > 80:
        print(f"{name} is Topper")
    totalmarks += marks
    if marks > highmarks:
        highmarks = marks
        toper = name
average = totalmarks / len(students)

print("Average Marks:", average)
print("Highest Marks Student:", toper, "-", highmarks)

#problem 6

word = input("Enter a word: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

name=input("Enter your name: ")
age=int(input("Enter your age: "))
if age<18:
    print(f"{name} you are a teenager")
elif age>18 or age<40:
    print(f"{name} you are an adult")
else:
    print(f"{name} you are mature")
s="programming"
vowels=0
dic={}
for char in s:
    if char in "aeiou":
        vowels+=1
    if char in s:
        dic=char.count(char)
    else:
        print(dic)"""