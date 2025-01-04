from collections import Counter
from pathlib import Path
import pandas as pd

if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        rucksacks = f.read().split('\n')
        
    priorities = 0
    for r in rucksacks:
        unique = list(set(r[:len(r)//2])) + list(set(r[len(r)//2:]))
        mc = Counter(unique).most_common(1)[0][0]
        if mc.islower():
            priorities += ord(mc) - ord('a') + 1
        else:
            priorities += ord(mc) - ord('A') + 27            
    print(f"The result of first star is {priorities}")

    priorities = 0
    for i in range(0, len(rucksacks), 3):
        unique = list(set(rucksacks[i])) + list(set(rucksacks[i+1])) + list(set(rucksacks[i+2]))
        mc = Counter(unique).most_common(1)[0][0]
        if mc.islower():
            priorities += ord(mc) - ord('a') + 1
        else:
            priorities += ord(mc) - ord('A') + 27      
    print(f"The result of second star is {priorities}")