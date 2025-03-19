# Probabilidade de Sorteio de Peças Acumulada

Um algoritmo para calcular a probabilidade de ser contemplado em um jogo de sorteio de peças estilo quebra-cabeça onde as peças podem ser acumuladas, dado um determinado número de tentativas. 

## A Origem do Problema

A empresa Opera promoveu uma campanha promocional chamada "Chacoalhe e Concorra" onde os critérios para a contemplação seguiam o especificado acima. Em um ponto onde acumulei 21 peças para um quebra-cabeça de apenas 6, me interessei por calcular a pobsbilidade de tal cenário (12,74% de chance).

## O Algoritmo

Baseando-se na análise da probabilidade de um Jogo Perfeito (N° tentativas = Tamanho quebra-cabeça) percebe-se que a probabilidade de vencer pode ser expressa como: 

$\Huge \frac{6}{6}\cdot \frac{5}{6}\cdot \frac{4}{6}\cdot \frac{3}{6}\cdot \frac{2}{6}\cdot \frac{1}{6}\tiny \text{ ou seja: }\huge \frac{6!}{6^6}\tiny \text{ portanto: }\huge \frac{n!}{n^n}\$

Um jogo de 7 tentativas, onde pelo menos uma peça vem errada pode ser descrito da seguinte forma

$\huge \frac{6!}{6^6} + \frac{6!}{6^6}\cdot \frac{5}{6} + \huge \frac{6!}{6^6}\cdot \frac{4}{6} + \huge \frac{6!}{6^6}\cdot \frac{3}{6} + \huge \frac{6!}{6^6}\cdot \frac{2}{6} + \huge \frac{6!}{6^6}\cdot \frac{1}{6}\$
 
