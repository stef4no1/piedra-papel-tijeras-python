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

game_images = [rock, paper, scissors]

user_choice = int(input("Que elegis? Pone 0 para elegir piedra, 1 para elegir papel y 2 para elegir tijeras. \n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("La computadora elige:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
  print("Pusiste un número invalido, perdiste!")
elif user_choice == 0 and computer_choice == 2:
  print("Ganaste!")
elif computer_choice == 0 and user_choice == 2:
  print("Perdiste!")
elif computer_choice > user_choice:
  print("Perdiste!")
elif user_choice > computer_choice:
  print("Ganaste!")
elif computer_choice == user_choice:
  print("Es un empate")
