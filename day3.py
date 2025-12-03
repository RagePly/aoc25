from typing import Any
from collections import Counter, defaultdict
from itertools import combinations
from re import match, findall

def part1(src: str) -> Any:
    s = 0
    for line in src.splitlines():
        m = 0
        for i in range(len(line)-1):
            for j in range(i+1, len(line)):
                n = int(line[i] + line[j])
                m = max(n, m)
        s += m
    return s

def part2(src: str) -> Any:
    s = 0
    for line in src.splitlines():
        cs = []
        j = 0
        for i in range(12):
            l = len(line[j:]) - (12 - i - 1)
            sub = line[j:j+l]
            mi, c = max(enumerate(sub), key=lambda p: (p[1], -p[0]))
            j += mi + 1
            cs.append(c)
        s += int("".join(cs))
    return s
