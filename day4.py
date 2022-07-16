# import random

# rand=random.randint(0,200)

# print(rand)

# random_float=random.random()
# print(random_float)


# fuck=["f","u","c","k","u","-"]

# fuck.insert(9,'m')

# fuck.remove('c')

# fuck.pop()

# print(fuck.count("u"))

# fuck.sort()

# print(fuck)
import random


# names=["dishu","dish","dis","di"]

# payer=random.choice(names)

# print(len(names))

# print(payer+" pays")

user=int(input("type 0 for rock ,type 1 for paper , type 2 for scissor"))

comp=random.randint(0,2)
print(f"comp choice is {comp}")

if user== 0 and comp==1:
    print("comp wins")
elif user==0 and comp==2:
    print("user wins")
elif user==1 and comp==0:
    print("user wins")
elif user==1 and comp==2:
    print("comp wins")
elif user==2 and comp==0:
    print("comp wins")
elif user==2 and comp==1:
    print("user wins")
elif user==comp:
    print("tie")
else:
    print("invalid input")
