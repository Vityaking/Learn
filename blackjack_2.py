from random import shuffle


class Card:
    def __init__(self, _type):
        self.type = _type


class Player:
    def __init__(self, name):
        self.name = name


class BlackJackService:
    def __init__(self):
        self.players = []
        self.hands = {}
        self.deck = []
        for _ in range(4):                              # using 4 decks
            self.deck.append([Card("2")]*4)
            self.deck.append([Card("3")]*4)
            self.deck.append([Card("4")]*4)
            self.deck.append([Card("5")]*4)
            self.deck.append([Card("6")]*4)
            self.deck.append([Card("7")]*4)
            self.deck.append([Card("8")]*4)
            self.deck.append([Card("9")]*4)
            self.deck.append([Card("10")]*4)
            self.deck.append([Card("jack")]*4)
            self.deck.append([Card("queen")]*4)
            self.deck.append([Card("king")]*4)
            self.deck.append([Card("ace")]*4) 
        shuffle(self.deck)


    def add_player(self, player):
        self.players.append(player)
        self.hands[player] = []


    def deal(self):
        for player in self.players:
            card1 = self.deck.pop()
            card2 = self.deck.pop()
            self.hands[player] = [card1, card2]


    def stop(self, player):
        pass


def main():
    service = BlackJackService()
    player1 = Player("Alex")
    service.add_player(player1)
    service.deal()

    while(True):
        in_str = input('q to quit, [stop|double|new]')
        if in_str == 'q':
            print('Bye!')
            exit()
        elif in_str == 'stop':
            service.stop(player1)
        elif in_str == 'double':
            service.double(player1)
        elif in_str == 'new':
            service.new(player1)


if __name__ == '__main__':
    main()
