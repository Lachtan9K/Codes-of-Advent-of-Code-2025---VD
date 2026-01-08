from pathlib import Path

def solve(lines):
    pts = []
    for s in lines:
        s = s.strip()
        if s:
            x, y, z = map(int, s.split(","))
            pts.append((x, y, z))

    n = len(pts)
    in_mst = [False] * n
    dist = [10**30] * n
    parent = [-1] * n

    dist[0] = 0
    max_w = -1
    max_i = max_j = -1

    for _ in range(n):
        u = -1
        best = 10**31
        for i in range(n):
            if not in_mst[i] and dist[i] < best:
                best = dist[i]
                u = i

        in_mst[u] = True

        if parent[u] != -1:
            a, b = parent[u], u
            if a > b:
                a, b = b, a
            if best > max_w or (best == max_w and (a, b) < (max_i, max_j)):
                max_w = best
                max_i, max_j = a, b

        xu, yu, zu = pts[u]
        for v in range(n):
            if not in_mst[v]:
                xv, yv, zv = pts[v]
                dx = xu - xv
                dy = yu - yv
                dz = zu - zv
                w = dx * dx + dy * dy + dz * dz
                if w < dist[v]:
                    dist[v] = w
                    parent[v] = u

    return pts[max_i][0] * pts[max_j][0]

if __name__ == "__main__":
    lines = Path("input.txt").read_text(encoding="utf-8").splitlines()
    print("the answer is:", solve(lines))
