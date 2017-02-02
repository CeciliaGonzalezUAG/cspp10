import random
#function name: get_p1_move
#   arguments: none
#   purpose: present player with options, use input() to get player move
#   returns: the player's move as either 'r', 'p', or 's'
def get_p1_move():
    #code 
    person = input("1 = Paper \n2 = Rock \n3 = Scissors \n PLease Enter a number from 1-3: ")
    if person == '1':
        return 'p'
    elif person == '2':
        return 'r'
    elif person == '3':
        return 's'
#function name: get_comp_move():
#   arguments: none
#   purpose: randomly generates the computer's move,
#            either 'r' 'p' or 's'
#   returns: the computer's randomly generated move
def get_comp_move(): 
    #code here
    computer=random.randint(1,3)
    if computer ==1:
        return 'r'
    elif computer ==2:
        return 'p'
    elif computer ==3:
        return 's'
    
#function name: get_rounds
#   arguments: none
#   purpose: allows the user to choose a number of rounds from 1 to 9.
#   returns: the user-chosen number of rounds
def get_rounds():
    #code here
    rounds= input("How many rounds from 1-9?: ")
    return int(rounds)
#function name: get_round_winner
#   arguments: player move, computer move
#   purpose: based on the player and computer's move, determine
#            the winner or if it's a tie
#   returns: returns a string based on the following:
#               "player" if player won
#               "comp" if computer won
#               "tie" if it's a tie
def get_round_winner(p1move, cmove):
    #code here
    if p1move=="r" and cmove=="p":
        print("The computer won")
        return "comp"
    elif p1move=="p" and cmove=="s":
        print("The computer won")
        return "comp"
    elif p1move=="s" and cmove=="r":
        print("The computer won")
        return "comp"
    elif cmove=="rock" and p1move=="paper":
        print("The player won")
        return "player"
    elif cmove=="p" and p1move=="s":
        print("The player won")
        return "player"
    elif cmove=="s" and p1move=="r":
        print("The player won")
        return "player"
    elif cmove=="r" and p1move=="r":
        print("tie")
        return "tie"
    elif cmove=="p" and p1move=="p":
        print("Tie")
        return "tie"
    elif cmove=="s" and p1move=="s":
        print("tie")
        return "tie"

#function name: get_full_move
#   arguments: a single letter move 'r','p', or 's'
#   purpose: returns the "full" word of a given move
#   returns: returns a string based on the following:
#               "Rock" if given "r"
#               "Paper" if given "p"
#               "Scissors" if given "s"
def get_full_move(shortmove):
    #code here
    if shortmove == "r":
        return "Rock"
    elif shortmove == "s":
        return "Scissors"
    elif shortmove == "p":
        return "Paper"
#function name: print_score
#   arguments: player score, computer score, number of ties
#   purpose: prints the scoreboard
#   returns: none
def print_score(pscore, cscore, ties):
    print ("Player 1 has {} points\nComputer has {} points\nYou both tied {} times".format(pscore,cscore,ties))

#function name: rps
#   arguments: none
#   purpose: the main game loop.  This should be the longest, using
#               all the other functions to create RPS
#   returns: none
def rps():
    score_player = 0
    score_comp = 0
    ties = 0
    rounds_no = get_rounds()
    for rounds_no in range(rounds_no):
        player_move = get_p1_move()
        comp_move = get_comp_move()
        print(player_move)
        print(comp_move)
        round_winner= get_round_winner(player_move,comp_move)
        print(round_winner)
        if round_winner == "player":
            score_player = score_player + 1
        elif round_winner == "comp":
            score_comp = score_comp + 1
        else:
            ties = ties + 1
        print_score(score_player, score_comp, ties)   
rps()