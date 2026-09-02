# GRAFO ORIGINAL COM HEURISTICAS E VALORES POR ARESTAS. 
grafo = {

        'A': [['B', 2], ['C', 4]],
        'B': [['D', 2], ['E', 5]],
        'C': [['F', 2], ['G', 2]],
        'D': [['H', 3]],
        'E': [],
        'F': [],
        'H': [['I', 4]],
        'G': [['I', 2]],
        'I': [['J', 1]],
        'J': []

}

heuristica = {

        'A': 9, 'B': 10, 'C': 5, 'F': 7, 'G': 3,
        'D': 8, 'E': 15, 'D': 8, 'H': 5, 'I': 1,
        'J': 0

}

# f(n) = g(n) + h(n)

# g sobre n representa o custo do inicio até fim, n = nó
# h sobre n representa o custo no inicio até o objetivo 
# f sobre n representa o custo utilizado pelo algoritmo para escolher o proximo estado
def a_estrela(inicio, alvo):
    
    # rastreia o caminho definindo a familiaridade entre nos
    pai = {inicio: None}
    
    # fila de prioridade manual: 
    # guarda tuplas( f_n, no_atual, caminho_percorrido, g_n )
    fila_prioridade = [(0 + heuristica[inicio], inicio, [inicio], 0)]
    
    # registra visitas para nao visitar nós custosos
    visitados = {}
    ordem_expansao = []
    
    while fila_prioridade:
    # busca o indice do nó com maior prioridade(menor valor)
        indice_melhor = 0
        
        for i in range(1, len(fila_prioridade)):
            if fila_prioridade[i][0] < fila_prioridade[indice_melhor][0]:
                indice_melhor = i
                
        # remove o nó prioritario da fila 
        custo_total, no_atual, caminho, custo_caminho = fila_prioridade.pop(indice_melhor)
        
        ordem_expansao.append(no_atual) 
        
        
        # se chega ao destino, retorna caminho e custo total gasto
        if no_atual == alvo:
            print(f"Estados visitados: {ordem_expansao}")
            print(f"Ordem de expansao: {' -> '.join(ordem_expansao)}")
            print(f"Quantidade de estados expandidos: {len(ordem_expansao)}")
            print(f"Caminho: {caminho}")
            print(f"Tamanho do caminho: {len(caminho)}")
            print(f"Custo total: {custo_caminho}")
            print(f"Alvo encontrado: {alvo}")
            return caminho, custo_caminho
            
        # se o nó ja foi visitado por caminho mais curto ou igual, ignora
        if no_atual in visitados and visitado[no_atual] <= custo_caminho:
            continue
        visitados[no_atual] = custo_caminho
        
        # explora os vizinhos do no atual 
        for vizinho, peso_aresta in grafo.get(no_atual, []):
            novo_custo_caminho = custo_caminho + peso_aresta 
            custo_heuristica   = heuristica.get(vizinho, 0)
            novo_custo_total   = novo_custo_caminho + custo_heuristica # prioridade final do A*
            
            novo_caminho = caminho + [vizinho]
            
            # adiciona vizinho na fila com prioridade calculada
            fila_prioridade.append((novo_custo_total, vizinho, novo_caminho, novo_custo_caminho))
        
    return None, float('inf') # se nao encontrar o caminho
    
# execucao do algoritmo a*
caminho_final, custo_total = a_estrela('A', 'J')
print(f"melhor caminho: {caminho_final}")       
print(f"custo total: {custo_total}")
    
    
    
    
    
    



