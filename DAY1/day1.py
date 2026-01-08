from pathlib import Path

MOD = 100

def solve(lines: list[str]) -> int:
    pos = 50
    hits = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        dir_ = line[0]
        dist = int(line[1:]) % MOD

        if dir_ == "L":
            pos = (pos - dist) % MOD
        elif dir_ == "R":
            pos = (pos + dist) % MOD
        else:
            raise ValueError(f"Neznámý směr: {dir_} v řádku {line!r}")

        if pos == 0:
            hits += 1

    return hits

if __name__ == "__main__":
    path = Path("input.txt")
    if path.exists():
        lines = path.read_text(encoding="utf-8").splitlines()
    else:
        import sys
        lines = sys.stdin.read().splitlines()

    print("the answer is:",solve(lines))
