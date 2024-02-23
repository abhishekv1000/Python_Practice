import random

stage = ['''
       +---+
       O   |
      /|\  |
      / \  |
          ===''', '''

       +---+
       O   |
      /|\  |
      /    |
          ===''', '''

        +---+
       O   |
      /|\  |
           |
          ===''', '''
       +---+
       O   |
      /|   |
           |
          ===''', '''
        +---+
       O   |
       |   |
           |
          ===''', '''
       +---+
       O   |
           |
           |
          ===''', '''
       +---+
           |
           |
           |
          ===''']

lives = 6

dictionary = ["mouse" , "cat" , "eye" , "read"]
word = random.choice(dictionary)
word_list = list(word)

word_blank = []

for j in range (len(word_list)):
   word_blank += "_"

print(word_list)

while not (word_list == word_blank ):
   char = input("Guess A Charater In Word : ").lower()

   for i in range(len(word_list)) :
        if word_list[i] == char:
           word_blank[i] = char 
   print(word_blank)   
   
   if char not in word :
       lives -= 1
       if lives == 0:
           print("YOU LOSE")    

   print(stage[lives])
