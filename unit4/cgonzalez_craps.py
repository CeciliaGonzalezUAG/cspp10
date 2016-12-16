import random

#function name
#purpose
    #print
#argument
#return

#current_amount
#to keep track and update the amount after a move, round, or bet
#bet_amount
#the current amount
my_total=100
bet=int(input("Place a bet under your current total:"))
def bet_amount(bet):
    if bet>my_total:
        print ("Please place affordable bet")
    return bet;
rounds=int(input("How many rounds would you like to play?: "))
def get_rounds(rounds):
    return rounds;

dice1=random.randint(1,6)
dice2=random.randint(1,6)
    
def roll_dice(dice1,dice2):
    roll1=dice1+dice2
    print roll1;
    
def game_winner(roll,my_total,bet):
    if roll==7 or roll==11:
        my_total=bet+my_total
        print("You win!")
    elif roll==2 or roll==3 or roll==12:
        my_total=my_total-bet
        print("You Lose!")
    else:
        point_number=roll
        dice3=random.randint(1,6)
        dice4=random.randint(1,6)
        roll2=dice3+dice4
        return roll2;

def  point_round(point_number,roll2,my_total,bet):
    for point_number in range(point_number):
        if roll2==point_number:
            my_total=my_total+bet
            print("You win")
        elif roll2==7:
            my_total=my_total-bet
            print("You lose")
        else:
            return point_number;
        
        
    
    
#to roll out 2 numbers to know whats the amount, set point, loss, or win
#no argument
#return dice numbers

#bet_amount
#keeps track of the current amount and updates after each bet was made.
#no argument
#return amount that is currently 


