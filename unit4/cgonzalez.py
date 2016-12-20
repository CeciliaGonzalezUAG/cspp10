import random

def phase_one(roll1,point_number):
    if roll1==7 or roll1==11:
        bank_account=bet+bank_account
        print("You win!")
        return "win"
    elif roll1==2 or roll1==3 or roll1==12:
        bank_account=bank_account-bet
        print("You Lose!")
        return "lost"
    else:
        point_number=roll1
        return roll1

def point_round(point_number,roll2, bank_account,bet):
    while roll2 != 7 :
        if roll2== point_number:
            bank_account=bank_account+bet
            print("you win")

def roll():
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    roll1=dice1+dice2
    print("Your roll is: "+ str(roll1))
    return roll1
    
bank_account=100

while bank_account != 0:

    bet=int(input("Place a bet that you have enough for: "))

    roll1=roll()
    
    
def craps():
    score_player=0
    score_house=0
    while point_number != 7:
    

        
print(bank_account)
