
from typing import Any
from collections import Counter, defaultdict
from itertools import combinations, product
from re import match, findall
from math import sqrt
from functools import reduce
from operator import add, mul
from math import gcd
import heapq 


def part1(src: str) -> Any:
    s = 0
    for line in src.splitlines():
        target, *buttons = line.split()
        buttons = [list(map(int, but[1:-1].split(","))) for but in buttons[:-1]]
        target = tuple(c == "#" for c in target[1:-1])

        q = [(0, 0, tuple([False]*len(target)))]
        v: set[tuple[int, ...]] = set()
        ii = 1

        while q:
            d, _, st = heapq.heappop(q)

            if st in v:
                continue
            v.add(st)

            if st == target:
                s += d
                break
            
            for b in buttons:
                new_st = tuple((not x) if i in b else x for i, x in enumerate(st))
                heapq.heappush(q, (d+1, ii, new_st))
                ii += 1
    return s

def part2(src: str) -> Any:
    import scipy.optimize
    import numpy as np
    s = 0

    for line in src.splitlines():
        _, *buttons = line.split()
        target = tuple(int(c) for c in buttons[-1][1:-1].split(","))
        buttons = [list(map(int, but[1:-1].split(","))) for but in buttons[:-1]]

        A = np.array([
            [
                int(i in b) for b in buttons
            ]
            for i in range(len(target))
        ])
        b = np.array(target)

        # Rationalle
        # x is the clicks per button (x_i is clicks per button i)
        # c^T x is the total number of clicks (given c_i = 1 for all i in 0..len x)
        # b is the target counters
        # Ax is the output counters from clicking x
        # We want to minimize c^T x while Ax == b (b <= Ax <= b)
        # We also want an integer solution greater than or equal to 0
        res = scipy.optimize.milp(
            np.ones((len(buttons),)), # sum of clicks (c^T x)
            integrality=1,            # positive integer solutions
            constraints=(A, b, b)     # Ax = b
        )        
        s += sum(int(np.round(xc)) for xc in res.x)
    return s
