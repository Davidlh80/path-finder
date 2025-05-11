import tkinter as tk
import time
from astar import a_star

CELL_COLORS = {
    'S': 'green',
    'E': 'red',
    '1': 'black',
    '0': 'white',
    '2': 'orange',
    '3': 'brown',
    '*': 'blue'
}

class MazeGUI:
    def __init__(self, root, maze):
        self.root = root
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.cell_size = 50
        self.canvas = tk.Canvas(root, width=self.cols * self.cell_size, height=self.rows * self.cell_size)
        self.canvas.pack()
        self.draw_maze()
        tk.Button(root, text="Iniciar A*", command=self.run_astar).pack(pady=10)

    def draw_maze(self, path=None):
        self.canvas.delete("all")
        for i in range(self.rows):
            for j in range(self.cols):
                cell = self.maze[i][j]
                color = CELL_COLORS.get(cell, 'white')
                if path and (i, j) in path[1:-1]:
                    color = CELL_COLORS['*']
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

    def animate_path(self, path):
        for (i, j) in path[1:-1]:
            self.maze[i][j] = '*'
            self.draw_maze(path)
            self.root.update()
            time.sleep(0.3)

    def run_astar(self):
        path = a_star(self.maze)
        if path:
            print("Menor caminho (em coordenadas):")
            print(path)
            self.animate_path(path)
        else:
            print("Sem solução: não há caminho entre S e E.")

def read_maze_from_terminal():
    print("Digite o labirinto linha por linha. Valores válidos: S, E, 0, 1, 2, 3")
    print("Digite uma linha vazia para finalizar.")
    maze = []
    valid = {'S', 'E', '0', '1', '2', '3'}
    while True:
        line = input()
        if not line.strip():
            break
        row = line.strip().split()
        if any(cell not in valid for cell in row):
            print("Linha inválida. Use apenas: S, E, 0, 1, 2, 3.")
            continue
        maze.append(row)
    return maze

if __name__ == "__main__":
    maze = read_maze_from_terminal()
    if not maze:
        print("Nenhuma entrada fornecida.")
    else:
        root = tk.Tk()
        root.title("A* PathFinder - Interface Gráfica")
        app = MazeGUI(root, maze)
        root.mainloop()
        import tkinter as tk
        import time
        from astar import a_star  # importa o algoritmo A*

        CELL_COLORS = {
            'S': 'green',
            'E': 'red',
            '1': 'black',
            '0': 'white',
            '2': 'orange',
            '3': 'brown',
            '*': 'blue'
        }


        class MazeGUI:
            def __init__(self, root, maze):
                self.root = root
                self.maze = maze
                self.rows = len(maze)
                self.cols = len(maze[0])
                self.cell_size = 50
                self.canvas = tk.Canvas(root, width=self.cols * self.cell_size, height=self.rows * self.cell_size)
                self.canvas.pack()
                self.draw_maze()
                tk.Button(root, text="Iniciar A*", command=self.run_astar).pack(pady=10)

            def draw_maze(self, path=None):
                self.canvas.delete("all")
                for i in range(self.rows):
                    for j in range(self.cols):
                        cell = self.maze[i][j]
                        color = CELL_COLORS.get(cell, 'white')
                        if path and (i, j) in path[1:-1]:
                            color = CELL_COLORS['*']
                        x1 = j * self.cell_size
                        y1 = i * self.cell_size
                        x2 = x1 + self.cell_size
                        y2 = y1 + self.cell_size
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

            def animate_path(self, path):
                for (i, j) in path[1:-1]:
                    self.maze[i][j] = '*'
                    self.draw_maze(path)
                    self.root.update()
                    time.sleep(0.3)

            def run_astar(self):
                path = a_star(self.maze)
                if path:
                    print("Menor caminho (em coordenadas):")
                    print(path)
                    self.animate_path(path)
                else:
                    print("Sem solução: não há caminho entre S e E.")


        def read_maze_from_terminal():
            print("Digite o labirinto linha por linha. Valores válidos: S, E, 0, 1, 2, 3")
            print("Digite uma linha vazia para finalizar.")
            maze = []
            valid = {'S', 'E', '0', '1', '2', '3'}
            while True:
                line = input()
                if not line.strip():
                    break
                row = line.strip().split()
                if any(cell not in valid for cell in row):
                    print("Linha inválida. Use apenas: S, E, 0, 1, 2, 3.")
                    continue
                maze.append(row)
            return maze


        if __name__ == "__main__":
            maze = read_maze_from_terminal()
            if not maze:
                print("Nenhuma entrada fornecida.")
            else:
                root = tk.Tk()
                root.title("A* PathFinder - Interface Gráfica")
                app = MazeGUI(root, maze)
                root.mainloop()
