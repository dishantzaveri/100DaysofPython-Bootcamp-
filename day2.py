# print(len(12345))

print("Hello"[0])  

#subscripting

print(123+425)  #integer


123_43_2

a=float(123.45)
print(type(a))

print(str(100)+str(100))

two_digit_number=input('type a 2 digit number')

output=(int(two_digit_number[0])+int(two_digit_number[1]))

print(output)

height=input('type your height in inches')
weight=input('type your weight in pounds')

bmi = float(weight)/(float(height)*float(height))
bmi2 = float(weight)/float(height)

print(bmi)
bmi_as_int=int(bmi2)
print(bmi_as_int)

print(round(2.443467,3))

print(8//3)\

score=0
isWinning=True

print(f"your score is {score} and you are winning ? oh {isWinning}")  

# #tip calculator

bill = float(input("total bill is"))

tip= float(input("tip percentage is"))

people= int(input("number of people"))

pay= round(tip/100*(float(bill/people)),2) + float(bill/people)

print("each person pays",pay)

