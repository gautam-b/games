from random import choice
from tqdm import trange
from collections import Counter
import re


def main():
    n_coin_toss = 1000_000
    result = simulate(n_coin_toss)
    counts = Counter(result)
    head_pct = counts['H'] / n_coin_toss
    print(f'Number of coin toss: {n_coin_toss}')
    print(f'Head %: {head_pct:.1%}')

    sequence = "".join(result)
    for i in range(3, 10):
        n_heads = 'H' * i
        n_consecutive_head = get_n_consecutive_head(n_heads, sequence)
        print(f'Num of {i} consecutive head occurs {n_consecutive_head} time with percantage occurrence of {n_consecutive_head / n_coin_toss:.1%}')


def get_n_consecutive_head(pattern, text):
    return len(re.findall(pattern, text))


def coin_toss():
    return choice(['H', 'T'])


def simulate(n_coin_toss):
    return [coin_toss() for _ in trange(n_coin_toss)]


if __name__ == "__main__":
    main()