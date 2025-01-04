from pathlib import Path
import numpy as np
import pandas as pd
import re


def subroutine(s, size=4):
    value = next(i for i in range(size, len(s)) if len(set(s[i-size:i])) == size )
    return value
    
    
if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        stream = f.read()
        
    assert subroutine('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7
    assert subroutine('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
    assert subroutine('nppdvjthqldpwncqszvftbrmjlhg') == 6
    assert subroutine('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
    assert subroutine('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11
    
    print(f"The result of first star is {subroutine(stream)}")   

    assert subroutine('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14) == 19
    assert subroutine('bvwbjplbgvbhsrlpgdmjqwftvncz', 14) == 23
    assert subroutine('nppdvjthqldpwncqszvftbrmjlhg', 14) == 23
    assert subroutine('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14) == 29
    assert subroutine('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14) == 26
    
    print(f"The result of second star is {subroutine(stream, 14)}")