from pathlib import Path

def solve(lines):
    g = [x.rstrip("\n") for x in lines if x.rstrip("\n") != ""]
    h = len(g)
    w = max(len(x) for x in g)
    g = [x.ljust(w) for x in g]

    srow = next(i for i, row in enumerate(g) if "S" in row)
    scol = g[srow].index("S")

    beams = {scol}
    splits = 0

    for r in range(srow + 1, h):
        new = set(beams)
        for c in beams:
            if g[r][c] == "^":
                splits += 1
                new.discard(c)
                if c - 1 >= 0:
                    new.add(c - 1)
                if c + 1 < w:
                    new.add(c + 1)
        beams = new

    return splits

if __name__ == "__main__":
    lines = Path("input.txt").read_text(encoding="utf-8").splitlines()
    print("the answer is:", solve(lines))
