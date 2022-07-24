

def dishant(name):
    print(f"Hello {name}")
dishu = "Dishu"
dishant(name = dishu)

import math


def paint_calc(height, width, cover):
    area=height*width
    number_of_paints = math.ceil(area/cover)
    print(f"You will need {number_of_paints} liters of paint")


test_h=int(input("Enter the height of the triangle: "))
test_w=int(input("Enter the width of the triangle: "))
covarage=5
paint_calc(height=test_h,width=test_w,cover=covarage)

def prime_no(number):
    is_prime = True
    for i in range(2,number):
        if number%i==0:
            is_prime = False
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

n=int(input("Enter the number: "))
prime_no(number=n)

