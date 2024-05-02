#imposto de renda
salario = float(input("Diga seu salario atual: "))
if salario > 2000:
    inss = salario * 0.10
    impostoRenda = salario * 0.15
    print("valor do inss:", inss, "e do imposto de renda:", impostoRenda)
if salario < 2000:
    print("Isento do imposto de renda")

# abono salarial
salario = float(input("Diga seu salario atual: "))
tempo = int(input("diga quantos anos completos tem de serviço: "))
if tempo < 1:
    print("salario se matem", salario)
else:
    if tempo < 10:
        salario = salario * 1.10
    else:
        salario = salario * 1.25
    print("salario novo, com abono", salario)

# converter numero flutuante em metros e converta o resultado em centimetros 
metros = float(input("valor em metros: "))
centimetros = metros * 100
print(f"{metros:.2f} metros equivalem a {centimetros:.2f} centimetros")
print("%4.2f" % metros, "metros equivalem a", "%4.2f" % centimetros, "centimetros")
print(metros, "metros equivalente a", centimetros, "centimetros")
