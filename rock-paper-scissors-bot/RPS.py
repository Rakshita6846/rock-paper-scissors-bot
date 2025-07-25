# RPS.py

import random

opponent_history = []

def player(prev_play, opponent_history=opponent_history):
    if prev_play:
        opponent_history.append(prev_play)

    # Always play random move if not enough data
    if len(opponent_history) < 5:
        return random.choice(["R", "P", "S"])

    # Try to find a pattern in the last 3 moves
    pattern = "".join(opponent_history[-3:])
    moves = ["R", "P", "S"]
    pattern_counts = {"R": 0, "P": 0, "S": 0}

    for i in range(len(opponent_history) - 3):
        if "".join(opponent_history[i:i+3]) == pattern:
            next_index = i + 3
            if next_index < len(opponent_history):
                next_move = opponent_history[next_index]
                pattern_counts[next_move] += 1

    # If pattern found, predict the most likely next move
    if sum(pattern_counts.values()) > 0:
        prediction = max(pattern_counts, key=pattern_counts.get)
    else:
        # Fallback to most frequent move
        prediction = max(set(opponent_history), key=opponent_history.count)

    # Counter the predicted move
    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[prediction]

