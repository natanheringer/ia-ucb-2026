grafo = { 
    
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': [],
    'G': ['I'],
    'H': ['I'],
    'I': ['J'],
    'J': []
    
}

def dfs(grafo, inicio, alvo):
    
    # no pai para rastrear o caminho 
    pai       = {inicio: None}
    # cria a pilha vazia
    pilha     = [inicio]
    
    # guarda os visitados em uma lista
    visitados = []
    ordem_expansao = []
    
    print(f"\n----------DFS---------")
    print(f"Nós a visitar: \n")
    
    while len(pilha) > 0:
        # retira o elemento mais recente(ultimo indice)
        no_atual = pilha.pop()
        
        # guarda o valor 
        if no_atual not in ordem_expansao:
            ordem_expansao.append(no_atual)
            
        #processa o nó
        if no_atual not in visitados:
            visitados.append(no_atual)
            print(no_atual, end=" -> ")
        
        if no_atual == alvo:
            print(f"\n\nEstados Visitados: {visitados}")
            
            str_expansao = " -> ".join(ordem_expansao)
            print(f"\nOrdem de expansao dos Estados: {str_expansao}\n")
            print(f"Quantidade de estados expandidos: {len(ordem_expansao)}\n")
            print(f"Alvo encontrado: {alvo}\n")
            
            caminho = []
            no      = alvo
            while no is not None:
                caminho.append(no)
                no  = pai[no]
                
            caminho.reverse()
            print(f"Caminho: ", caminho)
            return
           
        # --- CORREÇÃO AQUI: Alinhado na esquerda, fora do "if no_atual == alvo" ---
        # explora os vizinhos do no atual
        # revertemos a lista de vizinhos para manter a ordem
        for vizinho in reversed(grafo[no_atual]):
            # se o vizinho ainda nao foi explorado, 
            if vizinho not in visitados:   
                
                pai[vizinho] = no_atual
                pilha.append(vizinho) # entra no topo da pilha

    print(f"fim da busca")
    
dfs(grafo, 'A', 'J')

