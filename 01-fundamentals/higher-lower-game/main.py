import random
import art
import game_data
def next():
    next_star = random.choice(game_data.data)
    return next_star

def play_game():
    A = []
    B = []
    for draw in range(1):
        A.append(next())
        B.append(next())
        if A == B:
            A.remove(A)
            A.append(draw)
    keep_playing = True
    score = 0

    while keep_playing:
        print(f"{A[0]['name']}, a {A[0]['description']}, from {A[0]['country']}")
        print(art.vs)
        print(f"{B[0]['name']} a {B[0]['description']}, from {B[0]['country']}")
        guess = input("Who has more followers type 'A' or 'B': ").upper()
        if A[0]['follower_count'] > B[0]['follower_count']:
            right_answer = "A"
        else:
            right_answer = "B"
        if guess == right_answer:
            score += 1
            print("\n" * 20)
            print(f"Correct! Your score is {score}")
            A[0] = B[0]
            B[0] = next()
            keep_playing = True
        else:
            print(f"Incorrect! your final score is {score}")
            keep_playing = False

play_game()