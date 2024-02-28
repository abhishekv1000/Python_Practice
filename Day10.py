# def Is_LeapYear(year):
#     if(year % 400 == 0) | (year%4 ==0 & year%100 ==0):
#         return True
#     else :
#         return False
    

# def days_in_month(year , month) : 

#     days = [31,28 ,31,30,31,30,31,31,30,31,30,31]
#     if Is_LeapYear(year) and month == 2:
#         return 29
#     return days[month-1]


# year = int(input("Enter A Year : "))
# month = int(input("Enter A Month : "))
# days = days_in_month(year,month)
# print(days)



def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def multi(n1, n2):
    return n1*n2
def div(n1, n2):
    return n1/n2


dic = {
    "+" : add,
    "-" : sub,
    "*" : multi,
    "/" : div
}

should_continue = True 

while should_continue:

    first_num = float(input(" What's The First Number? :"))
    print("+  -  *  /  ")
    op = input("Pick An Operator :")
    Sec_num =  float(input(" What's The Second Number? :"))

    calculation = dic[op]

    print(f"{first_num} {op} {Sec_num} = {calculation(first_num,Sec_num)}")

    if input("Type 'Yes' To Continue & 'No' To Stop : ") == "No":
        should_continue = False





