import logging

logging.basicConfig(filename="Testing_War.log", level=logging.INFO)

from card_deck import *

order = ('2', '3', '4', '5', '6', '8', '9', 'T', 'J', 'Q', 'K', '7', 'A')


class Player:
    def __init__(self, deck, *args, **kwargs):
        self.deck = deck
        self.stash = []
        self.war_stash = []


def game_set_up():
    deck = deck_creator()
    p1, p2 = deal(deck)
    shuffle(p1)
    shuffle(p2)
    return Player(p1), Player(p2)


def game_loop(rounds, turns=1):
    game_loop.turns = turns
    while game_loop.turns <= rounds:
        turn = f"The current turn count is {game_loop.turns}"
        logging.info(turn)
        one_vs_two()
        game_loop.turns += 1
    else:
        result1 = result(p_one)
        result2 = result(p_two)
        if result1 > result2:
            winner = f"The winner is Player1 with {result1} cards & Player 2 loses with {result2}\n"
            status = f"{len(p_one.deck)}:deck size\n{len(p_one.stash)}:stash size"
            logging.info(winner)
            logging.info(status)

        elif result2 > result1:
            winner = f"The winner is Player2 with {result2}  cards & Player 1 loses with {result1}\n"
            status = f"{len(p_two.deck)}:deck size\n{len(p_one.stash)}:stash size"

        else:
            logging.info("It's a tie")


def one_vs_two():
    card1 = []
    card2 = []
    if len(p_one.deck) > 0 and len(p_two.deck) > 0:
        card1 = p_one.deck.pop(0)
        card2 = p_two.deck.pop(0)
        evaluate(card1, card2)
    else:
        resupply()
        one_vs_two()


def evaluate(card1, card2):
    if order.index(card1[0]) > order.index(card2[0]):
        winner = f"Player1 wins: {card1} > {card2}"
        logging.info(winner)
        p_one.stash += [card1, card2]
        stash_win(p_one)
    elif order.index(card2[0]) > order.index(card1[0]):
        winner = f"Player2 wins: {card2} > {card1}"
        logging.info(winner)
        p_two.stash += [card1, card2]
        stash_win(p_two)
    else:
        stash = [card1, card2]
        same_card = f"{card1} is the same as {card2}"
        logging.warning(same_card)
        logging.warning("This means war!!!")
        war(stash)


def result(self):
    total = len(self.deck) + len(self.stash)
    return total


def war(stash):
    try:
        p_one.war_stash += [p_one.deck.pop(0) for _ in range(3)]
        p_two.war_stash += [p_two.deck.pop(0) for _ in range(3)]
        stash_for_grabs = f"Player one is putting the following up for grabs:{p_one.war_stash}\nPlayer two is putting the following up for grabs:{p_two.war_stash}"
        logging.warning(stash_for_grabs)
        one_vs_two()
    except IndexError:
        logging.info("Players are resupplying")
        resupply()
        war(stash)


def stash_win(player):
    if len(p_one.war_stash) > 0 or len(p_two.war_stash) > 0:
        player.stash += [p_one.war_stash.pop()
                         for _ in range(len(p_one.war_stash))] + [p_two.war_stash.pop() for _ in range(len(p_two.war_stash))]


def resupply():
    if p_one.stash == 0:
        game_loop.turns = 100
    elif p_two.stash == 0:
        game_loop.turns = 100
    else:
        card_pop(p_one.stash, p_one.deck)
        card_pop(p_two.stash, p_two.deck)


def card_pop(stash, target):
    target += [stash.pop() for _ in range(len(stash))]


p_one, p_two = game_set_up()
rounds = int(input("How many rounds would you like to play?: "))
round_info = f"{rounds} have been decided to be played"
logging.info(round_info)
game_loop(rounds)
