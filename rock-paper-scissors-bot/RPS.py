opponent_moves = []

def player(prev_play, opponent_history=opponent_moves):
    if prev_play != "":
        opponent_history.append(prev_play)

    if len(opponent_history) < 5:
        return "R"

    # Count how often opponent plays each move
    r_count = opponent_history.count("R")
    p_count = opponent_history.count("P")
    s_count = opponent_history.count("S")

    # Check if opponent is random (counts are almost equal)
    total = len(opponent_history)
    r_ratio = r_count / total
    p_ratio = p_count / total
    s_ratio = s_count / total

    if abs(r_ratio - p_ratio) < 0.05 and abs(p_ratio - s_ratio) < 0.05:
        # If they are random, just play smarter than random
        # Most common move they used
        most_common = max({"R": r_count, "P": p_count, "S": s_count}, key=lambda k: {"R": r_count, "P": p_count, "S": s_count}[k])
        return counter_move(most_common)

    # Use pattern matching for other bots
    recent = "".join(opponent_history[-3:])
    pattern_counts = {"R": 0, "P": 0, "S": 0}

    for i in range(len(opponent_history) - 3):
        pattern = "".join(opponent_history[i:i+3])
        if pattern == recent:
            next_move = opponent_history[i+3]
            pattern_counts[next_move] += 1

    if sum(pattern_counts.values()) == 0:
        prediction = opponent_history[-1]
    else:
        prediction = max(pattern_counts, key=pattern_counts.get)

    return counter_move(prediction)

def counter_move(move):
    if move == "R":
        return "P"
    elif move == "P":
        return "S"
    else:
        return "R"
