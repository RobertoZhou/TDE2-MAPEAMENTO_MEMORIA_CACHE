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