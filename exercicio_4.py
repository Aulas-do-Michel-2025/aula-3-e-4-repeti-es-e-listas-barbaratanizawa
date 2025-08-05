"""
#### Exercício 4 - Lista de organismos

Você recebeu uma lista que contém, para cada organismos detectado numa amostra, uma outra lista contendo a 
quantidade de leituras que esse organismo teve em cada identificador taxonômico.

Obs: Deixei a lista direto no exercício para facilitar. Mas faça o código para descobrir, não coloque a resposta direto!

Por exemplo:

[[100, 200, 300], [1, 99, 10000], [1, 1, 1]].

Eu quero que você identifique o organismo que teve a maior média de leituras entre todos os organismos da lista.

Ao identificar digite a posição em que esse organismo se encontra na lista.

No exemplo acima, você imprimiria:

"O organismo com maior média é o da posição 1 da lista."

Dica: Utilize mais de um for para resolver o exercício, um para a lista de organismos e um para cada lista. Cuidado com a identação.
"""

# Lista fornecida
lista_de_organismos = [
    [50, 50, 50],
    [125, 99, 12],
    [19, 91, 42],
    [40, 189, 0],
    [1, 0, 0],
    [100, 100, 70],
    [99, 12, 12]
]

# Inicializa as variáveis para guardar a maior média e a posição correspondente
maior_media = None
posicao_maior = None

# Percorre a lista de organismos
for i in range(len(lista_de_organismos)):
    organismo = lista_de_organismos[i]
    soma = 0
    
    # Soma as leituras do organismo
    for leitura in organismo:
        soma += leitura
    
    media = soma / len(organismo)

    # Atualiza se a média for maior que a anterior
    if (maior_media is None) or (media > maior_media):
        maior_media = media
        posicao_maior = i

# Imprime o resultado final
print(f"O organismo com maior média é o da posição {posicao_maior} da lista.")
