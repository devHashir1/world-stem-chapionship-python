# Rock, Paper, Scissor


Player1 = None
Player2 = None
playing = True

def Game():
    global Player1, Player2, option, playing
    
    
    Player1 = input("Player 1:Enter rock, paper or scissor or exit: ")
    Player2 = input("Player 2:Enter rock, paper or scissor or exit: ")

    option = ("rock", "paper", "scissor", "exit")

    while Player1 not in option or Player2 not in option:
        if Player1 not in option:
            print("Invalid input by player 1")
            Player1 = input("Player 1: Enter rock, paper or scissor or exit: ")
        else:
            print("Invalid input by player 2")
            Player2 = input("Player 2: Enter rock, paper or scissor or exit: ")

    if (Player1 == "rock" and Player2 == "paper") or \
       (Player1 == "scissor" and Player2 == "rock") or \
       (Player1 == "paper" and Player2 == "scissor"):
        print("Player 2 win")

    elif Player1 == 'exit' or Player2 == 'exit':
        playing = False
    else:
        print("Player 1 Win")

while playing:
  Game()