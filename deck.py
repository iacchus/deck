#!/usr/bin/env python3

# https://en.wikipedia.org/wiki/Standard_52-card_deck
# https://en.wikipedia.org/wiki/Thoth_tarot_deck

"""deck module."""

SUITS = ('wands', 'swords', 'cups', 'disks')
COURT_CARDS = ('knight', 'queen', 'prince', 'princess')
NUMBERED_CARDS = ('ace', '2', '3', '4', '5', '6', '7', '8', '9', '10')
CARDS = COURT_CARDS + NUMBERED_CARDS


class Suit:
    """Suit.
    """


    def __init__(self, suit: str):
        """__init__.

        Args:
            suit (str): suit
        """

        if suit in SUITS:
            self.name = suit
        else:
            raise Exception('Invalid suit \'{}\''.format(suit))

    @property
    def value(self):
        """value.
        """

        return SUITS.index(self.name) + 1


class Card:
    """Card.
    """


    def __init__(self, card: str):
        """__init__.

        Args:
            card (str): card
        """

        if card in CARDS:
            self.name = card
        else:
            raise Exception('Invalid card \'{}\''.format(card))

    @property
    def value(self):
        """value.
        """
        return CARDS.index(self.name) + 1


class DeckCard:
    """DeckCard.
    """


    def __init__(self, card, suit):
        """__init__.

        Args:
            card:
            suit:
        """

        self.card = Card(card)
        self.suit = Suit(suit)

        format_payload = {
            'card': self.card.name.capitalize(),
            'suit': self.suit.name.capitalize()
                }
        self.name = "{card} of {suit}".format(**format_payload)

    @property
    def value(self):
        """value.
        """
        return self.suit.value * self.card.value

    def __int__(self):
        """__int__.
        """

        return self.value

    def __repr__(self):
        """__repr__.
        """

        payload = {'name': self.name, 'value': self.value}
        return "<DeckCard {name} (numeric value {value})>".format(**payload)


class Deck:
    """Deck.
    """


    def __init__(self):
        """__init__.
        """
        #self.cards = [DeckCard(card, suit) for card in CARDS for suit in SUITS]
        self.cards = \
            {
                (suit.value*card.value): DeckCard(card.name, suit.name)
                for card, suit in  [(Card(card), Suit(suit))
                                    for suit in SUITS for card in CARDS]
            }


if __name__ == "__main__":

    a = Deck()

    import pprint
    pprint.pprint(a.cards)
