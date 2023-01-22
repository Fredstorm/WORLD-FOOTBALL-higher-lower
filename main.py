#Current Task
#Pick two celebrities and compare them

import random
import os

os.system('clear')

# to make it in a function

def clear():
     os.system('clear')

clear() # class the function

celebrities = {'Cristiano Ronaldo':515, 'Lionel Messi':390, 'Neymar Jr':194, 'Kylian Mbappé':78, 'David Beckham':76, 'Ronaldinho':70, 'Karim Benzema':62, 'Zlatan Ibrahimović':56, 'Sergio Ramos':54, 'Mohamed Salah':53, 'Paulo Dybala':51, 'Gareth Bale':49, 'Luis Suarez':45, 'Andrés Iniesta':41, 'Antoine Griezmann':37, 'Toni Kroos':36, 'Zinedine Zidane':35, 'Robert Lewandowski':31, 'Eden Hazard':27, 'Luka Modric':26}

game_over = False
score = 0
celebrity1_name = random.choice(list(celebrities.keys()))
celebrity1_followers = celebrities.get(celebrity1_name)
celebrity2_name = random.choice(list(celebrities.keys()))
while celebrity2_name == celebrity1_name:
  celebrity2_name = random.choice(list(celebrities.keys()))
celebrity2_followers = celebrities.get(celebrity2_name)

while game_over == False:
  

  print(r"""
    _     _       _                              _                        
   | |   (_)     | |                            | |                       
   | |__  _  __ _| |__   ___ _ __    ___  _ __  | | _____      _____ _ __ 
   | '_ \| |/ _` | '_ \ / _ \ '__|  / _ \| '__| | |/ _ \ \ /\ / / _ \ '__|
   | | | | | (_| | | | |  __/ |    | (_) | |    | | (_) \ V  V /  __/ |   
   |_| |_|_|\__, |_| |_|\___|_|     \___/|_|    |_|\___/ \_/\_/ \___|_|   
             __/ |                                                        
            |___/                                                                        
  """)
  
  print(f"Compare A: {celebrity1_name}.")
  print(r"""  
   __   _____ 
   \ \ / / __|
    \ V /\__ \
     \_/ |___/                        
  """)
  print(f"Against B: {celebrity2_name}.")
  answer = input("Who has more followers? Type 'A' or 'B': ")
  
  if answer == 'A':
    if celebrity1_followers > celebrity2_followers:
      clear()
      print(f"You're right!")
      score += 1
      print(f"Current score: {score}.")
      celebrity2_name = random.choice(list(celebrities.keys()))
      while celebrity2_name == celebrity1_name:
        celebrity2_name = random.choice(list(celebrities.keys()))
      celebrity2_followers = celebrities.get(celebrity2_name)
      if celebrity1_name == 'Cristiano Ronaldo':
        print("You win! Cristiano Ronaldo is the most followed account on Instagram.")
        game_over = True
      
    elif celebrity1_followers < celebrity2_followers:
      clear()
      print("Sorry, that's wrong.")
      print(f"Final score: {score}")
      game_over = True
    
  if answer == 'B':
    if celebrity2_followers > celebrity1_followers:
      clear()
      print(f"You're right!")
      score += 1
      print(f"Current score: {score}.")
      celebrity1_name = celebrity2_name
      celebrity1_followers = celebrities.get(celebrity1_name)
      celebrity2_name = random.choice(list(celebrities.keys()))
      while celebrity2_name == celebrity1_name:
        celebrity2_name = random.choice(list(celebrities.keys()))
      celebrity2_followers = celebrities.get(celebrity2_name)
      if celebrity1_name == 'Cristiano Ronaldo':
        print("You win! Cristiano Ronaldo is the most followed account on Instagram.")
        game_over = True
    elif celebrity2_followers < celebrity1_followers:
      clear()
      print("Sorry, that's wrong.")
      print(f"Final score: {score}")
      game_over = True
