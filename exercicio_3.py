"""
#### Exercício 3 - Comparando listas.

Receba duas listas de input do usuário. Ele digitará como um texto com os números separados por vírgula. 
Para isso, pode-se utilizar o código disponibilizado que vai transformar esse texto em lista para você.

Eu quero que você me diga qual das listas tem o maior número dentro delas. 

Se a primeira lista tiver o maior número, imprima: "Primeira".
Se a segunda lista tiver o maior número, imprima: "Segunda".
Se ambas tiverem o mesmo número como maior, digite: "Ambas".

Exemplos:

----------------------------------

Digite a sua primeira lista (separando os números por vírgula): 1, 50, 2, 40
Digite a sua segunda lista (separando os números por vírgula): 0, 2, 99, 1, 1, 3

Resposta:
Segunda

----------------------------------

Digite a sua primeira lista (separando os números por vírgula): 1, 0, 2, 30
Digite a sua segunda lista (separando os números por vírgula): 9, 9, 9, 30

Resposta:
Ambas
"""

# Código para pegar as listas de input
primeira_lista = [*map(int, input("Digite a sua primeira lista (separando os números por vírgula): ").split(","))]
segunda_lista = [*map(int, input("Digite a sua segunda lista (separando os números por vírgula): ").split(","))]

# Pegar o maior número de cada lista
maior_primeira = max(primeira_lista)
maior_segunda = max(segunda_lista)

# Comparar os valores e imprimir a resposta
if maior_primeira > maior_segunda:
    print("Primeira")
elif maior_segunda > maior_primeira:
    print("Segunda")
else:
    print("Ambas")
