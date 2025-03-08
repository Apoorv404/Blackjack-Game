from art import logo
from random import choice

def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)

def calculate_score(player):
    """Calculate the score of user or computer."""
    if 10 in player and 11 in player:
        return  0
    if 11 in player and sum(player) > 21:
        player.remove(11)
        player.append(1)
    return sum(player)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "You won with a Blackjack 😎"
    elif u_score > 21:
        return "You went over, you lose 😭"
    elif c_score > 21:
        return "Opponent went over, you win 😁"
    elif u_score > c_score:
        return "You won 😃"
    else:
        return "You lose 😤"

def play_game():
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    should_continue = True
    print(logo)

    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

    while should_continue:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            should_continue = False
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                should_continue = False


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
