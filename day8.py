from typing import Any
from collections import Counter, defaultdict
from itertools import combinations
from re import match, findall
from math import sqrt

def part1(src: str) -> Any:
    nodes = []
    for line in src.splitlines():
        x, y, z = map(int, line.split(","))
        nodes.append((x,y,z))
    
    dists: list[tuple[float, tuple[int, int, int], tuple[int, int, int]]] = []

    for (x1,y1,z1), (x2,y2,z2) in combinations(nodes, r=2):
        r = sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
        dists.append((r, (x1,y1,z1), (x2,y2,z2))) 
    dists.sort()

    groups: list[set[tuple[int, int, int]]] = []
    for _, p1, p2 in dists[:1000]:
        has_i1 = False
        has_i2 = False
        i1 = i2 = 0
        for i1 in range(len(groups)):
            if p1 in groups[i1]:
                has_i1 = True
                break
        for i2 in range(len(groups)):
            if p2 in groups[i2]:
                has_i2 = True
                break
        
        if (has_i1 and p2 in groups[i1]) or (has_i2 and p1 in groups[i2]):
            continue

        if has_i1 and has_i2:
            if i1 > i2:
                g1 = groups.pop(i1)
                groups[i2].update(g1)
            else:
                g2 = groups.pop(i2)
                groups[i1].update(g2)
        elif has_i1:
            groups[i1].add(p2)
        elif has_i2:
            groups[i2].add(p1)
        else:
            groups.append(set((p1, p2)))
    a, b, c = sorted((len(g) for g in groups), reverse=True)[:3]
    return a * b * c 

def part2(src: str) -> Any:
    nodes = []
    for line in src.splitlines():
        x, y, z = map(int, line.split(","))
        nodes.append((x,y,z))
    
    dists: list[tuple[float, tuple[int, int, int], tuple[int, int, int]]] = []

    for (x1,y1,z1), (x2,y2,z2) in combinations(nodes, r=2):
        r = sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
        dists.append((r, (x1,y1,z1), (x2,y2,z2))) 
    dists.sort()

    groups: list[set[tuple[int, int, int]]] = []
    for _, p1, p2 in dists:
        has_i1 = False
        has_i2 = False
        i1 = i2 = 0
        for i1 in range(len(groups)):
            if p1 in groups[i1]:
                has_i1 = True
                break
        for i2 in range(len(groups)):
            if p2 in groups[i2]:
                has_i2 = True
                break
        
        if (has_i1 and p2 in groups[i1]) or (has_i2 and p1 in groups[i2]):
            continue

        elif has_i1 and has_i2:
            if i1 > i2:
                g1 = groups.pop(i1)
                groups[i2].update(g1)
            else:
                g2 = groups.pop(i2)
                groups[i1].update(g2)
        elif has_i1:
            groups[i1].add(p2)
        elif has_i2:
            groups[i2].add(p1)
        else:
            groups.append(set((p1, p2)))

        if len(groups) == 1 and len(next(iter(groups))) == len(nodes):
            return p1[0] * p2[0]
 