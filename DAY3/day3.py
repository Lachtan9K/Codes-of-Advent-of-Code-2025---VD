from pathlib import Path

def max_two_digit(bank: str) -> int:
    bank = bank.strip()
    n = len(bank)
    if n < 2:
        return 0

    digits = [ord(c) - 48 for c in bank]

    suffix_max = [0] * (n + 1)
    m = -1
    for i in range(n - 1, -1, -1):
        if digits[i] > m:
            m = digits[i]
        suffix_max[i] = m

    best = -1

    for i in range(n - 1):
        val = digits[i] * 10 + suffix_max[i + 1]
        if val > best:
            best = val

    return best

def solve(lines: list[str]) -> int:
    return sum(max_two_digit(line) for line in lines if line.strip())

if __name__ == "__main__":
    path = Path("input.txt")
    if path.exists():
        lines = path.read_text(encoding="utf-8").splitlines()
    else:
        import sys
        lines = sys.stdin.read().splitlines()

    print("the answer is:",solve(lines))
