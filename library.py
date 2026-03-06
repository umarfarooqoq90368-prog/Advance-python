from secrets import choice

import numpy as np
import pandas as pd
dic={"name":[],"age":[],"balance":[]}
df=pd.DataFrame(dic)
print(df)

"""balance=0
while True:
    method = input("Enter your choice:"
                   "\n 1:create account: "
                   "\n 2:check  balance:"
                   "\n 3:withDraw amount"
                   "\n 4:Deposit amount"
                   )
    choice = input("Enter your choice (y/n")

    if method=="1":
        name=input("Enter your name:")
        age=int(input("Enter your age:"))
    elif name==dic["name"]:
        print(f"{name}your account is already created"{balance}"")
        print(f"{name}account created and your balance is: {balance}:")
        print(choice=="y")
        continue
    if method=="2":
        print(f"{balance}")
    if method=="3":
        amount=int(input("Enter your amount:"))
        balance=balance-amount
        print(f"your current balance is: {balance}")
    if method=="4":
        amount=int(input("Enter your amount:"))
        balance=balance+amount
        print(f"your current balance is: {balance}")"""


