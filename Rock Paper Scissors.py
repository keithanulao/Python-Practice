import random 

#Player Name
Name = str(input('Enter Player Name:'))

#Choice Phase
choice_list = ['rock', 'paper', 'scissors']

# Counter variables
wins = 0
losses = 0
ties = 0

while True:
    while True:
        player = str(input("Rock, Paper or Scissors or type 'exit' to exit: ")).replace(' ', '').lower()
        if player == 'exit' or player in choice_list:
            break
        else:
            print("Invalid input. Please enter 'rock', 'paper', 'scissors', or 'exit'.")
  
    if player == 'exit':
        break

    print()
    randy = random.choice(choice_list)
    print('CPU:', randy)
    print(Name,':', player)
    print()

    #this is the key list for the game
    if randy == 'rock':
        randy = 0
    elif randy == 'paper':
        randy =  1
    elif randy == 'scissors':
        randy = 2
    if player == 'rock':
        player = 0
    elif player == 'paper':
        player =  1
    elif player == 'scissors':
        player = 2

    #Battle Phase
    if randy - player == 0:
        print('Tie')
        ties += 1
    elif randy - player == -1 or randy - player == 2:
        print(Name, ' Win')
        wins += 1
    else:
        print(Name, ' Loss')
        losses += 1

    print()

print()
print("Game Over.")
print("Wins:", wins, "Losses:", losses, "Ties:", ties)
print()
