import pandas as pd
while True:
    choise= input("Enter your choice:"
                   "\n 1:create account: "
                   "\n 2:check  balance:"
                   "\n 3:withDraw amount"
                   "\n 4:Deposit amount"
                  "\n 5:Exist"
                   )
    if choise == "1":
        print("create account")
    elif choise == "2":
        print("check balance")
    elif choise == "3":
        print("withdraw amount")
    elif choise == "4":
        print("deposit amount")
    elif choise == "5":
        print("exist")
        break
    useracc={"name":["umar"],"account":[103],"balance":[5000,]}
    df=pd.DataFrame(useracc)
    print(df)

