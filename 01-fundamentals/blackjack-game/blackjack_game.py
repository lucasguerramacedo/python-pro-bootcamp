import random
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "draw"
    elif computer_score == 0:
        return "Table BlackJack you lose"
    elif user_score == 0:
        return "BlackJack you win!"
    elif user_score > 21:
        return "You bust"
    elif computer_score > 21:
        return "Table bust you win!"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"



def play_game():
    print(art.logo)
    game = True
    user_cards = []
    user_score = -1
    computer_cards = []
    computer_score = -1

    for draw in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while game:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\nyour cards are {user_cards} your current score is {user_score}")
        print(f"computer's first card [{computer_cards[0]}]")
        if user_score == 0 or computer_score == 0 or user_score > 21:
             game = False
        else:
            draw = input("\nType 'y' to hit or 'n' to stand ")
            if draw == 'y':
                user_cards.append(deal_card())
            else:
                game = False
    while computer_score != 0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"\nYour final hand {user_cards} final score {user_score}")
    print(f"Table final hand {computer_cards} final score {computer_score}")
    print(compare(user_score, computer_score))

    again = input("\nPress 'y' to play again or 'n' to stop ")
    if again == 'y':
        print("\n" * 20)
        play_game()
play_game()







