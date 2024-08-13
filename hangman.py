#hangman game
import random

#words list
words = ["code", "python", "console", "algorithm", "scratch"]

#program selects random word
secretword = random.choice(words)

#program sets up blank string of _'s
guessed = ""
print("Welcome to the hangman game! Guess the letters in my secretly chosen word!")

for char in secretword:
  guessed += "_"

print(guessed)

#program asks user to guess a letter
while True:
  #winning logic
  if "_" not in guessed:
    print("Congratulations you guessed all of the letters!")
    break
    
  guess = input("Guess a letter: ")

  if guess == secretword:
    print("Congratulations you guessed the word " + secretword + "!")
    break

  if len(guess) > 1:
    print("That guess is incorrect")
    continue
  
  temp = ""
  if guess in secretword:
    for i in range(len(guessed)):
      if guess == secretword[i]:
        temp += guess
      elif guessed != "_":
        temp += guessed[i]
      else:
        temp += "_"
    guessed = temp
  else:
    print("That letter/guess is not in the word")
    
  print(guessed)