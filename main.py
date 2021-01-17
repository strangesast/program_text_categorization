import csv
import json
from collections import defaultdict
import pathlib
import difflib

root = pathlib.Path('files')
if not root.is_dir():
    root.mkdir()

with open('program_comparison_big.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    #v = [p[2] for p in reader]

    data = defaultdict(dict)
    for part_num, _hash, program in reader:
        data[part_num][_hash] = program

#print([len(vv) for vv in v])

#d = {a: dict((b, 0) for b in h) for a in h}


output = {}
for part_num, o in data.items():
    hashes = o.keys()
    l = len(hashes)
    print(f'{l} {part_num}')
    d = {h: {h: 0.0 for h in hashes} for h in hashes}
    #list(list(0 for _ in range(l)) for _ in range(l))
    
    matcher = difflib.SequenceMatcher()
    for a in hashes:
        matcher.set_seq1(o[a])
        for b in hashes:
            matcher.set_seq2(o[b])
            r = matcher.ratio()
            d[a][b] = r
    output[part_num] = d



with open('output.json', 'w') as f:
    json.dump(output, f)

    '''
    for a, b in ((a, b) for a in v for b in v):
        d[a[1]][b[1]] = 1
    '''

    '''
    for part_num, _hash, program in reader:
        print(repr(program))
        break
        with open(root / f'{_hash}', 'w') as f:
            f.write(program)
    '''
