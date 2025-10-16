# Trabalho de Substituição de Páginas – MRU, LRU e FIFO

## Integrantes do Grupo
- Roberto Zhou 
- Matheus De Bortoli Silva  
- Rafael Gabardo
---

## LINK: <a href="https://youtu.be/A6humEFcQqc">TDE 2 - MAPEAMENTO MEMÓRIA CACHE<a/>

## Descrição do Trabalho
Este trabalho consiste em pesquisar, implementar e explicar os algoritmos de substituição de páginas **MRU**, **LRU** e **FIFO**, utilizando a linguagem de programação de preferência do grupo. A atividade inclui a execução de testes com sequências de páginas e análise dos resultados.

Além da implementação, os integrantes deverão gravar um **vídeo explicativo de até 10 minutos**, abordando cada algoritmo, sua implementação e os resultados obtidos.

---

## Algoritmos Implementados

### FIFO (First In First Out)
- Estratégia: Remove a página que está há mais tempo na memória.
- Características: Simples de implementar, mas pode ter desempenho inferior em algumas situações.

### LRU (Least Recently Used)
- Estratégia: Remove a página que **não foi usada há mais tempo**.
- Características: Bom desempenho para padrões de acesso com localidade temporal.

### MRU (Most Recently Used)
- Estratégia: Remove a página **mais recentemente utilizada**.
- Características: Útil em casos específicos, como leituras sequenciais grandes.

---
