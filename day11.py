from typing import Any
from collections import Counter, defaultdict
from itertools import combinations, product
from re import match, findall
from math import sqrt
from functools import reduce, cache
from operator import add, mul
from math import gcd
import heapq 


def part1(src: str) -> Any:
    g = dict()
    for line in src.splitlines():
        fr, tos = line.split(": ")
        g[fr] = set(tos.split())

    @cache
    def get_paths(start: str) -> int:
        if start == "out":
            return 1
        return sum(map(get_paths, g[start]))
    return get_paths("you")

def part2(src: str) -> Any:
    g = dict()
    for line in src.splitlines():
        fr, tos = line.split(": ")
        g[fr] = set(tos.split())

    @cache
    def get_paths(start: str, dac: bool, fft: bool) -> int:
        if start == "dac":
            dac = True
        if start == "fft":
            fft = True
        if start == "out":
            if dac and fft:
                return 1
            return 0
        return sum(map(lambda n: get_paths(n, dac, fft), g[start]))

    return get_paths("svr", False, False)

