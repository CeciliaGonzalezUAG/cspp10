import random

def bet(bank_account):
    if bet>bank_account:
        return "Not enough money"
    elif bet< 0:
        return "You can't bet negative money!"
    elif bet==0:
        return"Place valid amount"

def roll():
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    roll1=dice1+dice2
    print("Your roll is: "+ str(roll1))
    return roll1
    
def phase_one(roll1,point_number,bet,bank_account):
    if roll1==7 or roll1==11:
        bank_account=bet+bank_account
        return "You win"
    elif roll1==2 or roll1==3 or roll1==12:
        bank_account=bank_account-bet
        return "you lose"
    else:
        point_number=roll1
        return roll1


def roll2():
    dice3=random.randint(1,6)
    dice4=random.randint(1,6)
    roll2=dice3+dice4
    print("Your roll is: "+ str(roll2))
    return roll2
    
    
def point_round(point_number,roll2, bank_account,bet,point):
    while roll2 != 7 :
        if roll2== point_number:
            bank_account=bank_account+bet
            return "you win"
        elif roll2==7:
            bank_account=bank_account-bet
            return "House wins"
            
#point_round, phase_one, 

def craps():
    bank_account=100
    bet=int(input("Place a bet that you have enough for: "))
    roll1=roll()
    while  bank_account != 0:
        if bank_account ==0:
            print("No money left, House won")
        elif point_round=="you win":
            print("You win!")
        elif point_round=="House wins":
            print("House wins")
        elif phase_one=="You win":
            print("You win!")
        elif phase_one=="you lose":
            print("House wins!")
    print(bank_account)
craps()