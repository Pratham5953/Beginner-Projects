print("Welcome to the game of hand cricket by PRATHAM")
n=input("Enter your name:")
print()
print("Enter any number between 1 and 9 (both inclusive)while playing")
print("If you enter any other number while batting, 1 run will be detucted from")
print("your score as penality. If you do it while balling, the system gains its ")
print("runs normally and you will lose a chance of making the system out")
ss=0
ps=0
print()
print("Write 1 to choose batting and 2 for balling")
ch=int(input("Enter your choice:"))
import random
if ch==1:
    print("You have chosen to bat")
    while True:
        s=random.randint(1,9)
        p=int(input("Enter your number:"))
        print("Systems number:",s)
        if p<1 or p>9:
            print("You have entered invalid number and will lose 1 run")
            p=(-1)
        if p==s:
            print("--------------YOU ARE OUT-----------------")
            print("Your score is:",ps)
            break
        ps+=p
    print("Now its your turn is to ball")
    while True:
        s=random.randint(1,9)
        p=int(input("Enter your number:"))
        print("Systems number:",s)
        if p==s:
            print("--------------SYSTEM IS OUT-----------------")
            print("System score is:",ss)
            break
        ss+=s
        if ss>ps:
            break
elif ch==2:
    print("You have chosen to ball")
    while True:
        s=random.randint(1,9)
        p=int(input("Enter your number:"))
        print("Systems number:",s)
        if p==s:
            print("--------------SYSTEM IS OUT-----------------")
            print("System score is:",ss)
            break
        ss+=s
    print("Now its your turn to bat")
    while True:
        s=random.randint(1,9)
        p=int(input("Enter your number:"))
        print("Systems number:",s)
        if p<1 or p>9:
            print("You have entered invalid number and will lose 1 run")
            p=(-1)
        if p==s:
            print("--------------YOU ARE OUT-----------------")
            print("Your score is:",ps)
            break
        ps+=p
        if ps>ss:
            break
else:
    print("Please rerun the game as you have entered a wrong choice")
if ch==1 or ch==2:
    print()
    print("Your(",n,") score is:",ps)
    print("System score is:",ss)
    print()
    if ss<ps:
        print("-----CONGRAGULATIONS! YOU WON WITH A LEAD OF ",ps-ss," RUNS-----")
    elif ps<ss:
        print("-----YOU LOST THE GAME BY ",ss-ps," RUNS. BETTER LUCK NEXT TIME-----")
    elif ps==ss:
        print("THE MATCH IS A DRAW AS THE SYSYEM AND YOU SCORED THE SAME")
