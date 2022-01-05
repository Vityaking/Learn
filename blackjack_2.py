from random import shuffle


class Card:
    def __init__(self, _type):
        self.type = _type   


    def value(self):
        temp = self.type
        try:
            value = int(temp)
        except ValueError:
            if temp == 'ace':
                value = 11
            else: 
                value = 10
        return value

class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


class BlackJackService:
    def __init__(self):
        self.players = []
        self.hands = {}
        self.deck = []
        for _ in range(4):                              # using 4 decks
            self.deck.extend([Card("2")]*4)
            self.deck.extend([Card("3")]*4)
            self.deck.extend([Card("4")]*4)
            self.deck.extend([Card("5")]*4)
            self.deck.extend([Card("6")]*4)
            self.deck.extend([Card("7")]*4)
            self.deck.extend([Card("8")]*4)
            self.deck.extend([Card("9")]*4)
            self.deck.extend([Card("10")]*4)
            self.deck.extend([Card("jack")]*4)
            self.deck.extend([Card("queen")]*4)
            self.deck.extend([Card("king")]*4)
            self.deck.extend([Card("ace")]*4) 
        shuffle(self.deck)
        dealer = Player('dealer', 1000000)
        self.add_player(dealer)
        self.dealer = dealer


    def add_bet(self, bet):
        self.bet = bet


    def add_player(self, player):
        self.players.append(player)
        self.hands[player] = []


    def deal(self):
        self.hands.clear()
        for player in self.players:
            player.balance -= self.bet
            card1 = self.deck.pop()
            card2 = self.deck.pop()
            self.hands[player] = [card1, card2]
            if player.name == 'dealer':
                print(player.name,':', card1.type)
            else:
                print(player.name, ':', card1.type,card2.type)


    def sum(self, player):
        self.player = player
        sum = 0
        cards = []
        cards.extend(self.hands[player])
        if (cards[0] == 'ace' and cards[1].value() == 10) or (cards[0].value() == 10 and cards[0] == 'ace'):
            return 0                                                                                                # 0 means blackjack
        for card in cards:
            sum += card.value()
            pass
        return sum


    def stop(self, player):
        self.player = player
        print(self.player.name, ':')
        for card in self.hands[player]:
            print(card.type, end = ',')
        self._dealer()
        self.end(player)
        

    def double(self, player):
        self.player = player
        if len(self.hands[player]) > 2:
            print('You can\'t double')
            return False
        else:
            self.hands[player].append(self.deck.pop())
            print(player.name, ':', end = ',')
            for card in self.hands[player]:
                print(card.type, end = ',')
            self._dealer()
            self.end(player)
            return True


    def new(self, player):
        self.player = player
        if self.sum(player) > 20:
            print('you can\'t draw more cards')
            return False
        else:
            self.hands[player].append(self.deck.pop())
            print(player.name, ':', end = ',')
            for card in self.hands[player]:
                print(card.type, end = ',')
            return True


    def _dealer(self):
        sum = self.sum(self.dealer)
        while (sum < 16) and (sum < 21):
            self.hands[self.dealer].append(self.deck.pop())
            sum = self.sum(self.dealer)


    def end(self, player):
        self.player = player
        sum = self.sum(player)
        dealerSum = self.sum(self.dealer)
        print('dealer:', end = '')
        for card in self.hands[self.dealer]:
            print(card.type, end = ',')
        if sum == 0:
            print('You have Blackjack')
            player.balance += 2.5 * self.bet
        elif sum > 21:
            print('Too much, you lost. Better luck next time')
        elif sum < 21 and dealerSum > 21:
            print('You won')
            player.balance += 2*self.bet
        elif (sum > dealerSum) and (dealerSum != 0):
            print('You won')
            player.balance += 2*self.bet
        elif sum < dealerSum:
            print('You lost')
        elif sum == dealerSum:
            print('Tie')
            player.balance += self.bet
        else:
            print('pain')
        print(player.name, '\'s balance:', player.balance)


def main():
    service = BlackJackService()
    service.add_bet(200)
    player1 = Player("Alex", 1000)
    player2 = Player("Bob", 1000)
    service.add_player(player1)
    service.add_player(player2)

    while(input('q to quit, anything else to play') != 'q'):
        for player in service.players:
            if player.balance < service.bet:
                print(player.balance)
                name_ = player.name
                print(name_, 'has not enough money to bet. The game is over for them. Bye!')
                service.players.remove(player.name) #### doesn't work as desired
        service.deal()
        restart = False
        while (not restart):
            print(player1.name,'\'s turn:')
            in_str = input('q to quit, [stop|double|new]')
            if in_str == 'q':
                print('Bye!')
                exit()
            elif in_str == 'stop':
                service.stop(player1)
                restart = True
            elif in_str == 'double':
                if service.double(player1):
                    restart = True
            elif in_str == 'new':
                if service.new(player1):
                    print('Sum: ',service.sum(player1))

        restart = False
        while (not restart):
            print(player2.name,'\'s turn:')
            in_str = input('q to quit, [stop|double|new]')
            if in_str == 'q':
                print('Bye!')
                exit()
            elif in_str == 'stop':
                service.stop(player2)
                restart = True
            elif in_str == 'double':
                if service.double(player2):
                    restart = True
            elif in_str == 'new':
                if service.new(player2):
                    print('Sum: ',service.sum(player2))


if __name__ == '__main__':
    main()
