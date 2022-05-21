import random

computer=[]
player=[]

cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,10]

def deal_card(cards):
    return random.choice(cards)

def summ(cards):
    sum=0
    for card in cards:
        sum= sum + card
    return sum

def score(cards):
    if 11 in cards and 10 in cards and len(cards)==2:
        return 0
    if 11 in cards and summ(cards)>21:
        for i in cards:
            if i==11:
                cards.remove(11)
                cards.append(1)
    return summ(cards)   
    
def printt():
    print (f"Computer: {computer}, Player: {player}")
    print (f" Scores:  {score(computer)}, {score(player)}")

def game_not_over():
    if score(computer)==0 or score(player)==0 or score(player)>21:
        print ("Game Over")
        return False
    else: return True
    #else: return False

def compare():
    if score(player)<score(computer):
        print("you win!!")
    elif score(player)==score(computer):
        print("its a draw!!")
    else:
        print("you lost!!")


for _ in  range(2):
    computer.append(deal_card(cards))
    player.append(deal_card(cards))
        
printt()
game=game_not_over()
print (game)

while game:
    response=(input("Do you want to deal? ")).lower()
    if response=="yes":
        player.append(deal_card(cards))
        printt()
        game=game_not_over()
    else:
        if score(computer)<17:
            computer.append(deal_card(cards))
            printt()
        else:
            printt()
            game=False


compare()
#print(score([12,11]))


    
    