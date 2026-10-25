import sqlite3
import time
import datetime
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
tran="Transaction.db"
det="Account details.db"

class account:
    def __init__(self,name,acc_no,password,bal):
        self.name=name
        self.acc_no=acc_no
        self.password=password
        self.bal=int(bal)
    def withdraw(self,n):
        if n<=self.bal:
            print("Collect cash from counter")
            self.bal=self.bal-n
            with sqlite3.connect(tran) as con:
                t=con.cursor()
                t.execute("INSERT INTO TRANSACTIONS VALUES(?,?,?,?);",(self.name,self.acc_no,"WITHDRAW",datetime.datetime.now().strftime("%d/%m/%Y %I:%M %p")))
            con.close()
        else:
            print("You dont have that much money in ur account")
    def deposit(self,n):
        self.bal=self.bal+n
        with sqlite3.connect(tran) as con:
            t=con.cursor()
            t.execute("INSERT INTO TRANSACTIONS VALUES(?,?,?,?);",(self.name,self.acc_no,"DEPOSIT",datetime.datetime.now().strftime("%d/%m/%Y %I:%M %p")))
        con.close()
    def check_bal(self):
        print(f"You have Rs/{self.bal} in your account")

class bank: 
    def create_user(self):
        with sqlite3.connect(det) as conn:
            c=conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS ACCOUNT_DETAILS(NAME TEXT, ACCOUNT_NO INT PRIMARY KEY,
            PASSWORD INT, ACCOUNT_BAL REAL);''')
            name=input("Enter your name:")
            while True:
                pas=input("Enter a password of any 4 digit pin:")
                if len(pas)==4 and pas.isdigit():
                    break
                else:
                    print("Password must be of exactly 4 digits. Retry!")
                    continue
        conn.close()   
        with sqlite3.connect(tran) as con:
            t=con.cursor()
            t.execute('''CREATE TABLE IF NOT EXISTS TRANSACTIONS(NAME TEXT, ACCOUNT_NO INT,
                        TYPE TEXT, DATE_TIME DATETIME);''')
            t.execute("SELECT MAX(ACCOUNT_NO) FROM TRANSACTIONS;")
            acc_no=t.fetchone()[0]
            if acc_no==None:
                acc_no=10000
        con.close()           
        with sqlite3.connect(det) as conn:
            c=conn.cursor()
            acc_no+=1
            c.execute("INSERT INTO ACCOUNT_DETAILS VALUES(?,?,?,?);",(name,acc_no,pas,0))
            print(f"Your account number is:{acc_no}")
        conn.close()
        with sqlite3.connect(tran) as con:
            t=con.cursor()
            t.execute("INSERT INTO TRANSACTIONS VALUES(?,?,?,?);",(name,acc_no,"NEW USER",datetime.datetime.now().strftime("%d/%m/%Y %I:%M %p")))
        con.close()
                   
    def login(self):
        name=input('Enter your name:')
        acc=int(input("Enter your account number:"))
        pas=input(("Enter your password:"))
        if not os.path.exists(det):
            return "Account doesn't exist"
        with sqlite3.connect(det) as conn:
            c=conn.cursor()
            c.execute("SELECT * FROM ACCOUNT_DETAILS WHERE NAME=? AND ACCOUNT_NO=? AND PASSWORD=?;",(name,acc,pas))
            d=c.fetchone()
        conn.close()
        if d==None:
            return "Invalid username or password for the account numberor the account doesn't exist, retry"
        return account(d[0],d[1],d[2],d[3])
    def transfer(self,Account,Acc,n):
        if Account.bal>=n:
            Account.bal-=n
            Acc.bal+=n
            with sqlite3.connect(tran) as con:
                t=con.cursor()
                t.execute("INSERT INTO TRANSACTIONS VALUES(?,?,?,?);",(Account.name,Account.acc_no,"Money Transfer",datetime.datetime.now().strftime("%d/%m/%Y %I:%M %p")))
                t.execute("INSERT INTO TRANSACTIONS VALUES(?,?,?,?);",(Acc.name,Acc.acc_no,"Money Recieved",datetime.datetime.now().strftime("%d/%m/%Y %I:%M %p")))
            con.close()
        else:
            print("Transaction failed! Not enough balance in your account.")
    def refresh(self,Account):
        with sqlite3.connect(det) as conn:
            c=conn.cursor()
            c.execute("UPDATE ACCOUNT_DETAILS SET ACCOUNT_BAL=? WHERE ACCOUNT_NO=?;",(Account.bal,Account.acc_no))
    def remove(self,Account):
        with sqlite3.connect(det) as conn:
            c=conn.cursor()
            c.execute("DELETE FROM ACCOUNT_DETAILS WHERE ACCOUNT_NO=?;",(Account.acc_no,))
        conn.close()        
    def transaction(self,Account):
        with sqlite3.connect(tran) as con:
            t=con.cursor()
            t.execute("SELECT * FROM TRANSACTIONS WHERE ACCOUNT_NO=?;",(Account.acc_no,))
            for row in t.fetchall():
                print(f"Name:{row[0]},Account No:{row[1]},Transaction Type: {row[2]},Date and Time:{row[3]}")
        
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
            print("2. deposit money")
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
                    Account.deposit(n)
                    Bank.refresh(Account)
                elif c==3:
                    name=input('Enter name to transfer money:')
                    acc=int(input("Enter account number:"))

                    with sqlite3.connect(det) as conn:
                        cur=conn.cursor()
                        cur.execute("SELECT * FROM ACCOUNT_DETAILS WHERE ACCOUNT_NO=? AND NAME=?;",(acc,name))
                        ro=cur.fetchone()
                    if not ro==None:
                        n=int(input("Enter amount to transfer:"))
                        Acc=account(ro[0],ro[1],ro[2],ro[3])
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
                    with sqlite3.connect(tran) as con:
                        t=con.cursor()
                        t.execute("INSERT INTO TRANSACTIONS VALUES(?,?,?,?);",(Account.name,Account.acc_no,"LOGOUT",datetime.datetime.now().strftime("%d/%m/%Y %I:%M %p")))
                    Account=""
                    break
                else:
                    print("Please enter a proper choice")
                time.sleep(2)
                c=int(input("What do u want to do next (1.withdraw 2.Deposit 3.Transfer money 4.Check Balance 5.View Transactions 6.Remove user 7.Logout):"))
    elif ch==2:
        Bank=bank()
        Bank.create_user()
    elif ch==3:
        print("Exiting......")
        break
    else:
        print("You should have entered correct option, retry again")
    time.sleep(2)
    ch=int(input("Enter your choice (1.Login, 2.New User, 3.Exit):"))