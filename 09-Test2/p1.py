card = {
    "A": 10,
    "K": 10,
    "Q": 10,
    "J": 10,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "1": 1
    }

def f(player1,player2):
    sum1 = 0
    sum2 = 0
    for i in player1:
        value = card[i]
        sum1 = sum1 + value
    
    for i in player2:
        value = card[i]
        sum2 = sum2 + value
    
    if sum1 > sum2:
        return True
    if sum1 <= sum2:
        return False
    
    


    


