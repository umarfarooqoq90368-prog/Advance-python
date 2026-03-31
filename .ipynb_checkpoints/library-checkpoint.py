from secrets import choice

import numpy as np
import pandas as pd
dic={"name":[],"age":[],"balance":[5000,]}
while True:
    method = input("Enter your choice:"
                   "\n 1:create account: "
                   "\n 2:check  balance:"
                   "\n 3:withDraw amount"
                   "\n 4:Deposit amount"
                   )
    choice = input("Enter your choice (y/n): ")

    if method=="1":
        name=input("Enter your name:")
        age=int(input("Enter your age:"))
        dic["name"].append(name)
        dic["age"].append(age)
        dic["balance"].append("balance")
        print(f"{name}account created and your balance is: {"balance"}:")
        for i in dic:
            if i=="name":
                dic[i]=choice
        print(f"{name}your account is already created{"balance"}")
        print(choice=="y")
        continue
    if method=="2":
        print(f"{"balance"}")
        for d in dic:
            if dic[d]=="balance":
                dic[d]=choice
                print(f"{name}your  current account {"balance"}")
    if method=="3":
        amount=int(input("Enter your amount:"))
        for f in dic:
            if dic[f] == "balance":
                dic[f]=choice
        balance="balance"-amount
        dic["balance"].append("balance")
        print(f"your current balance is: {"balance"}")
    if method=="4":
        name=input("Enter your name:")
        amount=int(input("Enter your amount:"))
        for h in dic:
            if dic[h] == name:
                dic[h]=choice
        balance=balance+amount
        dic["balance"].append(balance)
        print(f"your current balance is: {"balance"}")


