from pathlib import Path
import numpy as np
import pandas as pd
import re

if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        stacks, moves = f.read().split('\n\n')
        
    rule = r'move (\d+) from (\d+) to (\d+)'
    
    moves = [map(int, re.fullmatch(rule, m).groups()) for m in moves.split('\n')]
    caisses = np.array(list(map(list, stacks.split('\n')[:-1])))
    caisses = np.rot90(caisses)
    stacks = {}
    stacks_bis = {}
    for i, line in enumerate(caisses[1::4]):
        stacks[caisses.shape[0] // 4 - i + 1] = list(np.delete(line, np.where(line==' ')))[::-1]
        stacks_bis[caisses.shape[0] // 4 - i + 1] = list(np.delete(line, np.where(line==' ')))[::-1]
        
    for nb_caisses, start, end in moves:
        for i in range(nb_caisses):
            caisse = stacks[start].pop()
            stacks[end].append(caisse)
            
        caisses_moved = [stacks_bis[start].pop() for _ in range(nb_caisses)]
        stacks_bis[end].extend(caisses_moved[::-1])
        
    print(f"The result of first star is {''.join(stacks[i+1][-1] for i in range(len(stacks)))}")        
    print(f"The result of second star is {''.join(stacks_bis[i+1][-1] for i in range(len(stacks_bis)))}")