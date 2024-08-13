import random

secret_number = random.randrange(0, 100)

print("Welcome to the number guessing game, guess the number I'm thinking of! (0-100)")

while True:
  guess = int(input("Guess here: "))

  if guess > secret_number:
    print("Your guess too high!")
  elif guess < secret_number:
    print("Your guess is too low!")
  else:
    print("You got it right! Congratulations")
    break