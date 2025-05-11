import heapq

CELL_COSTS = {
    '0': 1,
    '2': 3,
    '3': 5
}

class Node:
    def __init__(self, x, y, cost, heuristic, parent=None):
        self.x = x
        self.y = y
        self.cost = cost
        self.heuristic = heuristic
        self.parent = parent

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def find_position(lab, target):
    for i, row in enumerate(lab):
        for j, value in enumerate(row):
            if value == target:
                return i, j
    return None

def neighbors(x, y):
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    return [(x+dx, y+dy) for dx, dy in directions]

def a_star(maze):
    start = find_position(maze, 'S')
    end = find_position(maze, 'E')
    if not start or not end:
        return None

    rows, cols = len(maze), len(maze[0])
    open_list = []
    visited = set()

    start_node = Node(*start, 0, manhattan(*start, *end))
    heapq.heappush(open_list, start_node)

    while open_list:
        current = heapq.heappop(open_list)

        if (current.x, current.y) == end:
            path = []
            while current:
                path.append((current.x, current.y))
                current = current.parent
            return path[::-1]

        visited.add((current.x, current.y))

        for nx, ny in neighbors(current.x, current.y):
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                cell = maze[nx][ny]
                if cell != '1':
                    move_cost = CELL_COSTS.get(cell, 1)
                    neighbor_node = Node(nx, ny, current.cost + move_cost, manhattan(nx, ny, *end), current)
                    heapq.heappush(open_list, neighbor_node)
    return None
