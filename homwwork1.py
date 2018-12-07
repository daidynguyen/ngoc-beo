import random
def shuffled_cards():
    result = []
    suits = ("Golden coins", "Goblets", "Swords", "Clubs")
    numbers = list(range(1,8)) + list(range(10,13))

    for suit in suits:
        for number in numbers:
            result.append("%s_%s" % (random.choice(numbers), random.choice(suits)))
    print(result)   
    #return cards
    
def highest_card(cards):
    shuffled_cards()
    cards = result.shuffled_cards
    print("cards:")
    
    for number in cards:
        if number ==1:
            print(highest="card")
        number = number + 1
        
        print(highest)
        

shuffled_cards()
highest_card(cards)
