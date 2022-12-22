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
game_items = [rock , paper , scissors]


import random
user_choice = int(input('what do you choose ? Type 0 for Rock , 1 for Papper and 2 fpr Scissors\n'))
print(game_items[user_choice])
computer_choice = random.randint(0,2)
print(f'the computer chooses  {game_items[computer_choice]}')


if user_choice == 0 and computer_choice == 2 :
  print('You Win ')
elif computer_choice == 0 and user_choice == 2 : 
  print('You lose')
elif computer_choice > user_choice : 
  print('You lose ')

elif computer_choice == user_choice : 
  print("it's a draw")
elif user_choice >= 3 :
  print('You typed an invalid number , you lose ')
elif computer_choice< user_choice : 
  print('You win ')