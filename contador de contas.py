print("====SOMADOR DE CONTAS MENSAIS====")
print("Criador: Elliot")

print()

l = float(input("Quanto você paga de luz: "))
a = float(input("Agua: "))
i = float(input("Internet: "))
a1 = float(input("Alimentação: "))
p = float(input("Planos: "))
p1 = float(input("Passagem: "))
c = float(input("Condominio: "))
o = float(input("Outros: "))
conta = l + a + i + a1 + p + p1 + c + o

print()

print("Você pagara este mês: R$", conta)

print()

p4 = float(input("Qual o seu sálario: "))
conta2 = p4 - conta
print("Você ficara com: R$", conta2)
print()

#FATURA
te1 = ("Luz, Agua, Iternet, Alimentacao, Planos, Passagem, Condominio, Outros")
te2 = (l, a, i, a1, p, p1, c, o )


arquivo = input("Nome do fratura: ")
arquivo123 = open(arquivo+".txt", "a")

arquivo123.write(str(arquivo))
arquivo123.write("\n")
arquivo123.write("\n")

arquivo123.write("Luz, Agua, Iternet, Alimentacao, Planos, Passagem, Condominio, Outros")

arquivo123.write("\n")
arquivo123.write(str(te2))

arquivo123.write("\n")
arquivo123.write("\n")

arquivo123.write("Total:")
arquivo123.write("\n")
arquivo123.write(str(conta))

arquivo123.write("\n")
arquivo123.write("\n")
arquivo123.write("Criador: Elliot")

aasd = input()





