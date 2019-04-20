'''
Monopoly board game simulation.

Done:
* Simple simulation
* Jail rule for three time double roll and "GO TO JAIL" square
* Community chest rules (https://monopoly.fandom.com/wiki/Community_Chest)
* Chance rules (https://monopoly.fandom.com/wiki/Chance)
'''

import random
from tqdm import trange
from prob_on_board import draw_prob
from queue import Queue


ITERATION = 1000_000

# Position of special squares on monopoly board (starting count from 1 at GO square)
GO = 1
JAIL = 11
community_chest = [3,18,34]
chance = [8,23,37]

num_of_cards = list(range(1,17))    # 1 to 16 possible cards
random.shuffle(num_of_cards)

# Create community chest card deck (using FIFO queue)
community_chest_cards = Queue()
[community_chest_cards.put(card) for card in num_of_cards]

# Create chance card deck (using FIFO queue)
chance_cards = Queue()
[chance_cards.put(card) for card in num_of_cards]


def two_dice_roll():
    double = False
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    value = dice1 + dice2
    if dice1 == dice2:
        double = True
    return value, double


def print_result(counts, sum_of_counts):
    print(sum_of_counts)
    print(f"Number of iteration: {ITERATION:,}", end="\n\n")
    print("Position | Frequency (%)")
    print("-"*26)
    
    for i, count in enumerate(counts):
        print(f"{i+1:8d} | {(count/sum_of_counts)*100:5.2f}")


def community_chest_move(cur_pos):
    global community_chest_cards
    card = community_chest_cards.get()  # get a card from top of deck
    community_chest_cards.put(card)     # put the card back to bottom of deck

    if card == 1:
        cur_pos = GO
    elif card == 6:
        cur_pos = JAIL
    return cur_pos


def main():
    global chance_cards
    double_dice_count = 0
    counts = [0] * 40
    current_pos = 1

    for _ in trange(ITERATION):
        dice_value, double = two_dice_roll()
        if double:
            double_dice_count += 1
        else:
            double_dice_count = 0

        if double_dice_count == 3:
            current_pos = JAIL
            counts[current_pos-1] += 1
            double_dice_count = 0
            continue

        current_pos = current_pos + dice_value
        if current_pos > 40:
            current_pos -= 40
        
        counts[current_pos-1] += 1

        # Check for Go to jail square
        if current_pos == 31:
            current_pos = JAIL
            counts[current_pos-1] += 1
            continue

        # Check if at community chest
        if current_pos in community_chest:
            new_pos = community_chest_move(current_pos)
            if new_pos != current_pos:
                current_pos = new_pos
                counts[current_pos-1] += 1

        # Check if at Chance
        if current_pos in chance:
            card = chance_cards.get()  # getting the card from top
            chance_cards.put(card)     # putting back the card at bottom
            if card == 1:
                current_pos = GO
                counts[current_pos-1] += 1
            elif card == 2:             # Advance to Illinois Avenue
                current_pos = 25
                counts[current_pos-1] += 1
            elif card == 3:             # Advance to St. Charles Place
                current_pos = 12
                counts[current_pos-1] += 1
            elif card == 4:             # Advance to nearest Utility (assuming no backward movement)
                if current_pos > 13 and current_pos < 30:
                    current_pos = 29
                else:
                    current_pos = 13
                counts[current_pos-1] += 1
            elif card == 5:             # Advance to nearest Railroad (assuming no backward movement)
                if current_pos <= 6 or current_pos > 36:
                    current_pos = 6
                elif current_pos > 6 and current_pos <= 16:
                    current_pos = 16
                elif current_pos > 16 and current_pos <= 25:
                    current_pos = 26
                else:
                    current_pos = 36
                counts[current_pos-1] += 1
            elif card == 8:             # Go Back Three 3 Spaces.
                current_pos -= 3
                if current_pos < 1:
                    current_pos += 40
                counts[current_pos-1] += 1
                # Check again for community chest position
                if current_pos in community_chest:
                    new_pos = community_chest_move(current_pos)
                    if new_pos != current_pos:
                        current_pos = new_pos
                        counts[current_pos-1] += 1
            elif card == 9:
                current_pos = JAIL
                counts[current_pos-1] += 1
            elif card == 12:             # Take a trip to Reading Railroad.
                current_pos = 6
                counts[current_pos-1] += 1
            elif card == 13:             # Advance token to Boardwalk.
                current_pos = 40
                counts[current_pos-1] += 1

    return counts


if __name__=="__main__":
    counts = main()
    sum_of_counts = sum(counts)
    print_result(counts, sum_of_counts)
    prob = [(num/sum_of_counts)*100 for num in counts]
    file_name = f"{__file__.split('.')[0]}.jpg"
    draw_prob(prob, file_name=file_name)
