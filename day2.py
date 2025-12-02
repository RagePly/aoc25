from typing import Any
from collections import Counter
from re import match

def part1(src: str) -> Any:
    s = 0
    for r in src.split(","):
        a, b = map(int, r.split("-"))
        for n in range(a, b+1):
            st = str(n)
            if len(st) % 2 == 0 and st[:len(st)//2] == st[len(st)//2:]:
                s += n
    return s

def part2(src: str) -> Any:
    s = 0
    for r in src.split(","):
        a, b = map(int, r.split("-"))
        for n in range(a, b+1):
            st = str(n)
            l = len(st)//2
            c = 2
            while (l := len(st) // c) > 0:
                if len(st) % l != 0:
                    c += 1
                    continue
                sub = st[:l]
                if st == sub*c:
                    s += n
                    break
                c += 1

    return s