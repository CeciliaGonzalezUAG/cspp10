import random

bank_account=100

bet=int(input("Place a bet that you have enough for: "))

dice1=random.randint(1,6)
dice2=random.randint(1,6)
roll1=dice1+dice2
print("Your roll is: "+ str(roll1))

def phase_one(roll1):
    if roll1==7 or roll1==11:
        bank_account=bet+bank_account
        print("You win!")
        return "win"
    elif roll1==2 or roll1==3 or roll1==12:
        bank_account=bank_account-bet
        print("You Lose!")
        return "lost"
    else:
        dice3=random.randint(1,6)
        dice4=random.randint(1,6)
        roll2=dice3+dice4
        print("Going to Phase 2")
        return roll2;
    
    
    
