import csv
import os
import time
import datetime
os.chdir(os.path.dirname(os.path.abspath(__file__)))
class account:
    def __init__(self,name,acc_no,password,bal):
        self.name=name
        self.acc_no=acc_no
        self.password=password
        self.bal=int(bal)
        self.time=datetime.datetime.now().strftime("%d/%m/%Y %I:%M %p")
    def withdraw(self,n):
        if n<=self.bal:
            print("Collect cash from counter")
            self.bal=self.bal-n
            with open("Transaction.csv",'a',newline="") as f:
                write=csv.writer(f)
                write.writerow((self.name,self.acc_no,"Withdraw",self.time))
        else:
            print("You dont have that much money in ur account")
    def deposite(self,n):
        self.bal=self.bal+n
        with open("Transaction.csv",'a',newline="") as f:
            write=csv.writer(f)
            write.writerow((self.name,self.acc_no,"Deposit",self.time))

    def check_bal(self):
        print(f"You have Rs/{self.bal} in your account")

class bank:
    def __init__(self):
        self.fname="Bank of Pratham.csv"
        self.time=datetime.datetime.now().strftime("%d/%m/%Y %I:%M %p")

    def create_user(self):
        if not os.path.exists("Bank of Pratham.csv"):
            with open("Bank of Pratham.csv",'w',newline='') as file:
                write=csv.DictWriter(file,fieldnames=["name","acc_no","bal","password"])
                write.writeheader()
                with open("Transaction.csv",'w',newline='') as f:
                    write=csv.DictWriter(f,fieldnames=["name","acc_no","type","date and time"])
                    write.writeheader()
        name=input("Enter your name:")
        while True:
            pas=input("Enter a password of any 4 digit pin:")
            if len(pas)==4 and pas.isdigit():
                break
            else:
                print("Password must be of exactly 4 digits. Retry!")
                continue    
        with open("Transaction.csv",'r' , newline="") as f:
            acc_no=10000
            read=csv.DictReader(f)
            for row in  read:
                if int(row["acc_no"])>acc_no:
                    acc_no=int(row["acc_no"])
        with open("Bank of Pratham.csv",'a+' , newline="") as file:
            write=csv.writer(file)
            write.writerow((name,acc_no+1,0,pas))
            print(f"Your account number is:{acc_no+1}")
        with open("Transaction.csv",'a',newline="") as f:
            write=csv.writer((f))
            write.writerow((name,acc_no+1,"New User",self.time))
                   
    def login(self):
        name=input('Enter your name:')
        acc=input("Enter your account nunmber:")
        pas=input("Enter your password:")
        if not os.path.exists("Bank of Pratham.csv"):
            return "Account doesn't exist"
        with open("Bank of Pratham.csv","r",newline='') as file:
            read=csv.DictReader(file)
            for row in read:
                if row['acc_no']==acc:
                    if row['name']==name and row['password']==pas:
                        return account(row["name"],row["acc_no"],row["password"],row["bal"])
            return "Invalid username or password for the account numberor the account doesn't exist, retry"
    def transfer(self,Account,Acc,n):
        with open("Bank of Pratham.csv",'r' , newline="") as file:
            read=csv.DictReader(file)
            if Account.bal>=n:
                Account.bal-=n
                Acc.bal+=n
                with open("Transaction.csv",'a',newline="") as f:
                    write=csv.writer(f)
                    write.writerow((Account.name,Account.acc_no,"Money Transfer",self.time))
                    write.writerow((Acc.name,Acc.acc_no,"Money Recieved",self.time))
            else:
                print("Transaction failed! Not enough balance in your account.")
    def refresh(self,Account):
        with open("Bank of Pratham.csv",'r' , newline="") as file:
            read=csv.DictReader(file)
            rows=[]
            for row in read:
                if Account.acc_no==row["acc_no"]:
                    rows.append({"name":Account.name,"bal":Account.bal,"acc_no":Account.acc_no,"password":Account.password})
                else:
                    rows.append(row)
        with open("Bank of Pratham.csv",'w' , newline="") as file:
            write=csv.DictWriter(file,fieldnames=["name","acc_no","bal","password"])
            write.writeheader()
            write.writerows(rows)
        

    def remove(self,Account):
        with open("Bank of Pratham.csv",'r' , newline="") as file:
            read=csv.DictReader(file)
            rows=[]
            for row in read:
                if Account.acc_no==row["acc_no"]:
                    print(f"User removed, collect your cash of Rs/{Account.bal} in counter")
                else:
                    rows.append(row)
        with open("Bank of Pratham.csv",'w' , newline="") as file:
            write=csv.DictWriter(file,fieldnames=["name","acc_no","bal","password"])
            write.writeheader()
            write.writerows(rows)
            with open("Transaction.csv",'a',newline="") as f:
                    write=csv.writer(f)
                    write.writerow((Account.name,Account.acc_no,"Account Removed",self.time))
    def transaction(self,Account):
        with open("Transaction.csv",'r',newline="") as f:
            read=csv.DictReader(f)
            for row in read:
                if row["acc_no"]==Account.acc_no:
                    print(row)
print("1.Login")
print("2.New User")
print("3.Exit")
ch=int(input("Enter your choice:"))
while True:
    if ch==1:
        Bank=bank()
        Account=Bank.login()
        if type(Account)==str:
            print(Account)
        else:
            Bank=bank()
            print("Menu")
            print('1. withdraw money')
            print("2. Deposite money")
            print("3. Transfer Money")
            print("4. Check Balance")
            print("5. View Transaction History")
            print("6. Remove user")
            print("7. Logout")
            c=int(input("Enter your choice:"))
            while True:
                if c==1:
                    n=int(input("Enter amount to withdraw:"))
                    Account.withdraw(n)
                    Bank.refresh(Account)
                elif c==2:
                    n=int(input("Enter amount to deposit:"))
                    Account.deposite(n)
                    Bank.refresh(Account)
                elif c==3:
                    name=input('Enter name to transfer money:')
                    acc=input("Enter account nunmber:")
                    with open("Bank of Pratham.csv","r",newline='') as file:
                        read=csv.DictReader(file)
                        for row in read:
                            if row['acc_no']==acc:
                                if row['name']==name:
                                    Acc=account(row["name"],row["acc_no"],row["password"],row["bal"])
                                    n=int(input("Enter amount to transfer:"))
                                    Bank.transfer(Account,Acc,n)
                                    Bank.refresh(Account)
                                    Bank.refresh(Acc)
                                else:
                                    print("Invalid username for the account number or the account doesn't exist, retry")
                    
                    
                elif c==4:
                    Account.check_bal()
                elif c==5:
                    Bank.transaction(Account)
                elif c==6:
                    Bank.remove(Account)
                    Account=""
                    time.sleep(2)
                    break
                elif c==7:
                    with open("Transaction.csv",'a',newline="") as f:
                        write=csv.writer(f)
                        write.writerow((Account.name,Account.acc_no,"User Logout",datetime.datetime.now().strftime("%d/%m/%Y %I:%M %p")))
                    Account=""
                    break
                else:
                    print("Please enter a proper choice")
                time.sleep(2)
                c=int(input("What do u want to do next (1.witdraw 2.Deposit 3.Transfer money 4.Check Balance 5.View Transactions 6.Remove user 7.Logout):"))
    elif ch==2:
        Bank=bank()
        Bank.create_user()
    elif ch==3:
        print("Exiting......")
        break
    else:
        print("You should have entered correct option, retry again")
    time.sleep(2)
    ch=int(input("Enter your choice (1.Login, 2.New User), 3.Exit:"))