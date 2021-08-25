import random
from enum import Enum


class Suit(str, Enum):
    Club = "♣"
    Diamond = "♦"
    Heart = "♥"
    Spade = "♠"


class BlackJackCard():
    def __init__(self, rank: int, suit: Suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.face}{self.suit} (H: {self.hard}; S: {self.soft})"

    @property
    def hard(self):
        if 10 < self.rank < 14:
            return 10
        elif self.rank == 14:
            return 1
        return self.rank

    @property
    def soft(self):
        if 10 < self.rank < 14:
            return 10
        elif self.rank == 14:
            return 11
        return self.rank

    @property
    def face(self):
        if self.rank == 11:
            return 'J'
        elif self.rank == 12:
            return 'Q'
        elif self.rank == 13:
            return 'K'
        elif self.rank == 14:
            return 'A'
        return self.rank


class Deck():
    def __init__(self):
        self._cards = []

        for rank in range(2, 15):
            for suit in iter(Suit):
                card = BlackJackCard(rank, suit)
                self._cards.append(card)

        random.shuffle(self._cards)

    def __str__(self):
        deck_comp = ''
        for card in self._cards:
            deck_comp += card.__str__() + '\n'
        return 'The deck has: \n' + deck_comp

    def pop(self) -> BlackJackCard:
        card = self._cards.pop()
        print(card)
        return card


class Hand:
    def __init__(self, dealer_card: BlackJackCard, *cards: BlackJackCard) -> None:
        self.dealer_card = dealer_card
        self._cards = list(cards)

    def __str__(self):
        return ", ".join(map(str, self._cards))

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"({self.dealer_card!r},"
            f"{', '.join(map(repr, self._cards))})"
        )


class Hand_Lazy(Hand):
    @property
    def total(self) -> int:
        delta_soft = max(c.soft - c.hard for c in self._cards)
        hard_total = sum(c.hard for c in self._cards)

        if hard_total + delta_soft <= 21:
            return hard_total + delta_soft
        return hard_total

    @property
    def card(self):
        return self._cards

    @card.setter
    def card(self, aCard: BlackJackCard) -> None:
        self._cards.append(aCard)

    @card.deleter
    def card(self) -> None:
        self._cards.pop(-1)


if __name__ == '__main__':
    d = Deck()
    # print(d)

    h = Hand_Lazy(d.pop(), d.pop(), d.pop(), d.pop())
    # print(h)
    print(f"Hand: {h.total}")

    # Example result #1:
    # K♦ (H: 10; S: 10)     -> Dealer card
    # A♦ (H: 1; S: 11)      -> Card 1
    # 10♠ (H: 10; S: 10)    -> Card 2
    # 9♣ (H: 9; S: 9)       -> Card 3
    # Hand: 20              -> Total hand score (A is counted as 1)

    # Example result #2:
    # 8♥ (H: 8; S: 8)       -> Dealer card
    # A♠ (H: 1; S: 11)      -> Card 1
    # 3♦ (H: 3; S: 3)       -> Card 2
    # 2♣ (H: 2; S: 2)       -> Card 3
    # Hand: 16              -> Total hand score (A is counted as 11)
