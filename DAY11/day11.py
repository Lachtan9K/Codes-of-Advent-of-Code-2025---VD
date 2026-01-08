from pathlib import Path
import sys

def solve(lines):
    adj = {}
    for line in lines:
        line = line.strip()
        if not line:
            continue
        a, b = line.split(":", 1)
        adj[a.strip()] = b.strip().split()

    sys.setrecursionlimit(1000000)

    memo = {}
    state = {}

    def dfs(u):
        if u == "out":
            return 1
        if u in memo:
            return memo[u]
        if state.get(u, 0) == 1:
            raise RuntimeError("cycle detected in reachable subgraph")
        state[u] = 1
        total = 0
        for v in adj.get(u, []):
            total += dfs(v)
        state[u] = 2
        memo[u] = total
        return total

    return dfs("you")

if __name__ == "__main__":
    lines = Path("input.txt").read_text(encoding="utf-8").splitlines()
    print("the answer is:", solve(lines))
