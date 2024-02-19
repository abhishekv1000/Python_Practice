import random
# # import Day3 

# ram_value = random.randint(0,1)

# if(ram_value == 0):
#     print("Head")
# else :
#     print("Tail")

# List1 = ["ram" ,"gyan"]
# List1.append("shyam")
# print(List1)

# names = input('Enter The Names Of Person') 
# names_list = names.split(", ")

# x = len(names_list)

# ran_index = random.randint(0,x-1)
# print(f"{names_list[ran_index]} is going to market")

# row1 = ["1","1","1"]
# row2 = ["2","2","2"]
# row3 = ["3","3","3"]
# map = [row1 ,row2, row3]

# print(f"{row1}\n{row2}\n{row3}\n")

# position = input('Enter Your Position') #it is form of string

# horizontal = int(position[0])
# vertical = int(position[1])

# select_row =map[vertical-1 ] 

import random

print("ROCK < PAPER < SCISSORS")

rock = '''
   ________
---'  _____)
     (_____)
     (____)
----._(___)

'''
paper = '''
   __________
---'  _______)
     (_________)
     (_________)
----._(______) 

'''

scissors = '''

   ____________
---'  _________)
     (_________)
     (____)
----._(___) 


'''

user_choice = int(input("0 ==>> Rock or 1 ==>> Paper or 2 ==> Sissors\n"))
computer_choice = random.randint(0 ,2)
print(f"Computer choose {computer_choice}")

if (user_choice==0 and computer_choice==2):
    print("User Win")
elif (computer_choice > user_choice):
    print("computer win ")
elif (computer_choice == user_choice):
    print("draw")  
else :
    print("You TypedWrongss")   