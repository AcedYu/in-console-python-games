import random

print("welcome to the rock paper scissors GAME")

choices = ["rock", "paper", "scissors"]
com_choice = random.choice(choices)
my_choice=input("input choice: ")
print("The computer chose: "+ com_choice)
if my_choice =="rock" and com_choice=="paper":
  print ("you lose!")
elif my_choice =="rock" and com_choice=="rock":
  print("you tie")
elif my_choice =="rock" and com_choice=="scissors":
  print ("you WIN")
elif my_choice=="paper" and com_choice=="scissors":
  print("you lose")
elif my_choice =="paper" and com_choice=="paper":
  print ("you tie")
elif my_choice=="paper" and com_choice=="rock":
  print("you WIN")
elif my_choice =="scissors" and com_choice=="rock":
  print ("you lose")
elif my_choice=="scissors" and com_choice=="scissors":
  print ("you tie")
elif my_choice =="scissors" and com_choice=="paper":
  print ("you WWWWIIINNN")