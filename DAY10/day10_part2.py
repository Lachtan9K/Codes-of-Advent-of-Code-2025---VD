from pathlib import Path
import re
import math
import heapq
import numpy as np
from scipy.optimize import linprog

pat_par = re.compile(r"\(([^)]*)\)")
pat_cur = re.compile(r"\{([^}]*)\}")

def parse_line(line):
    target = list(map(int, pat_cur.search(line).group(1).split(",")))
    m = len(target)

    buttons = []
    for g in pat_par.findall(line):
        g = g.strip()
        if g:
            buttons.append(list(map(int, map(str.strip, g.split(",")))))
        else:
            buttons.append([])

    b = len(buttons)
    A = np.zeros((m, b), dtype=float)
    for j, inc in enumerate(buttons):
        for i in inc:
            A[i, j] = 1.0

    return A, np.array(target, dtype=float)

def solve_ilp(A, b_eq):
    n = A.shape[1]
    c = np.ones(n, dtype=float)

    def lp(bounds):
        return linprog(c=c, A_eq=A, b_eq=b_eq, bounds=bounds, method="highs")

    best = math.inf

    bounds0 = [(0, None)] * n
    r0 = lp(bounds0)
    if not r0.success:
        raise RuntimeError("No feasible solution for a machine.")

    pq = []
    heapq.heappush(pq, (r0.fun, bounds0, r0.x))

    while pq:
        bound, bounds, x = heapq.heappop(pq)
        if bound >= best - 1e-9:
            continue

        frac_idx = None
        for i, v in enumerate(x):
            if abs(v - round(v)) > 1e-7:
                frac_idx = i
                break

        if frac_idx is None:
            best = bound
            continue

        v = x[frac_idx]
        flo = math.floor(v)
        cei = flo + 1

        lo, hi = bounds[frac_idx]

        if flo >= lo - 1e-12 and (hi is None or flo <= hi + 1e-12):
            b1 = list(bounds)
            b1[frac_idx] = (lo, flo)
            r1 = lp(b1)
            if r1.success and r1.fun < best - 1e-9:
                heapq.heappush(pq, (r1.fun, b1, r1.x))

        if cei >= lo - 1e-12 and (hi is None or cei <= hi + 1e-12):
            b2 = list(bounds)
            b2[frac_idx] = (cei, hi)
            r2 = lp(b2)
            if r2.success and r2.fun < best - 1e-9:
                heapq.heappush(pq, (r2.fun, b2, r2.x))

    return int(round(best))

def solve(lines):
    total = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        A, b_eq = parse_line(line)
        total += solve_ilp(A, b_eq)
    return total

if __name__ == "__main__":
    lines = Path("input.txt").read_text(encoding="utf-8").splitlines()
    print("the answer is:", solve(lines))
