import random
logo = """    ____     _   _ U _____ u ____    ____          _____    _   _  U _____ u      _   _       _   _   __  __     ____  U _____ u   ____      _    
U /"___|uU |"|u| |\| ___"|// __"| u/ __"| u      |_ " _|  |'| |'| \| ___"|/     | \ |"|   U |"|u| |U|' \/ '|uU | __")u\| ___"|/U |  _"\ u U|"|u  
\| |  _ / \| |\| | |  _|" <\___ \/<\___ \/         | |   /| |_| |\ |  _|"      <|  \| |>   \| |\| |\| |\/| |/ \|  _ \/ |  _|"   \| |_) |/ \| |/  
 | |_| |   | |_| | | |___  u___) | u___) |        /| |\  U|  _  |u | |___      U| |\  |u    | |_| | | |  | |   | |_) | | |___    |  _ <    |_|   
  \____|  <<\___/  |_____| |____/>>|____/>>      u |_|U   |_| |_|  |_____|      |_| \_|    <<\___/  |_|  |_|   |____/  |_____|   |_| \_\   (_)   
  _)(|_  (__) )(   <<   >>  )(  (__))(  (__)     _// \\_  //   \\  <<   >>      ||   \\,-.(__) )(  <<,-,,-.   _|| \\_  <<   >>   //   \\_  |||_  
 (__)__)     (__) (__) (__)(__)    (__)         (__) (__)(_") ("_)(__) (__)     (_")  (_/     (__)  (./  \.) (__) (__)(__) (__) (__)  (__)(__)_) 

"""
print (logo)


print("Welcome!to the number Guessing Game!")
print("I'm thinking of a number between 1 and 100")



NUMBER_OF_ATTEMPTS=0
inputs = []
difficulty =  input("Choose a difficulty.Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    NUMBER_OF_ATTEMPTS = 10
else:
    NUMBER_OF_ATTEMPTS = 5
GUESSED_NUMBER = random.randint(0,100)

def guess():
    global NUMBER_OF_ATTEMPTS
    print (f"You have {NUMBER_OF_ATTEMPTS} remaining to guess the number")
    play = True
    while play:
     user_input= int(input("Make a guess:"))

     if user_input != GUESSED_NUMBER :
        NUMBER_OF_ATTEMPTS -= 1
        if user_input>GUESSED_NUMBER:
            print("Too high!")
        elif user_input<GUESSED_NUMBER:
            print("Too low!")
        print(f"You have {NUMBER_OF_ATTEMPTS} remaining to guess the number")
        if NUMBER_OF_ATTEMPTS == 0:
             print(f"Game over! You've run out of attempts. The correct number was {GUESSED_NUMBER}.")
             play = False

     if user_input == GUESSED_NUMBER :
       play = False
       print("Wow!,You guessed the Correct Number!")






guess()
