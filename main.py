import heapq

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

def a_star(lab):
    start = find_position(lab, 'S')
    end = find_position(lab, 'E')

    if not start or not end:
        return None, "Labirinto inválido: ponto inicial ou final não encontrado."

    rows, cols = len(lab), len(lab[0])
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
            return path[::-1], None

        visited.add((current.x, current.y))

        for nx, ny in neighbors(current.x, current.y):
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                if lab[nx][ny] != '1':
                    neighbor_node = Node(nx, ny, current.cost + 1, manhattan(nx, ny, *end), current)
                    heapq.heappush(open_list, neighbor_node)

    return None, "Sem solução."

def print_lab_with_path(lab, path):
    lab_copy = [row[:] for row in lab]
    for x, y in path[1:-1]:
        lab_copy[x][y] = '*'
    for row in lab_copy:
        print(' '.join(row))

def read_maze():
    print("Digite o labirinto linha por linha (valores separados por espaço). Use:")
    print("S = início, E = fim, 0 = livre, 1 = obstáculo.")
    print("Digite uma linha vazia para finalizar.\n")

    maze = []
    while True:
        line = input()
        if not line.strip():
            break
        maze.append(line.strip().split())
    return maze

if __name__ == "__main__":
    maze = read_maze()
    path, error = a_star(maze)
    if error:
        print(error)
    else:
        print("\nMenor caminho (em coordenadas):")
        print(path)
        print("\nLabirinto com o caminho destacado:")
        print_lab_with_path(maze, path)
