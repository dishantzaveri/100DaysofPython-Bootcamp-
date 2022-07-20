

heights=input("enter the heights of the people").split()

for n in range(0,len(heights)):
    heights[n]=int(heights[n])
print(heights)

print(max(heights))

highest = 0

for score in heights:
    if score > highest:
        highest = score

print(f"highest score is {highest}")

print(sum(heights))
print(len(heights))

total_height=0

for height in heights:
    total_height+=height
print(total_height )

students = 0 
for student in heights:
    students+=1
print(students)

average_height=int(total_height/students)
print(average_height   )

heights=input("enter the heights of the people").split()

for n in range(1,101):
    if n%3==0 and n%5==0:
        print("fizzbuzz")
    elif n%3==0:
        print("fizz")
    elif n%5==0:
        print("buzz")
    else :
        print(n)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

for char in range(1, nr_letters + 1):
  password += random.choice(letters)

for char in range(1, nr_symbols + 1):
  password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password += random.choice(numbers)

print(password)

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")