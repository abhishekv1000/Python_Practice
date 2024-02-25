# def greet() :
#     print("Thanks U")

# greet()    

# def my_fun(a, b):
#     print(f"The NUMber IS {a},{b}")

# a = int(input("Please Enter The NUMber"))
# print(my_fun(a, 10))

# import math

# def no_of_cans(H, W, C):

#     print((H*W)/C)

# H = int(input("Enter The Height"))
# W= int(input("Enter The Width"))  
# C=5

# no_of_cans(H,W,C)

# def Prime_checker(Number):
#     count = 0
#     for i in range(1, Number+1):
#         if Number % i==0:
#             count += 1
#     print(count)        
#     if count ==2:
#         print("THE NUMBER IS PRIME")
#     else:
#         print("THIS IS NON PRIME" )    

# no = int(input("Enter The Number TO Check "))

# Prime_checker(no)

#**********************************************************************#
#**************************Encryption && Depcryption*******************#

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import string
from Day8_art import logo

print(logo)

ABCD = list(string.ascii_lowercase)
ABCD = ABCD 

def caesar(input, shift , direction) :
    Final_Text = ""
    if direction == "decode" : 
        shift *= -1
 
    for char in input:
        if char in ABCD:
            pos = ABCD.index(char)
            new_position = pos + shift 
            Final_Text += ABCD[new_position]
        # Final_Text += char    
    print(f"THE {direction} text is {Final_Text}")


should_continue = True

while should_continue:
   direction = input("Type 'encode' to encrypt , type 'decode' to decrypt : \n")
   text = input("Type Your Message : \n").lower()
   shift = int(input("Type the Number of Shifts : \n"))
   shift = shift % 26

   caesar(text,shift, direction)

   result = input("Type 'Yes' if you want to continue otherwise Type 'No' ")
   if result == 'no' :
       should_continue = False
       print("GOODBYE")



       


# def Encrypt(plain_text , shift_no): 
#    cipher_text = ""

#    for alpha in plain_text:
#         new_position = ABCD.index(alpha) + shift_no
#         new_alpha = ABCD[new_position]
#         cipher_text += new_alpha

#    print(cipher_text)



# def Decrypt(cipher_text ,shift_no):
#     old_text = ""

#     for alpha in cipher_text:
#         new_position = ABCD.index(cipher_text) - shift_no
#         old_alpha = ABCD[new_position]
#         old_text += old_alpha
#     print(old_text) 



# if direction == "encode" :
#     Encrypt(text , shift)
# elif direction == "decode":
#     Decrypt(text, shift)



