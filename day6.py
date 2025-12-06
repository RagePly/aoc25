from typing import Any
from collections import Counter, defaultdict
from itertools import combinations
from re import match, findall

def part1(src: str) -> Any:
    s = 0
    cols = []
    for line in src.splitlines():
        for i, c in enumerate(line.split()):
            if c == "+":        
                s += sum(cols[i])
            elif c == "*":
                p = 1
                for n in cols[i]:
                    p *= n
                s += p
            else:
                if i >= len(cols):
                    cols.append([int(c)])
                else:
                    cols[i].append(int(c))
    return s

def part2(src: str) -> Any:
    s = 0
    cols = []
    for line in src.splitlines():
        for i, c in enumerate(reversed(line)):
            if i >= len(cols):
                cols.append("")
            cols[i] = cols[i] + c
    terms = []
    for term in map(str.strip, cols):
        if not term:
            continue
        elif term.endswith("+"):
            s += sum(terms) + int(term[:-1])
            terms = []
        elif term.endswith("*"):
            p = int(term[:-1])
            for n in terms:
                p *= n
            s += p
            terms = []
        else:
            terms.append(int(term))
    return s
