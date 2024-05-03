# Exemplo de for and while
# Programa para imprimir a tabuada de 5
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

for item in range(0, 3, 2):
    print(item, " ")


# Programa para verificar se uma letra digitada é vogal ou consoante
# Loop while para verificar se a letra é vogal ou consoante
while True:
    letra = input("Digite uma letra ou 'sair' para encerrar: ").lower()
    if letra == 'sair':
        break
    if len(letra) == 1: 
        if letra in 'aeiou':
            print(f"A letra '{letra}' é uma vogal.")
        elif letra.isalpha():
            print(f"A letra '{letra}' é uma consoante.")
        else:
            print("Não é uma letra válida.")
    else:
        print("Por favor, digite apenas uma letra.")
