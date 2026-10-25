import csv, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def add_student(fname,name,marks):
    with open(fname+".csv",'a',newline="") as file:
        w=csv.writer(file)
        w.writerow((name,marks))
def create_file(fname):
    with open(fname+".csv",'w') as file:
        w=csv.DictWriter(file,fieldnames=["Name","Marks"])
        w.writeheader()
def read_data(fname):
    with open(fname+".csv",'r',newline='') as file:
        read=file.readlines()
        for row in read:
            print(row)
def avg(fname):
    with open(fname+".csv",'r') as file:
        read=file.readlines()
        sum=0
        for row in read:
            if row.strip()=='':
                continue
            name,marks=row.strip().split(",")
            if name!="Name":
                sum+=int(marks)
        return sum/(len(read)-2)
def highest(fname):
    dic={}
    with open(fname+".csv",'r') as file:
        read=file.readlines()
        for row in read:
            if row.strip()=='':
                continue
            name,marks=row.strip().split(",")
            if name!="Name":
                dic[name]=int(marks)
        l=list(dic.values())
        val=max(l)
        for key,value in dic.items():
            if value==val:
                print(f"{key} has got {value} marks which is highest marks")
print("MENU:")
print()
print("Enter 1 to create a file")
print("Enter 2 to add student data")
print("Enter 3 to get student marks data of a class")
print("Enter 4 to get average of a class")
print("Enter 5 to get highest marks in class")
print("Enter 6 to exit")
ch=int(input("Enter your choice:"))
while True:
    if ch==1:
        n=input("Enter class name to create a file:")
        create_file(n)
        print("File created")
    elif ch==2:
        fname=input("Enter class name:")
        n=int(input("Enter number of students to add:"))
        for i in range(n):
            name=input(f"Enter student {i+1} name:")
            marks=int(input("Enter marks:"))
            add_student(fname,name,marks)
            print()
    elif ch==3:
        n=input("Enter class name to read data:")
        read_data(n)
    elif ch==4:
        n=input("Enter class name to get average:")
        print(f"The avg marks of class {n} is {avg(n)}")
    elif ch==5:
        n=input("Enter class name to get highest marks:")
        highest(n)
    elif ch==6:
        print("Exiting.......")
        break
    else:
        print("Enter proper choice")
    ch=int(input("Enter your choice:"))
