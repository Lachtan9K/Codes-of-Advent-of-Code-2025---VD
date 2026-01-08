from pathlib import Path

def solve(lines):
    g = [line.strip() for line in lines if line.strip()]
    h, w = len(g), len(g[0])
    dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if g[i][j] != "@":
                continue
            adj = 0
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < h and 0 <= nj < w and g[ni][nj] == "@":
                    adj += 1
            if adj < 4:
                ans += 1
    return ans

if __name__ == "__main__":
    lines = Path("input.txt").read_text(encoding="utf-8").splitlines()
    print(solve(lines))
