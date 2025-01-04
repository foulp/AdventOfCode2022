from pathlib import Path
import pandas as pd

scores = {'X': 1, 'Y': 2, 'Z': 3}
corres = {'A': 'X', 'B': 'Y', 'C': 'Z'}
lose = {'X': 'Z', 'Y': 'X', 'Z': 'Y'}
win = {'X': 'Y', 'Y': 'Z', 'Z': 'X'}

if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        plays = pd.DataFrame((play.split() for play in f.read().split('\n')), columns=['a', 'b'])

    plays['c'] = plays['a'].replace(corres)
    plays['win'] = 3 * (plays['c'] == plays['b']) + 6 * ( ((plays['c']=='X') & (plays['b']=='Y')) | ((plays['c']=='Y') & (plays['b']=='Z')) | ((plays['c']=='Z') & (plays['b']=='X')) )
    plays['score'] = plays['b'].replace(scores)
    print(f"The result of first star is {plays['win'].sum() + plays['score'].sum()}")

    plays['d'] = plays.apply(lambda x: {'X': lose[x['c']], 'Y': x['c'], 'Z': win[x['c']]}[x['b']], axis=1)
    plays['win'] = 3 * (plays['c'] == plays['d']) + 6 * ( ((plays['c']=='X') & (plays['d']=='Y')) | ((plays['c']=='Y') & (plays['d']=='Z')) | ((plays['c']=='Z') & (plays['d']=='X')) )
    plays['score'] = plays['d'].replace(scores)
    print(f"The result of second star is {plays['win'].sum() + plays['score'].sum()}")