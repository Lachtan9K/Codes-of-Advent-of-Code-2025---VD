from pathlib import Path

def solve(lines):
    lines = [x.rstrip("\n") for x in lines]
    blank = lines.index("")
    rs = []
    for s in lines[:blank]:
        a, b = map(int, s.split("-"))
        rs.append((a, b))
    rs.sort()

    total = 0
    cur_a = cur_b = None
    for a, b in rs:
        if cur_a is None:
            cur_a, cur_b = a, b
        elif a > cur_b + 1:
            total += cur_b - cur_a + 1
            cur_a, cur_b = a, b
        else:
            if b > cur_b:
                cur_b = b

    if cur_a is not None:
        total += cur_b - cur_a + 1

    return total

if __name__ == "__main__":
    lines = Path("input.txt").read_text(encoding="utf-8").splitlines()
    print("the answer is:", solve(lines))
