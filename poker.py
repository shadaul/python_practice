import random


# Список рангов карт
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# Список мастей
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

karty = []

for num in ranks:
    for suit in suits:
        karty.append((num,suit))


# print(karty)

# вводился какая игра холдем или омаха, и колество игроков и если игра холдем то игрокам по 2е карты а если омаха то по 4


#flop : 3 карты 
#turn : 1 карта 
#river : 1 karta

# poker("Omaha", "Yura", "Daulet")

# summa_of_gamers = int(input("Введите количество игроков: "))
# type_of_game = int(input("какой тип повера хотите сыгарть: Омаха(1) или Холдем(2)"))




# проверка Типа игры и количесва игроков
def type_user(type_of_game:str, *players) -> list[str, list] | None:

    if not type_of_game in ("Omaha", "Holdem"):
        print("not valid game")
        return 
    
    if not (2 <= len(players) <= 10):
        print("not valid amount")
        return
    
    return [type_of_game, list(players)]


# x = type_user("Omaha", "Yury", "Daulet", "Sophia") #['Omaha', ['Yury', 'Daulet', 'sophia']]

# x[0]

#берется тип игры и имена игроков и Yury: [('2', 'Hearts'), ('2', 'Diamonds')]

def razdacha(data: list, kolody:list):
    
    if not isinstance(data, list):
        return 
    if data[0] == "Omaha":
        for i in data[1]:
            karty = random.choice(karty)
    
        
    


