from itertools import product
from tqdm import tqdm

NUM_OF_DICE = 2

counts = [0] * (NUM_OF_DICE * 6 + 1)

pools = list(product(range(1, 7), repeat=NUM_OF_DICE))
num_of_combitions = len(pools)

for dice_values in tqdm(pools):
    dice_total = sum(dice_values)
    counts[dice_total] += 1

print(f"Total Number of combinations: {num_of_combitions}")
print("Dice Total | Num of ways | Probability(%)")
print("-" * 41)
for i, item in enumerate(counts):
    if item > 0:
        print(f"{i:10d} | {item:11d} |{(item/num_of_combitions)*100:12.2f}")
