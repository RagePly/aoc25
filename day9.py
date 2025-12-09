
from typing import Any
from collections import Counter, defaultdict
from itertools import combinations
from re import match, findall
from math import sqrt

def part1(src: str) -> Any:
    s = 0
    pos = []
    for line in src.splitlines():
        pos.append(tuple(map(int, line.split(","))))
    
    ma = 0
    for (x1, y1), (x2, y2) in combinations(pos, r=2):
        a = (abs(x2-x1) + 1) * (abs(y2- y1) + 1)
        ma = max(ma, a)
    
    return ma

def part2(src: str) -> Any:
    import shapely.geometry
    import shapely
    s = 0
    pos = []
    m = []
    for line in src.splitlines():
        pos.append(tuple(map(int, line.split(","))))
    
    sphere = shapely.geometry.Polygon(pos)

    areas = []
    for i, j in combinations(range(len(pos)), r=2):
        (x1, y1), (x2, y2) = pos[i], pos[j]
        a = (abs(x2-x1) + 1) * (abs(y2 - y1) + 1)
        areas.append((a, i, x1, y1, j, x2, y2))

    areas.sort(reverse=True)

    ii = 0
    for a, i, x1, y1, j, x2, y2 in areas:
        l, r, u, d = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)
        box = shapely.geometry.box(l, u, r, d)
        
        ii += 1
        other = box.intersection(sphere, grid_size=1)
        
        if other.equals(box):
            return a
