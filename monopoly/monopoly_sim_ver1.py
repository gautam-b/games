"""
Monopoly board game simulation.

Steps:
x Simple simulation
- Jail rule for three time double roll
- Incorporate community and chance rules (https://monopoly.fandom.com/wiki/Community_Chest)
"""

import random
from tqdm import trange
from prob_on_board import draw_prob


ITERATION = 10_000
dice = range(1, 7)  # 1 to 6 possible  values


def two_dice_roll():
    return random.choice(dice), random.choice(dice)


def print_result(counts):
    sum_of_counts = sum(counts)
    print(sum_of_counts)
    print(f"Number of iteration: {ITERATION:,}", end="\n\n")
    print("Position | Frequency (%)")
    print("-" * 26)

    for i, count in enumerate(counts):
        print(f"{i+1:8d} | {(count/sum_of_counts)*100:5.2f}")


def main():
    # double_dice_count = 0
    counts = [0] * 40
    current_pos = 1

    for _ in trange(ITERATION):
        dice1, dice2 = two_dice_roll()
        dice_value = dice1 + dice2

        current_pos = current_pos + dice_value
        if current_pos > 40:
            current_pos = current_pos - 40
        counts[current_pos - 1] += 1

    prob = [num / 100 for num in counts]

    return counts


if __name__ == "__main__":
    counts = main()
    print_result(counts)
    sum_of_counts = sum(counts)
    prob = [(num / sum_of_counts) * 100 for num in counts]
    file_name = f"{__file__.split('.')[0]}.jpg"
    draw_prob(prob, file_name=file_name)
