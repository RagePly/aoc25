from typing import Any
from collections import Counter, defaultdict
from itertools import combinations
from re import match, findall

def part1(src: str) -> Any:
    s = 0
    splitters: set[tuple[int, int]] = set()
    liquid: set[tuple[int, int]] = set()
    maxy = 0
    for y, line in enumerate(src.splitlines()):
        for x, c in enumerate(line):
            if c == "^":
                splitters.add((x, y))
            elif c == "S":
                liquid.add((x, y))
        maxy = y
    
    while True:
        new_liquid: set[tuple[int, int]] = set()
        for x, y in liquid:
            if y == maxy + 1:
                return s
            if (x, y+1) in splitters:
                s += 1
                new_liquid.add((x-1, y+1))
                new_liquid.add((x+1, y+1))
            else:
                new_liquid.add((x, y+1))
        liquid = new_liquid

def part2(src: str) -> Any:
    splitters: set[tuple[int, int]] = set()
    liquid: dict[tuple[int, int], int] = {}
    maxy = 0
    for y, line in enumerate(src.splitlines()):
        for x, c in enumerate(line):
            if c == "^":
                splitters.add((x, y))
            elif c == "S":
                liquid[x, y] = 1
        maxy = y
    
    while True:
        new_liquid: dict[tuple[int, int], int] = {}

        for (x, y), t in liquid.items():
            if y == maxy + 1:
                return sum(liquid.values())
            if (x, y+1) in splitters:
                if (x-1, y+1) in new_liquid:
                    new_liquid[x-1, y+1] += t
                else:
                    new_liquid[x-1, y+1] = t
                if (x+1, y+1) in new_liquid:
                    new_liquid[x+1, y+1] += t
                else:
                    new_liquid[x+1, y+1] = t
            else:
                if (x, y+1) in new_liquid:
                    new_liquid[x, y+1] += t
                else:
                    new_liquid[x, y+1] = t
        liquid = new_liquid
