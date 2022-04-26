rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_img=[rock,paper,scissors]
import random
inp=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if(inp>=3 or inp<0):
    print("You typed an invalid number, you lose!")
else:
    print(game_img[inp])
    com_inp=random.randint(0,2)
    print("Computer chose:")
    print(game_img[com_inp])
    
    if(inp==0 and com_inp==2):
        print("You win!")
    elif(inp==com_inp):
        print ("It's a draw")
    elif(inp==1 and com_inp==2):
        print("You win!")
    elif(inp==2 and com_inp==0):
        print("You loose")
    elif(inp==2 and com_inp==1):
        print("You win!")
    elif(inp==0 and com_inp==1):
        print("You loose")
    elif(com_inp>inp):
        print("You lose")
