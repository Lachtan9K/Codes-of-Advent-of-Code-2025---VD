from pathlib import Path
import re
from collections import deque

def solve(lines):
    pat_diag = re.compile(r"\[([.#]+)\]")
    pat_par = re.compile(r"\(([^)]*)\)")

    total = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        m = pat_diag.search(line)
        diag = m.group(1)
        n = len(diag)

        target = 0
        for i, ch in enumerate(diag):
            if ch == "#":
                target |= 1 << i

        masks = []
        for g in pat_par.findall(line):
            g = g.strip()
            if not g:
                continue
            mask = 0
            for x in g.split(","):
                x = x.strip()
                if x:
                    mask |= 1 << int(x)
            masks.append(mask)

        dist = [-1] * (1 << n)
        q = deque([0])
        dist[0] = 0

        while q:
            s = q.popleft()
            if s == target:
                total += dist[s]
                break
            nsd = dist[s] + 1
            for mask in masks:
                ns = s ^ mask
                if dist[ns] == -1:
                    dist[ns] = nsd
                    q.append(ns)

    return total

if __name__ == "__main__":
    lines = Path("input.txt").read_text(encoding="utf-8").splitlines()
    print("the answer is:", solve(lines))
