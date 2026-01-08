from pathlib import Path
import bisect

def generate_candidates(max_b: int) -> list[int]:

    D = len(str(max_b))
    cands = set()

    for k in range(1, D // 2 + 1):
        start = 10 ** (k - 1)
        end = 10 ** k
        for x in range(start, end):
            s = str(x)
            for m in range(2, D // k + 1):
                t = s * m
                if len(t) > D:
                    break
                n = int(t)
                if n <= max_b:
                    cands.add(n)

    return sorted(cands)

def prefix_sums(arr: list[int]) -> list[int]:
    ps = [0]
    s = 0
    for v in arr:
        s += v
        ps.append(s)
    return ps

def sum_in_range(cands: list[int], ps: list[int], a: int, b: int) -> int:
    i = bisect.bisect_left(cands, a)
    j = bisect.bisect_right(cands, b)
    return ps[j] - ps[i]

def solve(line: str) -> int:
    ranges = []
    max_b = 0

    for part in line.strip().split(","):
        if not part:
            continue
        a_str, b_str = part.split("-")
        a, b = int(a_str), int(b_str)
        ranges.append((a, b))
        max_b = max(max_b, b)

    cands = generate_candidates(max_b)
    ps = prefix_sums(cands)

    total = 0
    for a, b in ranges:
        total += sum_in_range(cands, ps, a, b)

    return total

if __name__ == "__main__":
    path = Path("input.txt")
    if path.exists():
        line = path.read_text(encoding="utf-8").strip()
    else:
        import sys
        line = sys.stdin.read().strip()

    print("the answer is:",solve(line))
