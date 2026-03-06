#1 The Multi-Line Story:
print("""A boy found an old key in his garden
He tried it on a locked box in his house.
Inside, he discovered his grandfather’s hidden treasure. 
""")

#2The Border:
print("*********")
print(" Python ")
print("*********")

#3The Separator:
print(1,2,3,4,5,sep=" ->")
#4 The End Game:

print("my name is umar",end=" ")
print("I am student")

#5. The Formatter:
decnum=12.34567
print(f"{decnum:.2f}")

#2. The input() Function
#1 The Greeter
name = input("Enter your name: ")
color = input("Enter your favorite color: ")
print(f"Hi {name}, {color} looks great on you")

#2 The Age Gap:
age=int(input("enter your age"))
current_year=int(input("enter your current year"))
future_age=age+(2050-current_year)
print(f"In 2050 you will be {future_age} years old")

#3 The Multiplier:
num1=int(input("enter your first number"))
num2=int(input("enter your second number"))
print(num1*num2)
#TypeError: can't multiply sequence by non-int of type 'str'
#4 The Repeater:
word=input("enter your word")
num=int(input("enter your number"))
print(num*word)
#5 The Bill Splitter:
totalbill=int(input("enter total bill of amount"))
people=int(input("enter number of people"))
print(f"{totalbill/people}")


#3. Operators
# 1The Remainder:
num1=int(input("enter your first number"))
num2=int(input("enter your second number"))
print(f"number one:{num1} and number two: {num2}and its Remainder:{num1%num2} ")

#2. The Power:
x=int(input("enter your first number"))
y=int(input("enter your second number"))
print(f"{x**y}")

#3. The Floor:
num1=int(input("enter your first number"))
num2=int(input("enter your second number"))
print(f"{num1//num2}")

#4. The Comparison:
num = int(input("Enter a number: "))
print(num > 100)

#5.The Swapper:
a=10
b=15
a,b=a,b
print("a=",a)
print("b=",b)


