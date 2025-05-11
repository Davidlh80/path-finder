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

### 🔍 Sobre o Algoritmo A*
O algoritmo A* é uma técnica de busca em grafos que combina o custo do caminho já percorrido (g(n)) com uma estimativa heurística da distância até o objetivo (h(n)). A função de avaliação f(n) = g(n) + h(n) garante que o algoritmo encontre o caminho mais curto possível.

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