# Animals = [ "tiger" ,"dog", "bear"]

# for animal in Animals:
#    print(animal)


# student_height = input("Enter Students Height Separate With Comma\n").split(",")
# total_height = 0
 
# ##....................(From For in)

# for n in student_height :
#     total_height += int(n)

# print(total_height/len(student_height))

# #...................(From For IN RANGE)

# for i in range(0, len(student_height)):
#      total_height += int(student_height[i])

# print(total_height/len(student_height))




# number = input("Enter Your Number \n").split(",")

# max_value = 0

# for i in number :

#     if max_value < int(i) :
#         max_value = int(i)

# print(f"I Found Largest Value {max_value}")




# even_total = 0

# for i in range(2,101,2):
#     print(i)
#     even_total += i

# print(even_total)

# evenTotal = 0

# for number in range(1,101):
#     if number%2==0 :
#       evenTotal += number

# print(evenTotal)



# num = int(input("Lets Take Number"))

# if num % 3 == 0 and num % 5 == 0:
#     print("Fizz")
# elif num % 3==0:
#     print("Fizz")
# elif num %5 ==0:
#    print("buzz")
# else:
#     print(number)


 
import random



print("WELCOME TO PASSWORD GEN")
alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
number = ['0','1', '2','3','4','5','6','7','8','9']
symbol = ['!','@','#','$','%','^','&','*']

num_alpha = int(input("Enter The COUNT ABC\n"))
num_ = int(input("Enter The COUNT NUMBER\n"))
num_sym = int(input("Enter The COUNT SYMBOL\n"))


#...............Easy Level

# password = ""

# for char in range(1, num_alpha+ 1):
#     password += random.choice(alpha)
    
# for char in range(1, num_ + 1):
#     password += random.choice(number)
    
# for char in range(1, num_sym + 1):
#     password += random.choice(symbol)
    
# print(password)

#.................Hard Level


pass_list = []

for count in range(1, num_alpha+ 1):
    pass_list += random.choice(alpha)
    
for count in range(1, num_ + 1):
    pass_list += random.choice(number)
    
for count in range(1, num_sym + 1):
    pass_list  += random.choice(symbol)
    
print(pass_list)
random.shuffle(pass_list)
print(pass_list)

pass_str = " "

for i in pass_list:
    pass_str += i
print(pass_str)

