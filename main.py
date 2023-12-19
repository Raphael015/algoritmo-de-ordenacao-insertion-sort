def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def criar_vetor(tamanho):
    vetor = []
    numero = 1  # Começando com o primeiro número ímpar
    for _ in range(tamanho):
        vetor.append(numero)
        numero += 2
    return vetor

# Exemplo de uso:
tamanho_do_vetor = int(input("Digite o tamanho do vetor: "))
vetor = criar_vetor(tamanho_do_vetor)

print(f"Vetor original: {vetor}")
insertion_sort(vetor)
print(f"Vetor ordenado: {vetor}")
