# PathFinder - Resolvendo o Labirinto 2D com o Algoritmo A*

## 📋 Contribuidores

- [David Ho](https://github.com/Davidlh80)
- [Larissa Pedrosa](https://github.com/larisilvapedrosa)
- [Paula de Freitas](https://github.com/pauladefreitas)

## 📝 Descrição do Projeto
Este projeto implementa o algoritmo A* em Python para encontrar o menor caminho em um labirinto 2D. O algoritmo é especialmente útil para robôs de resgate que precisam navegar de forma eficiente em ambientes com obstáculos, encontrando o caminho ótimo entre um ponto inicial e um ponto final.

## 🚀 Como Executar o Projeto

### Pré-requisitos
1. Python 3.8 ou superior
2. Bibliotecas necessárias:
   ```bash
   pip install heapq
   ```

### Passos para Execução
1. Clone o repositório:
   ```bash
   git clone https://github.com/Davidlh80/path-finder.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd path-finder
   ```
3. Execute o arquivo principal:
   ```bash
   python main.py
   ```

## 🔍 Sobre o Algoritmo A* - Implementação
O algoritmo A* é uma técnica de busca em grafos que combina o custo do caminho já percorrido *(g(n))* com uma estimativa heurística da distância até o objetivo *(h(n))*. A função de avaliação *f(n) = g(n) + h(n)* garante que o algoritmo encontre o caminho mais curto possível.

#### Componentes do Algoritmo:
1. **Função de Custo (g(n))**: 
   - Representa o custo real do caminho desde o nó inicial até o nó atual
   - No nosso caso, cada movimento tem custo 1

2. **Função Heurística (h(n))**: 
   - Utiliza a distância de Manhattan para estimar o custo até o objetivo
   - Calculada como |x1 - x2| + |y1 - y2|
   - Garante que a estimativa nunca superestima o custo real

3. **Função de Avaliação (f(n))**: 
   - f(n) = g(n) + h(n)
   - Determina a ordem de exploração dos nós
   - Garante que o algoritmo explore primeiro os caminhos mais promissores

A implementação é iniciada no arquivo *astar.py*, que contém somente a lógica do algoritmo e suas funções auxiliares. Iniciado com a importação da biblioteca ``heapq``, visto que no A*, é necessário escolher o próximo nó com o menor custo total estimado e ``heapq`` implementa um fila de prioridade *(min-heap)*.

```python
import heapq
```

A seguir, ocorre a definição do dicionário de custos das células, sendo: 

```python
CELL_COSTS = {
    '0': 1,    #caminho livre (custo baixo)
    '2': 3,    #terrenos mais difíceis (custos maiores)
    '3': 5     #terrenos mais difíceis (custos maiores
}
```

Agora, implementamos a classe ``Node``, que define um nó da busca. A função ``__init__`` define o início do algoritmo, com a posição do robô, custo acumulado e estimado até o destino e a referência ao nó anterior. 

```python
    def __init__(self, x, y, cost, heuristic, parent=None):
        self.x = x                  # posição linha
        self.y = y                  # posição coluna
        self.cost = cost            # custo acumulado do caminho percorrido
        self.heuristic = heuristic  # custo estimado até o destino
        self.parent = parent        # referência ao nó anterior (para reconstruir o caminho)
```

Já a função ``__it__`` permite comparar os nós com ``heapq`` usando *f(n) = g(n) + h(n)*, ou seja, a função de avaliação, como exeplificado acima.

```python
    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)
```

Posteriormente, a função ``manhattan`` é usada como heurística admissível e calcula a distância de Manhattan entre dois pontos, indicada para movimentos em grade sem diagonais.

```python
def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
```

A seguir, a função ``find_position`` procura pela posição (linha e coluna) de um caractere (S ou E) na matriz do labirinto. 

```python
def find_position(lab, target):
    for i, row in enumerate(lab):
        for j, value in enumerate(row):
            if value == target:
                return i, j
    return None
```

A função ``neighbors``, por sua vez, gera os vizinhos adjacentes (cima, baixo, esquerda e direita) de uma célula e não considera as diagonais. 

```python
def neighbors(x, y):
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    return [(x+dx, y+dy) for dx, dy in directions]
```

Por fim, a função principal aplica o algoritmo A* ao labirinto 2D. 

### 🧭 Etapas do algoritmo 

Primeiro, procura-se as posições de início (``S``) e fim (``E``), e valida se, caso elas não existam, não há retorno e não há entrada válida para execução do algoritmo.

```python
    start = find_position(maze, 'S')
    end = find_position(maze, 'E')
    if not start or not end:
        return None
```

Agora, realiza-se as inicializações das variáveis. 

```python
open_list = []       # fila de prioridade de nós a explorar
visited = set()      # conjunto de posições já visitadas

start_node = Node(*start, 0, manhattan(*start, *end))
heapq.heappush(open_list, start_node)
```

O nó inicial é criado com custo 0 e heurística calculada, e é adicionado na fila de prioridade. 

```python
while open_list:
    current = heapq.heappop(open_list)
```

Agora,se incia o *loop* de busca e o nó com menor *f(n) = g + h* da fila é selecionado.

```python
        if (current.x, current.y) == end:
            path = []
            while current:
                path.append((current.x, current.y))
                current = current.parent
            return path[::-1]
```

Neste ponto, há uma verificação se a posição atual do robô é E, ou seja, se está no fim. Se sim, o algoritmo encontrou o caminho, então, este é reconstruído, montando uma lista com as coordenadas do caminho percorrido até E, através de ``current.parent``. Como o caminho é construído de trás para frente, ``[::-1]`` é usado para inverter a ordem da lista. 

Já no caso da posição atual não ser E, o código continua sua execução. 

```python
visited.add((current.x, current.y))
```

Assim, marca a casa atual como uma célula visitada para dar continuidade ao caminho. 

```python
        for nx, ny in neighbors(current.x, current.y):
```

Esse laço tem como objetivo ver quais vizinhos são válidos, calcular o custo de chegada, criar um novo nó para cada vizinho válido e adicionar esse nó à fila que escolherá sempre o de menor custo + heurística. Portanto, ele é iniciado com ``neighbors`` retornando as posições adjacentes ao nó atual e declara ``nx, ny`` como as coordenadas do vizinho. 

```python
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
```

Esse condicional valida se a posição está dentro dos limites da matriz ``0 <= nx < rows and 0 <= ny < cols`` e se não está presente na lista de células visitadas. Se não for válida, ignora e vai para o próximo vizinho. 

```python
                cell = maze[nx][ny]
```

Aqui, seleciona o valor da célula. Caso o valor da célula for ``'1'``, ou seja, caso a célula for um obstáculo, ela é ignorada e o robô não pode passar. Caso não:

```python
                    move_cost = CELL_COSTS.get(cell, 1)
```

O custo da célula é consultado no dicionário e, se não estiver no dicionário, usa o valor padrão ``'1'``. 

```python
            neighbor_node = Node(
                nx, ny,
                current.cost + move_cost,
                manhattan(nx, ny, *end),
                current
            )
```

Aqui, um nó é criado representando o vizinho selecionado, sendo: ``nx, ny`` a posição ``x, y`` do nó, ``cost`` o custo acumulado do custo atual + o custo de se mover para esse vizinho, ``heuristic`` a distância de Manhattan até o destino ``E`` e ``parent`` o nó atual (``current``), para reconstrução do caminho no passo anterior. 

```python
                    heapq.heappush(open_list, neighbor_node)
```

Este passo final adiciona o nó selecionado na fila de prioridade ``open_list``. A fila automaticamente manterá os nós ordenados pelo menor *f(n) = g + h*.

Essa iteração considera apenas vizinhos dentro da matriz e não visitados, ignorando obstáculos. Para traçar o menor caminho, dentro do *if*, calcula o custo de movimento com base no tipo de célula e cria um novo nó para adicioná-lo à fila. Se a fila acabar, e não for retornado caminho válido, essa função retorna None. 

O arquivo *main.py* contém a implementação da interface gráfica via *Tkinter*, a leitura da matriz pelo terminal e a visualização do caminho encontrado. 

A escolha de separar as implementações por arquivos se deve pelo princípio de separação das responsabilidades e pela melhor organização e legibilidade do código. 

## 📝 Exemplos de Uso

### Exemplo de Entrada
```
S 0 1 0 0
0 0 1 0 1
0 1 0 0 0
1 0 0 E 1
```

### Exemplo de Saída
```
Menor caminho (em coordenadas):
[(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]

Labirinto com o caminho destacado:
S 0 1 0 0
* * 1 0 1
1 * 1 0 0
1 * * E 1
```

### Legenda:
- S: Ponto inicial
- E: Ponto final
- 0: Caminho livre
- 1: Obstáculo
- *: Caminho encontrado

## 🔧 Funcionalidades Implementadas

1. **Leitura do Labirinto**:
   - Suporte para entrada manual do labirinto
   - Validação de pontos inicial (S) e final (E)

2. **Algoritmo A***:
   - Implementação eficiente usando heap
   - Heurística de Manhattan
   - Tratamento de casos sem solução

3. **Visualização**:
   - Exibição do caminho em coordenadas
   - Representação visual do labirinto com o caminho destacado