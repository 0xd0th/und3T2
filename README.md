# Trabalho Prático 2 - Unidade 3

## SPOJ SHPATH - The Shortest Path

### Integrantes

- Tiago Goes
- Evandro Nobre
- Bruno Cavalcante
- Emanuel Alves

---

### Linguagem Utilizada

Python 3

---

### Link do Problema

https://www.spoj.com/problems/SHPATH/

---

### Descrição

O problema SHPATH - The Shortest Path consiste em encontrar o menor custo entre pares de cidades em um conjunto de consultas.

Cada cidade possui um nome e uma lista de conexões para outras cidades, juntamente com o custo de deslocamento. Para cada consulta, deve ser determinado o menor custo entre a cidade de origem e a cidade de destino.

---

### Como Executar

Clone o repositório:

```text 
git clone github.com/0xd0th/und3T2
cd und3T2
```

Execute o programa:

```text 
python src/main.py < dados/entrada.txt
```

---

### Modelagem do Problema

O problema foi modelado como um grafo direcionado e ponderado.

`Vértices` - cada cidade representa um vértice do grafo.

Como as consultas utilizam nomes de cidades, foi utilizado um dicionário ("dict") para associar cada nome a um índice numérico correspondente à sua posição de leitura na entrada.

`Arestas` - as conexões informadas para cada cidade representam as arestas do grafo.

Cada conexão contém:

- o identificador da cidade de destino;
- o custo para alcançar essa cidade.

Para cada conexão é criada uma aresta direcionada da cidade atual para a cidade de destino.

`Pesos` - corresponde ao custo fornecido na entrada.

Como todos os custos são positivos, é possível utilizar o algoritmo de Dijkstra para encontrar os menores caminhos.

### Representação do Grafo

O grafo foi implementado utilizando listas de adjacência.

Cada vértice armazena uma coleção de objetos do tipo "DirectedEdge", que representam:

- vértice de origem;
- vértice de destino;
- peso da aresta.

Essa representação reduz o consumo de memória e permite percorrer apenas as conexões existentes durante a execução do algoritmo.

Consultas

Após a construção do grafo, são fornecidas diversas consultas.

Cada consulta contém:

- cidade de origem;
- cidade de destino.

Para cada consulta é executado o algoritmo de Dijkstra para determinar o menor custo entre as duas cidades.

---

### Algoritmo Utilizado

Foi utilizado o algoritmo de Dijkstra com fila de prioridade mínima.

O algoritmo funciona da seguinte forma:

1. Inicializa todas as distâncias com infinito.
2. Define a distância da cidade de origem como zero.
3. Insere a origem na fila de prioridade.
4. Remove repetidamente o vértice com menor distância conhecida.
5. Realiza o relaxamento das arestas adjacentes.
6. Atualiza as distâncias sempre que encontra um caminho melhor.
7. Continua até encontrar a menor distância para o destino.

Foi utilizada uma otimização que interrompe a execução assim que o vértice destino é removido da fila de prioridade, pois nesse momento sua menor distância já foi determinada.

---

### Estruturas de Dados Utilizadas

- Lista de adjacência;
- Classe "DirectedEdge";
- Classe "EdgeWeightedDigraph";
- Dicionário ("dict") para mapeamento de nomes de cidades;
- Vetor de distâncias;
- Fila de prioridade mínima ("heapq").

---

### Variação de Dijkstra Utilizada

A solução utiliza o algoritmo de Dijkstra tradicional com fila de prioridade mínima.

A principal característica do problema não está em modificar o algoritmo, mas em:

- modelar corretamente as cidades utilizando nomes;
- converter os nomes para índices numéricos;
- processar múltiplas consultas sobre o mesmo grafo.

Para cada consulta é realizada uma nova execução do algoritmo.

---

### Complexidade

Sejam:

- V = número de cidades;
- E = número de conexões;
- Q = número de consultas.

Cada execução do algoritmo de Dijkstra possui complexidade:

O((V + E) log V)

Como o algoritmo é executado para cada consulta:

O(Q · (V + E) log V)

A complexidade de memória é:

O(V + E)

devido ao armazenamento do grafo em listas de adjacência.

---

### Casos Especiais Considerados

- Múltiplas consultas para o mesmo grafo;
- Existência de vários caminhos entre duas cidades;
- Custos elevados nas arestas;
- Grafo direcionado;
