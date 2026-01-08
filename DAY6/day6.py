from pathlib import Path

def solve(lines):
    lines = [x.rstrip("\n") for x in lines if x.strip("\n") != ""]
    rows = [list(x) for x in lines]
    h = len(rows)
    w = max(len(r) for r in rows)
    for r in rows:
        if len(r) < w:
            r.extend([" "] * (w - len(r)))

    sep = [all(rows[i][j] == " " for i in range(h)) for j in range(w)]

    blocks = []
    j = 0
    while j < w:
        while j < w and sep[j]:
            j += 1
        if j >= w:
            break
        start = j
        while j < w and not sep[j]:
            j += 1
        end = j
        blocks.append((start, end))

    total = 0
    for start, end in blocks:
        op = "".join(rows[-1][start:end]).strip()
        nums = []
        for r in rows[:-1]:
            s = "".join(r[start:end]).strip()
            if s:
                nums.append(int(s))
        if op == "+":
            total += sum(nums)
        else:
            p = 1
            for x in nums:
                p *= x
            total += p

    return total

if __name__ == "__main__":
    lines = Path("input.txt").read_text(encoding="utf-8").splitlines()
    print("the answer is:", solve(lines))
