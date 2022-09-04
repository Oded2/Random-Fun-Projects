import random
difficulty = input('Easy, medium, or hard. Easy is a random between 1 - 10, medium 1 - 100, hard, 1 - 1000. Press E for easy, M for medium, H for hard. ').lower()
while difficulty != 'h' and difficulty != 'm' and difficulty != 'e':
      difficulty = input('Error: please enter H for hard, M for medium, E for easy. ')
if difficulty == 'e':
      max_num = 10
      score = 5
      mode = 'easy'
if difficulty == 'm':
      max_num = 100
      score = 25
      mode = 'medium'
if difficulty == 'h':
      max_num = 1000
      score = 35
      mode = 'hard'

score = int(score)
num = random.randint(0,max_num)
tries = 1
user_input = input(f'Welcome to the number guessing game. You chose {mode} difficulty, so you will get a number from 0 to {max_num:,}, with {score} attempts. Please put in your first guess, and good luck! ')
while 7 == 7:
      try:
            user_num = int(user_input)
            break
      except ValueError:
            user_input = input('Error: input is not a number, please input a number ')
while user_num != num:
      score = score - 1
      tries = tries + 1
      if user_num < num:
            user_input = input(f'{user_num} is too low, {score} attempts left. ')
            while 7 == 7:
                  try:
                        user_num = int(user_input)
                        break
                  except ValueError:
                        user_input = input('Error: input is not a number, please input a number ')
      if user_num > num:
            user_input = input(f'{user_num} is too high, {score} attempts left ')
            while 7 == 7:
                  try:
                        user_num = int(user_input)
                        break
                  except ValueError:
                        user_input = input('Error: input is not a number, please input a number ')

      if score == 1:
            print(f'You lost. The number was {num}')
            break
if score != 0:
      print(f'You won! The number was {num}! It took you {tries} tries, with {score - 1} attempts remaining')



