from pathlib import Path
import numpy as np

def solve(lines):
    g = [line.strip() for line in lines if line.strip()]
    h, w = len(g), len(g[0])
    a = np.array([[1 if c == "@" else 0 for c in row] for row in g], dtype=np.int8)

    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

    def counts(x):
        p = np.pad(x, 1, mode="constant", constant_values=0)
        c = np.zeros((h, w), dtype=np.int16)
        for di, dj in dirs:
            c += p[1+di:1+di+h, 1+dj:1+dj+w]
        return c

    total = 0
    while True:
        c = counts(a)
        rem = (a == 1) & (c < 4)
        k = int(rem.sum())
        if k == 0:
            break
        a[rem] = 0
        total += k

    return total

if __name__ == "__main__":
    lines = Path("input.txt").read_text(encoding="utf-8").splitlines()
    print("the answer is: ",solve(lines))
