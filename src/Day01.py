from pathlib import Path
import pandas as pd

if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        food = {i: list(map(int, x.split('\n'))) for i, x in enumerate(f.read().split('\n\n'))}

    result = max(sum(v) for v in food.values())
    print(f"The result of first star is {result}")

    result = sum(sorted(sum(v) for v in food.values())[-3:])
    print(f"The result of second star is {result}")