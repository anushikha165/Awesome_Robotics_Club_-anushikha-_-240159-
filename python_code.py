#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      Dell
#
# Created:     10-04-2025
# Copyright:   (c) Dell 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import heapq
grid = [
    ['S', '.', '.', '.', '.', '~', '.', '.', '^', '.'],
    ['#', '#', '#', '.', '.', '~', '#', '.', '^', '.'],
    ['.', '.', '.', '#', '.', '.', '#', '.', '.', '.'],
    ['.', '~', '~', '#', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '#', '#', '#', '#', '.'],
    ['^', '^', '.', '.', '.', '.', '.', '.', '~', '.'],
    ['#', '.', '.', '.', '.', '#', '~', '~', '~', '.'],
    ['.', '.', '#', '#', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '^', '^', '^', '^', 'G'],
    ['.', '#', '#', '#', '#', '#', '#', '.', '.', '.']
]
costs = {
    'S': 0,
    'G': 0,
    '.': 1,
    '~': 3,
    '^': 5,
    '#': float('inf')
}
dirs = [(-1,0), (1,0), (0,-1), (0,1)]

def find_point(symbol):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == symbol:
                return i, j
    return None

start = find_point('S')
goal = find_point('G')
rows, cols = len(grid), len(grid[0])

def dijkstra():
    visited = set()
    pq = [(0, start, [])]

    while pq:
        cost, (x, y), path = heapq.heappop(pq)

        if (x, y) in visited:
            continue
        visited.add((x, y))
        path = path + [(x, y)]

        if (x, y) == goal:
            return path, cost

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                cell_cost = costs[grid[nx][ny]]
                if cell_cost != float('inf'):
                    heapq.heappush(pq, (cost + cell_cost, (nx, ny), path))

    return [], float('inf')
path, total_cost = dijkstra()
print("Step-by-step path coordinates:")
for coord in path:
    print(coord)
print(f"\nTotal path cost: {total_cost}")

