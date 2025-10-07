# Função FIFO, pega o ultimo elemento inserido
def fifo(paginas, quadros):
    memoria = []
    for p in paginas:
        if p not in memoria:
            if len(memoria) < quadros:
                memoria.append(p)
            else:
                memoria.pop(0)  # Remove o primeiro que entrou
                memoria.append(p)
    return memoria

# Função LRU, pega o menos recentemente usado
def lru(paginas, quadros):
    memoria = []
    uso_recente = {}
    for i, p in enumerate(paginas):
        if p not in memoria:
            if len(memoria) < quadros:
                memoria.append(p)
            else:
                # Remove o menos recentemente usado que está na memória
                lru_pagina = min(memoria, key=lambda x: uso_recente.get(x, -1))
                memoria.remove(lru_pagina)
                memoria.append(p)
        uso_recente[p] = i  # Atualiza o tempo de uso
    return memoria

# Função MRU, pega o mais recente usado
def mru(paginas, quadros):
    memoria = []
    uso_recente = {}
    for i, p in enumerate(paginas):
        if p not in memoria:
            if len(memoria) < quadros:
                memoria.append(p)
            else:
                # Remove o mais recente usado que está na memória
                mru_pagina = max(memoria, key=lambda x: uso_recente.get(x, -1))
                memoria.remove(mru_pagina)
                memoria.append(p)
        uso_recente[p] = i
    return memoria

seq_a = [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7]
seq_b = [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11]
seq_c = [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11]

quadros = 8

print("=== FIFO ===")
print("a)", fifo(seq_a, quadros))
print("b)", fifo(seq_b, quadros))
print("c)", fifo(seq_c, quadros))
# qual quadro na memória possuirá a página 7 ?
print("Página 7 está no quadro 8")

print("\n=== LRU ===")
print("a)", lru(seq_a, quadros))
print("b)", lru(seq_b, quadros))
print("c)", lru(seq_c, quadros))
# qual quadro na memória possuirá a página 11 ?
print("Página 11 está no quadro 8")

print("\n=== MRU ===")
print("a)", mru(seq_a, quadros))
print("b)", mru(seq_b, quadros))
print("c)", mru(seq_c, quadros))
# qual quadro na memória possuirá a página 11 ?
print("Página 11 está no quadro 8")

# Qual a melhor politica de substituição?
print("\nA melhor política de substituição depende do padrão de acesso às páginas.\nEm geral, LRU é considerada uma das melhores em termos de desempenho.\n")
