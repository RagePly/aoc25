from typing import Any
from collections import Counter, defaultdict
from itertools import combinations
from re import match, findall

def part1(src: str) -> Any:
    s = 0
    rolls = set()

    for y, line in enumerate(src.splitlines()):
        for x, c in enumerate(line):
            if c == "@":
                rolls.add((x, y))
    
    for x, y in rolls:
        r = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue

                if (x+dx, y+dy) in rolls:
                    r += 1
        if r < 4:
            s += 1
    return s

def part2(src: str) -> Any:
    s = 0
    rolls = set()

    for y, line in enumerate(src.splitlines()):
        for x, c in enumerate(line):
            if c == "@":
                rolls.add((x, y))
    
    while True:
        prev_len = len(rolls)
        to_remove = set()
        for x, y in rolls:
            r = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue

                    if (x+dx, y+dy) in rolls:
                        r += 1
            if r < 4:
                to_remove.add((x, y))

        s += len(to_remove)
        for p in to_remove:
            rolls.remove(p)

        if prev_len == len(rolls):
            return s
