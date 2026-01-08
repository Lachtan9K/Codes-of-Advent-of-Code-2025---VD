from pathlib import Path
import bisect

MOD10 = [1]
for _ in range(10):
    MOD10.append(MOD10[-1] * 10)

def build_candidates(max_b: int) -> list[int]:
    """
    Vygeneruje všechna čísla tvaru xx (řetězec nějakých číslic opakovaný 2×),
    bez nul na začátku, do maxima max_b.
    """
    cands = []
    # max_b má u nás max 10 číslic => stačí poloviny k=1..5
    for k in range(1, 6):
        pow10 = MOD10[k]
        start = 10 ** (k - 1)
        end = 10 ** k
        for x in range(start, end):
            n = x * pow10 + x
            if n <= max_b:
                cands.append(n)
    cands.sort()
    return cands

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
        if b > max_b:
            max_b = b

    cands = build_candidates(max_b)
    ps = prefix_sums(cands)

    total = 0
    for a, b in ranges:
        total += sum_in_range(cands, ps, a, b)
    return total

if __name__ == "__main__":
    # očekává se input jako jedna dlouhá řádka
    path = Path("input.txt")
    if path.exists():
        line = path.read_text(encoding="utf-8").strip()
    else:
        import sys
        line = sys.stdin.read().strip()

    print("the answer is:",solve(line))
