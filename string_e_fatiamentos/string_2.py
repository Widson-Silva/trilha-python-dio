nome = "Widson"
idade = 24
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Widson", "idade": 24}

print("Nome: %s Idade: %d" %(nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(idade, nome))

print("Nome: {0} Idade: {1} Nome: {0} {0}".format(nome, idade))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))

print("Nome: {name} Idade: {age}".format(age=idade, name=nome))

print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}") # Formatação das casas decimais
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}") # Formatação das casas decimais com espaçamento a esquerda
