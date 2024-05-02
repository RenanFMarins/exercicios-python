# peça um numero inteiro e determine se ele é ou nao um numero primo

numero = int(input("digite um numero inteiro: "))
primo = True
for i in range(2, numero):
    if numero % i == 0:
        primo = False
        print(f"{numero} nao é primo!")
        break
if primo:
    print(numero, "é primo!")

# peça numero inteiro e determine se ele é ou nao um numero primo

numero = int(int("Digite um número: "))
if numero < 0:
    print("numero invalido. digite apenas valores positivos")
if numero == 0 or numero == 1:
    print(numero, "é um caso especial.")
else:
    if numero == 2:
        print("2 é primo")
    elif numero % 2 == 0:
        print(numero, "não é primo, pois 2 é o unico numero par primo")
    else:
        x = 3
        while x < numero:
            if numero % x == 0:
                break
            x = x + 2
        if x == numero:
            print(numero, "é primo ")
        else:
            print(numero, "não é primo, pois é divisivel por ", x)
