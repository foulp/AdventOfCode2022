from pathlib import Path

if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        pairs = f.read().split('\n')
        
    pairs = list(map(lambda x: x.split(','), pairs))
    pairs = [ list(zip(range1.split('-'), range2.split('-'))) for range1, range2 in pairs]
    pairs_full_overlap = [ ( (int(starts[0]) <= int(starts[1])) & (int(ends[0]) >= int(ends[1])) ) or ( (int(starts[0]) >= int(starts[1])) & (int(ends[0]) <= int(ends[1])) ) for starts, ends in pairs]
    print(f"The result of first star is {sum(pairs_full_overlap)}")

    pairs_no_overlap = [ (int(ends[0]) < int(starts[1])) or (int(ends[1]) < int(starts[0]))  for starts, ends in pairs]
    print(f"The result of second star is {len(pairs) - sum(pairs_no_overlap)}")