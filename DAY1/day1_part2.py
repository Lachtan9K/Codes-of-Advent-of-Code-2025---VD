from pathlib import Path

MOD = 100

def count_hits_to_zero(pos: int, k: int, direction: str) -> int:
    """
    Kolikrát během k kliků (po každém kliku) ukáže ciferník na 0,
    když začínáme na `pos` a jdeme o 1 vpravo/vlevo modulo 100.
    """
    if k <= 0:
        return 0

    if direction == "R":
        t0 = (MOD - pos) % MOD
    elif direction == "L":
        t0 = pos % MOD
    else:
        raise ValueError(f"Neznámý směr: {direction}")

    t0 = MOD if t0 == 0 else t0

    if k < t0:
        return 0
    return 1 + (k - t0) // MOD

def solve_part2(lines: list[str]) -> int:
    pos = 50
    hits = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        direction = line[0]
        k = int(line[1:])

        hits += count_hits_to_zero(pos, k, direction)

        if direction == "R":
            pos = (pos + k) % MOD
        else:  # "L"
            pos = (pos - k) % MOD

    return hits

if __name__ == "__main__":
    path = Path("input.txt")
    if path.exists():
        lines = path.read_text(encoding="utf-8").splitlines()
    else:
        import sys
        lines = sys.stdin.read().splitlines()

    print("the answer is: ",solve_part2(lines))
