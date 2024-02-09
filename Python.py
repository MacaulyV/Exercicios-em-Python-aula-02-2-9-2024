# Definindo a função que vai encontrar os números exclusivos
def numeros_exclusivos(a, b):
    # Criando listas vazias para os números exclusivos
    numeros_exclusivos_a = []
    numeros_exclusivos_b = []

    # Encontrando os números que estão em a mas não em b
    for numero in a:
        if numero not in b:
            numeros_exclusivos_a.append(numero)

  


