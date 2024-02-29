import random

print("Welcome To THe Number Guess Game !")
print("I'm Thinking of a Number Between 1 to 100")
num = random.randint(1,100)

print(f"Don't See Answer {num}")

Type = input("Choose a difficulty. Type 'easy' or 'hard' : -->>") 


attempt = 0
guess = 0


def game(attempt,guess):
   for i in range(1,attempt+1):

        if guess > num:
            attempt -= 1
            print(f"Yours attempt is {attempt}")
            print("Too High")
            guess = int(input("Make A Guess"))
        elif guess < num:
            attempt -=1
            print(f"Yours attempt is {attempt}")
            print("Too Low")
            guess = int(input("Make A Guess"))
            
        elif guess == num:
            print("You Won")
        else : 
          print("U LOOSE")


if Type == "hard" :
    print("You Have 5 Attempt Remaining To Guess The Number")
    attempt = 5
else :
    print("You Have 10 Attempt Remaining To Guess The Number") 
    attempt = 10 

while guess!= num:
      guess = int(input("Make A Guess"))
      game(attempt,guess)

