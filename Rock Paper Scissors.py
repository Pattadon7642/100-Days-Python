import random

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

list_input = [rock, paper, scissors]
player_choose = int(input(f'What do you choose? Type 0 for ock, 1 for Paper or 2 for Scisscors.\n'))
if player_choose == 0:
    print(rock)
elif player_choose == 1:
    print(paper)
elif player_choose == 2:
    print(scissors)
print('Computer choose:')
computer_choose = random.randint(0,len(list_input)-1)
if computer_choose == 0:
    print(rock)
elif computer_choose == 1:
    print(paper)
elif computer_choose == 2:
    print(scissors)

if computer_choose > player_choose:
    print('Computer win!!!')
elif computer_choose == player_choose:
    print('Draw')
else:
    print('Player win!!!')