# print("Welcome To Rollercoaster!")

# height = int( input("Enter Your Age "))

# if height > 120:
#     print("You Are Ride On Rollercoaster")
# else:
#     print("So Try Anther")


# ..........................

# print(" Check Odd Even Number")

# number = int(input("Enter Your No."))

# if number % 2 == 0:
#     print (f"{number} is Even")
# else :
#     print(f"{number} Is ODD")


# height = float(input("Enter Your Height In Meter\n"))
# weight = float(input("Enter Your Weight In KG : \n"))

# bmi = round(weight/(height**2))

# if bmi < 18.5:
#     print(f"Your BMI is {bmi}")
# elif bmi < 25 :
#     print(f"Your BMI is {bmi}")
# elif bmi < 30 :
#     print(f"Your BMI is {bmi}") 
# elif bmi < 35 :
#     print(f"Your BMI is {bmi}")
# else :
#     print(f"Your BMI is {bmi}")


# year = int(input("Enter The Year"))

# if (year%400 == 0) or (year % 4==0 and year%100!=0):

#     print("Leap Year")
# else:
#     print("Not a Leap Year")

#..................................

# print("Welcome to Python Pizza Deiveries")

# size = input("What Is the Size Of Pizza ? S,M or L :\n")
# add_pepperoni = input("Do you want pepperoni ? Y or N :\n")
# extra_cheese = input("Do you want extr cheese ? Y or N :\n")
# bill = 0

# if size == "S":
#     bill+=15
# elif size == "M":
#     bill+=20
# else :
#     bill+=25 

# if add_pepperoni == "Y" :
#     if size == "S":
#       bill +=2
#     else :
#        bill+=3

# if extra_cheese == "Y" :
#     bill+=1

# print(bill)

# .....................

print("Welcome To LOve Calculator !")

name1 = input("What is Your Name ? \n")
name2 = input("Whar Is Their name ? \n")

both_name = (name1 + name2).lower()

t = both_name.count('t')
r = both_name.count('r')
u = both_name.count('u')
e = both_name.count('e')

true = t+r+u+e

l = both_name.count('l')
o = both_name.count('o')
v = both_name.count('v')
e = both_name.count('e')

love = l+o+v+e

love_score = str(true) + str(love)

if love_score < 10 or love_score >90:
    print(f"Your Score is {love_score} You Go Together like Coke and Mentos")
elif 40 < love_score < 50:
    print(f"Your Score is {love_score} , Your Are Alright Together")
else :
    print(f"Your Score Is {love_score}")    





 