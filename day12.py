
from typing import Any, cast

def part1(src: str) -> Any:
    *p, l = src.split("\n\n")
    ar = [pp.count("#") for pp in p]
    s = 0
    for l in l.splitlines():
        a, *t = l.split()
        w, h = map(int, a[:-1].split("x"))
        if sum(ar[i]*int(n) for i, n in enumerate(t)) < w*h:
            s += 1
    return s

def part2(src: str) -> Any:
    return "Why did you do this, Eric?"