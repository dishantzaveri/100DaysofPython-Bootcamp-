# ifelse

print('welcome to the rollercoaster')

height=int(input("height in cm bolo apni."))

if height >= 120:
    print("you are tall enough to ride")
    age=int(input("age bolo apni."))
    if age < 12:
        print("pay 5")
    elif age<22:
        print("pay 12")
    elif age<18:
        print("pay 10")

    else:
        print("pay 15")

else:
    print("you are not tall enough to ride")

number=int(input("number bol"))

if number%2==0:
    print("even")
else:
    print("odd")    


# leapyear

year=int(input("enter the year bhai"))

if year % 4==0:
    if year % 100==0:
        if year % 400==0:
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("leap year")
else:
    print("not a leap year")
bill = 0
size=(input("enter size of pizza , S ,M OR L"))

addpepperoni=input("do you want pepperoni , Y OR N")

extracheese=input("do you want extracheese , Y OR N")

if size=="S":
    bill=bill+15
    if addpepperoni=="Y":
        bill=bill+2
    if extracheese=="Y":
        bill=bill+1
elif size=="M":
    bill=bill+20    
    if addpepperoni=="Y":
        bill=bill+3
    if extracheese=="Y":
        bill=bill+1
elif size=="L": 
    bill=bill+25    
    if addpepperoni=="Y":
        bill=bill+3
    if extracheese=="Y":
        bill=bill+1
else:
    print("invalid size")

print(f"total bill is ${bill}")


