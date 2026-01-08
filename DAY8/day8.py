from pathlib import Path
import heapq

def solve(lines):
    pts = []
    for s in lines:
        s = s.strip()
        if s:
            x, y, z = map(int, s.split(","))
            pts.append((x, y, z))

    n = len(pts)
    k = 1000

    heap = []
    for i in range(n - 1):
        xi, yi, zi = pts[i]
        for j in range(i + 1, n):
            xj, yj, zj = pts[j]
            dx = xi - xj
            dy = yi - yj
            dz = zi - zj
            d = dx * dx + dy * dy + dz * dz
            item = (-d, -i, -j)
            if len(heap) < k:
                heapq.heappush(heap, item)
            else:
                if item > heap[0]:
                    heapq.heapreplace(heap, item)

    edges = [(-a, -b, -c) for a, b, c in heap]
    edges.sort()

    parent = list(range(n))
    size = [1] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]

    for _, i, j in edges:
        union(i, j)

    comp = {}
    for i in range(n):
        r = find(i)
        comp[r] = comp.get(r, 0) + 1

    top3 = sorted(comp.values(), reverse=True)[:3]
    return top3[0] * top3[1] * top3[2]

if __name__ == "__main__":
    lines = Path("input.txt").read_text(encoding="utf-8").splitlines()
    print("the answer is:", solve(lines))
