import random

def play(player1, player2, num_games, verbose=False):
    p1_score = 0
    p2_score = 0
    p1_last = ""
    p2_last = ""

    for i in range(num_games):
        p1_move = player1(p2_last)
        p2_move = player2(p1_last)

        if verbose:
            print(f"Round {i+1}: Player 1 -> {p1_move} | Player 2 -> {p2_move}")

        if beats(p1_move, p2_move):
            p1_score += 1
        elif beats(p2_move, p1_move):
            p2_score += 1

        p1_last = p1_move
        p2_last = p2_move

    print(f"Final Score — Player 1: {p1_score} | Player 2: {p2_score}")
    print(f"Win Rate: {round((p1_score / num_games) * 100, 2)}%")

def beats(a, b):
    return (a == "R" and b == "S") or (a == "S" and b == "P") or (a == "P" and b == "R")

# Four sample bots
def quincy(prev_play):
    if not hasattr(quincy, "index"):
        quincy.index = 0
    moves = ["R", "P", "S"]
    move = moves[quincy.index]
    quincy.index = (quincy.index + 1) % 3
    return move

def abbey(prev_play):
    return random.choice(["R", "P", "S"])

def kris(prev_play):
    return "P"

def mrugesh(prev_play):
    return "S"
