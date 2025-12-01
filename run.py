from importlib import import_module
from argparse import ArgumentParser
from re import fullmatch
from pathlib import Path
from time import perf_counter
from functools import reduce
from operator import mul

def as_sec(t: float) -> str:
    if t >= 10.0:
        return f"{t:6.1f} s"
    elif t >= 1e-2:
        return f"{t*1e3:6.1f} ms"
    elif t >= 1e-5:
        return f"{t*1e6:6.1f} us"
    else:
        return f"{t*1e9:6.1f} ps" # will never happen
    
def run_bench(impl, src: str, t: float | None, cnt: int | None):
    acc = []
    ttot = 0.0
    c = 0
    r = None

    while (cnt is None or c < cnt) and (t is None or ttot < t):
        start = perf_counter()
        r = impl(src)
        dur = perf_counter() - start
        ttot +=  dur
        c += 1
        acc.append(dur)

    arith_avg = ttot / c 
    variance = " +- " + as_sec(sum((x - arith_avg)**2 for x in acc) / (c - 1)) \
        if c > 1 else ""
    max_t = as_sec(max(acc))
    min_t = as_sec(min(acc))

    return r, as_sec(arith_avg), variance, max_t, min_t

def run_day(impl, day: int, part: int, src: str, bench: bool, t: float | None, cnt: int | None):
    if t is None and cnt is None:
        cnt = 100
        t = 1

    r, a, v, ma, mi = run_bench(impl, src, t, cnt) \
        if bench else run_bench(impl, src, None, 1)

    if bench:
        print(f"Day {day:2} Part {part} in {a}{v} ({mi}, {ma}): {r}")
    else:
        print(f"Day {day:2} Part {part} in {a}: {r}")

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("days", type=str, default="all", nargs="?")
    parser.add_argument("-b", "--benchmark", action="store_true", help="if present; run each solution multiple times and report arithmetic average (or geometric, if --geometric is set)")
    parser.add_argument("-n", "--samples", type=int, help="the number of samples for the benchmark")
    parser.add_argument("-m", "--max-time", type=int, help="the number of seconds to run the benchmark")

    args = parser.parse_args()

    if args.samples is not None and args.max_time is not None:
        parser.error("cannot specify --samples and --max-time at the same time; only one is used as an upper bound")
    
    use_time = args.max_time is not None

    if args.days == "all":
        days = [i for i in range(1, 12 + 1) if Path(f"./day{i}.py").exists()]
    elif (m := fullmatch(r"^(\d+)-(\d+)$", args.days)):
        days = list(range(int(m[1]), int(m[2]) + 1))
    elif fullmatch(r"\d+(?:,\d+)*", args.days):
        days = list(map(int, args.days.split(",")))
    else:
        parser.error(f"invalid argument {args.days}")
    
    for day in days:
        inp = Path(f"./data/day{day}.txt")

        if not Path(f"./day{day}.py").exists():
            print(f"Day {day}: ERROR - missing implementation")
            continue
        elif not inp.exists():
            print(f"Day {day}: ERROR - missing input; download https://adventofcode.com/2025/day/{day}/input into {inp}")
            continue
        
        mod = import_module(f"day{day}")
        inp_src = inp.read_text().strip()

        run_day(mod.part1, day, 1, inp_src, args.benchmark, args.max_time, args.samples)
        run_day(mod.part2, day, 2, inp_src, args.benchmark, args.max_time, args.samples)
