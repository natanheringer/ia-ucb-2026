
""" 
-------------------------------------------------------
     EU DEVO TER UM NÓ_INICIO, UM GRAFO E UM NÓ_ALVO

1 -  DEVO DECLARAR O O GRAFO EM UM DICIONARIO(STRUCT + ARRAY DE PONTEIROS)

2 -  EU DEVO SAIR DESSE INICIO
     BUSCANDO TODOS OS FILHOS PRIMEIRO.
     A PARTIR DOS FILHOS EXPLORADOS,
     EXPLORAR TODOS OS NOVOS FILHOS.
     ATÉ ENCONTRAR O ALVO
-------------------------------------------------------
GRAFO ORIGINAL COM HEURISTICAS E VALORES POR ARESTAS. 
grafo = {

        'A': [['B', 2], ['C', 4]],
        'B': [['D', 2], ['E', 5]],
        'C': [['F', 2], ['G', 2]],
        'D': ['H', 3],
        'E': [],
        'F': [],
        'H': ['I', 4],
        'G': ['I', 2],
        'I': ['J', 1],
        'J': []

}

heuristica = {

        'A': 9, 'B': 10, 'C': 5, 'F': 7, 'G': 3,
        'D': 8, 'E': 15, 'D': 8, 'H': 5, 'I': 1,
        'J': 0

}
"""

grafo = {

	'A': ['B', 'C'],
        'B': ['D','E'],
        'C': ['F', 'G'],
        'E': [],
        'F': [],
        'D': ['H'],
        'H': ['I'],
        'G': ['I'],
        'I': ['J'],
        'J': []
}


def bfs(grafo, inicio, alvo):

        pai            = {inicio: None}
        # cria a fila vazia     
        fila           = [inicio]

        # Lista para rastrear nos visitados
        visitados      = [inicio]
        ordem_expansao = []
        
        print(f"\n----------BFS----------")
        print(f"Nós a visitar: \n")


        # para inserir na fila: .append(argumento)


        while len(fila) > 0:
                # FIFO: Retira o elemento mais antigo (indice 0)
                no_atual = fila.pop(0)
                ordem_expansao.append(no_atual)
                
                if no_atual == alvo:
                    print(f"\n\nEstados Visitados: {visitados}\n")
                    print(f"Ordem de expansao dos Estados:  {' -> '.join(ordem_expansao)}\n")
                    print(f"Quantidade  de Estados Expandidos: {len(ordem_expansao)}\n")
                    print(f"Alvo encontrado: {alvo}\n")
                    
                    caminho = []
                    no      = alvo
                    while no is not None:
                       caminho.append(no)
                       no = pai[no]
                    
                    caminho.reverse()
                    print(f"Tamanho do caminho: {len(caminho)}\n")
                    print(f"Caminho: {caminho}\n")
                    return
 
                # Processa o nó 
                print(no_atual, end=" -> ")

                # Explora os vizinhos do nó atual
                for vizinho in grafo[no_atual]:
                        # Se o vizinho ainda não foi descoberto
                        if vizinho not in visitados:
                                
                                pai[vizinho] = no_atual
                                
                                visitados.append(vizinho)       # Marca como visitado imediatamente
                                # print(no_atual, vizinho)
                                fila.append(vizinho)            # Entra no final da fila
                                
                                
        print("Fim da busca")
        
       



bfs(grafo, 'A', 'J')
