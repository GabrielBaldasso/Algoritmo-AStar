# Algoritmo A* para Busca em Labirintos

Este projeto implementa a busca de caminho em um labirinto utilizando o algoritmo A*, que é um algoritmo de busca heurística. O algoritmo utiliza a distância de Manhattan como heurística para encontrar o caminho mais curto entre dois pontos em um labirinto. O código é capaz de imprimir o caminho percorrido e a matriz com o caminho marcado.

## Funcionalidades
- **Algoritmo A***: Implementação do algoritmo A* para encontrar o caminho mais curto entre o ponto de partida ('P') e o ponto de destino ('D').
- **Heurística de Manhattan**: A heurística utilizada é a distância de Manhattan, que calcula a soma das diferenças absolutas das coordenadas dos pontos.
- **Matriz de Labirinto**: O labirinto é representado como uma matriz, onde '1' representa uma parede, '0' um espaço vazio, 'P' o ponto de partida e 'D' o ponto de destino.
- **Exibição de Resultados**: O caminho percorrido é mostrado na matriz do labirinto, com o caminho sendo representado por pontos ('.').

## Componentes do Código
- **Classe `No`**: Representa um nó do labirinto, contendo informações sobre a posição (x, y), o nó pai, o custo real (g), e a heurística (h).
- **Função de Heurística**: A função `calcular_heuristica` calcula a distância de Manhattan entre um nó e o destino.
- **Função de Busca**: A função `encontrar_caminho` implementa o algoritmo A* para buscar o caminho mais curto no labirinto.

## Como Funciona
1. **Inicialização**: A partir do labirinto, são identificados os pontos de origem ('P') e destino ('D').
2. **Busca**: O algoritmo A* explora os vizinhos de cada nó, calculando o custo total (f = g + h) e selecionando o nó com o menor valor de f para continuar a busca.
3. **Caminho**: Quando o destino é alcançado, o caminho é reconstruído a partir dos nós pai e exibido na matriz do labirinto.
4. **Resultado**: O caminho encontrado é impresso na forma de uma matriz, onde o caminho percorrido é indicado por pontos ('.').
