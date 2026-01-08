from pathlib import Path
import bisect

def solve(lines):
    lines = [x.rstrip("\n") for x in lines]
    blank = lines.index("")
    rs = []
    for s in lines[:blank]:
        a, b = map(int, s.split("-"))
        rs.append((a, b))
    rs.sort()

    merged = []
    for a, b in rs:
        if not merged or a > merged[-1][1] + 1:
            merged.append([a, b])
        else:
            if b > merged[-1][1]:
                merged[-1][1] = b

    starts = [a for a, b in merged]
    ends = [b for a, b in merged]

    def is_fresh(x):
        i = bisect.bisect_right(starts, x) - 1
        return i >= 0 and x <= ends[i]

    cnt = 0
    for s in lines[blank + 1:]:
        if s:
            if is_fresh(int(s)):
                cnt += 1
    return cnt

if __name__ == "__main__":
    lines = Path("input.txt").read_text(encoding="utf-8").splitlines()
    print("the answer is:", solve(lines))
