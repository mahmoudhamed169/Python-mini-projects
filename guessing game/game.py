# guessing game


import random
EASY_LEVEL_TURNS = 3   
INTERMEDIATE_LEVEL_TURNS = 7
HARD_LEVEL_TURNS = 15
lower = 1


def set_difficulty():
  level = input("Enter the game level : \n1 (1) Easy 	 (2) Intermediate 	 (3) Hard : ")
  if level == "1":    
    return EASY_LEVEL_TURNS , 10 , 0
  elif level == "2" :    
    return INTERMEDIATE_LEVEL_TURNS , 100 , 0
  else:    
    return HARD_LEVEL_TURNS , 1000 , 0



def check_answer(guess, answer, turns ,attempts ): 
  if guess > answer:
    print("No, Decrease!")    
    return turns - 1  , attempts + 1
  elif guess < answer:
    print("No, Increase!")    
    return turns - 1  ,  attempts + 1
  else:
    turns = 0      
    print(f"You got it in {attempts} trials ! The answer was {answer}.")
    return turns , attempts 





def game():  
  print("Welcome to the Number Guessing Game!") 
  turns , upper , attempts  = set_difficulty()
  answer = random.randint(1, upper)
  print(f'guess the number between 0 : {upper}')
  # print(answer)  
  guess = 0
  attempts= 1  
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")   
    guess = int(input("I have a hidden number, guess it "))    
    turns , attempts  = check_answer(guess, answer, turns , attempts )
    if turns == 0:
      print("You've run out of guesses, you lose.")
      break
    elif guess != answer:
      print("Guess again.")




game()