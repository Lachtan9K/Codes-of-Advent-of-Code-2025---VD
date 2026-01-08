from pathlib import Path

def best_k_digits(s: str, k: int = 12) -> int:
    a = [ord(c) - 48 for c in s.strip()]
    n = len(a)
    if n <= k:
        return int("".join(map(str, a)))

    remove = n - k
    st = []
    for d in a:
        while remove and st and st[-1] < d:
            st.pop()
            remove -= 1
        if len(st) < k:
            st.append(d)
        else:
            remove -= 1

    if remove > 0:
        st = st[:-remove]

    return int("".join(map(str, st)))

def solve(lines: list[str]) -> int:
    return sum(best_k_digits(line, 12) for line in lines if line.strip())

if __name__ == "__main__":
    lines = Path("input.txt").read_text(encoding="utf-8").splitlines()
    print("the answer is:",solve(lines))
