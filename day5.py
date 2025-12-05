
from typing import Any
from collections import Counter, defaultdict
from itertools import combinations
from re import match, findall

def part1(src: str) -> Any:
    s = 0
    rss = []
    rs, ing = src.split("\n\n")
    for r in rs.splitlines():
        a, b = map(int, r.split("-"))
        rss.append((a,b))
    
    for i in ing.splitlines():
        ii = int(i)

        for a, b in rss:
            if a <= ii <= b:
                s += 1
                break
    return s

def part2(src: str) -> Any:
    s = 0
    regions = []
    rs, _ = src.split("\n\n")
    for r in rs.splitlines():
        a, b = map(int, r.split("-"))
        while True:
            for i in range(len(regions)):
                aa, bb = regions[i]
                if b < aa - 1:
                    continue
                elif bb + 1 < a:
                    continue
                else:
                    regions.pop(i)
                    a = min(a, aa)
                    b = max(b, bb)
                    break
            else:
                break
        regions.append((a, b))
    for a, b in regions:
        s += b - a + 1
    return s
