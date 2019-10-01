import random as rand

suits = ['clubs', 'spades', 'hearts', 'diamonds']
numbers = [x for x in range(2, 10)]

face_cards = ["Ace", "Ten", "Jack", "Queen", "King"]
fc_values = [1, 10, 11, 12, 13]


def deck_creator():
    num_deck = [f"{num} of {suit}" for num in numbers for suit in suits]
# Face card Deck
    fc_deck = [f"{fc} of {suit}" for fc in face_cards for suit in suits]
    deck = fc_deck + num_deck
    return deck


def deal(deck):
    player1_deck = []
    player2_deck = []
    for card in deck:
        if "spade" in card or "clubs" in card:
            player1_deck += [card]
        else:
            player2_deck += [card]
    return (player1_deck, player2_deck)


def shuffle(player):
    for _ in range(20):
        rand.shuffle(player)
