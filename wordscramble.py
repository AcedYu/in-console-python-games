#import the random module
import random
#create a predefined list of words for the game
wordlist = ["code", "coder", "python", "string", "boolean", "integer", "double", 
            "number", "list", "array", "function", "class", "object"]

#randomly choose a word from the list
word = random.choice(wordlist)

#scramble the word
scrambled = ''.join(random.sample(word, len(word)))

#Let the player know what the game is about
print("Welcome to the word guessing game!")
print("Guess the Scrambled Word provided!")
print("Your scrambled word is: " + scrambled)

#game logic loop
while True:
  guess = input("Enter your guess here: ")
  if guess == word:
    print("Congratulations you are correct!")
    break
  else:
    print("Incorrect, try again!")