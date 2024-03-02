import random
from game_data12 import data

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""


def get_random_dta():
    return random.choice(data)

def format_data(new):

    name = new["name"]
    # follower = new["follower_count"]
    About = new["description"]
    Country = new["country"]

    return f"{name}, {About} ,{Country}"

# def check(guess, a, b):
#     if a >b and guess == "a":
#         return True
#     else:
#         return False
        

def game():
   
    print(logo)
    score = 0
    game_should_continue = True
 
    while game_should_continue :  
  
        A = get_random_dta()
        B = get_random_dta()
        if  A == B:
            B = get_random_dta()


        print(f"Campare A : {format_data(A)}")
        print(vs)
        print(f"Campare B : {format_data(B)}\n")

        guess = input("Who HAs More Followers ? Type 'a' or Type 'b' ")

        A_followers = A["follower_count"] 
        B_followers = B["follower_count"]
 
        if (A_followers > B_followers) and guess =="a":    
            score += 1
            print(f"You're right! Current score: {score}.")
        else :
            game_should_continue = False
            print(f"Sorry ! That's Is Wrong . Final score: {score}.")


game()