import random

coin = random.choice(["Heads", "Tails"])
# Give some sort of intro to the game
# allow the user to input "Heads" or "Tails"
# IF the player's choice is the same as the random coin toss, say you win
# or ELSE say you lose
print ("HI! welcome to my coin-flip game!")
guess = input("Heads or Tails?: ")

if coin == guess:
  print ("The coin flipped " + guess + " YOU WIN!!!!!!!! ") 
else:
  print ( "The coin flipped " + guess + " YOU LOSE!!!!!!!!")