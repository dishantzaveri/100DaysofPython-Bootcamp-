def format_name(f_name,l_name):
    if f_name=="" or l_name=="":
        return "No name"
    formatted_f_name=f_name.title()
    formatted_l_name=l_name.title()
    return formatted_f_name+" "+formatted_l_name

string= format_name("f","f")
print(string)

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year,month):
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    else:
        return month_days[month-1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def divide(n1,n2):
    return n1/n2    

def multiply(n1,n2):
    return n1*n2


operations={"+":add,"-":subtract,"/":divide,"*":multiply}

num1=int(input("what is the first element"))
num2=int(input("what is the second element"))
for symbol in operations:
    print(symbol)
operation_symbol= input("what is the operation")


print(f"{num1} {operation_symbol} {num2} = {operations[operation_symbol](num1,num2)}")