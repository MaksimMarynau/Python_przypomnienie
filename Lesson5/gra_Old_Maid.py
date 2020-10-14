class Card:
    """Klasa reprezentująca karty do gry"""
    suit_list = ["trefl","karo","kier","pik"]
    rank_list = ["puste","As","2","3","4","5","6","7","8",
                 "9","10","Walet","Dama","Krol",]

    def __init__(self, suit=0, rank=0):
        """Konstruktor karty"""
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Zwroc postac napisowa karty"""
        return f"{Card.rank_list[self.rank]} {Card.suit_list[self.suit]}"
    def __repr__(self):
        """Zwroc reprezentacje napisowa"""
        return f"Card({self.suit}, {self.rank})"
    def __cmp__(self, other):
        """Porownaj karty"""
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1
        #Kolory te same, sprawdzamy numery
        if self.rank > other.rank:
            return 1
        if self.rank < other.rank:
            return -1
        return 0 #remis

class Deck:
    """Klasa reprezentujaca talie"""

    def __init__(self):
        """Stworz cala talie kart"""
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Card(suit,rank))

    def __str__(self):
        """Zwroc postac napisowa talii kart"""
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s

    def shuffle(self):
        """Tasuj talie"""
        import random
        n_cards = len(self.cards)
        for i in range(n_cards):
            j = random.randrange(i, n_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def remove_card(self,card):
        """Unicestwianie karty"""
        if card in self.cards:
            self.cards.remove()
            return True
        else:
            return False

    def pop_card(self):
        """Rozdanie (wydanie na zewnatrz) jednej karty"""
        return self.cards.pop()

    def is_empty(self):
        """Test czy talia jest pusta"""
        return self.cards == []
    def deal(self,hands,n_cards=999):
        """Rozdaj karty do rak"""
        n_hands = len(hands)
        for i in range(n_cards):
            if self.is_empty():
                break
            card = self.pop_card()
            hand = hands[i % n_hands]
            hand.add_card(card)

class Hand(Deck):
    """Klasa reprezentujaca reke gracza"""
    def __init__(self,name=""):
        """Konstruktor reki"""
        self.cards = []
        self.name = name

    def __str__(self):
        """Zwroc postac napisowa reki"""
        s = "Ręka " + self.name
        if self.is_empty():
            s = s + " jest pusta\n"
        else:
            s = s + " zawiera\n"
        return s + Deck.__str__(self)

    def add_card(self,card):
        """Dodanie karty do reki"""
        self.cards.append(card)

class CardGame:
    """Ogolna klasa dla gier karcianych"""

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.hands = []

    def print_hands(self):
        """Wypisz rece graczy"""
        for hand in self.hands:
            print( hand )

class OldMainHand(Hand):

    def remove_matches(self):
        count = 0
        original_cards = self.cards[:]
        for card in original_cards:
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print(f"Ręka {self.name}: {card} tworzy parę z {match}")
                count += 1
        return count

class OldMaidGame(CardGame):

    def play(self,names):
        self.deck.remove_card(Card(0,12))
        for name in names:
            self.hands.append(OldMainHand(name))
        self.deck.deal(self.hands)
        print("---Rozdano karty")
        self.print_hands()
        matches = self.remove_all_matches()
        print("---Pary usunięte, początek gry")
        self.print_hands()
        turn = 0
        n_hands = len(self.hands)
        while matches < 25:
            matches = matches + self.play_one_turn(turn)
            turn = (turn + 1) % n_hands
        print("---Koniec gry")
        self.print_hands()


    def remove_all_matches(self):
        count = 0
        for hand in self.hands:
            count = count + hand.remove_matches()
        return count

    def play_one_turn(self,i):
        if self.hands[i].is_empty(): return 0
        neighbor = self.find_neighbor(i)
        picked_card = self.hands[neighbor].pop_card()
        self.hands[i].add_card(picked_card)
        print("Ręka {} pobiera {}".format(self.hands[i].name, picked_card))
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle()
        return count

    def find_neighbor(self,i):
        n_hands = len(self.hands)
        for next in range(1, n_hands):
            neighbor = (i + next) % n_hands
            if not self.hands[neighbor].is_empty():
                return neighbor

game = OldMaidGame()
game.play(["Adam","Bogdan","Cezary"])
