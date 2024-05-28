menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

===> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao.lower() == "d": # Parte do depósito

        valor_deposito = float(input("Informe o valor do deposito R$: ")) # Input do Teclado / Depósito

        if valor_deposito > 0: # Verifica se o valor é positivo
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n" # Adiciona um depósito ao Extrato

        else: # Caso não for positivo ele da uma mensagem de erro e continua a repetição do While
            print("\nOperação falhou! O Valor informado é inválido.")

    elif opcao.lower() == "s": # Parte do saque

        valor_saque = float(input("Informe o valor de saque R$: ")) # Input do Teclado / Saque

        excedeu_saldo = valor_saque > saldo 

        excedeu_limite = valor_saque > limite

        excedeu_saques = numero_saque >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! O limite de saque diário foi excedido")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saque += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao.lower() == "e":

        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato) # Ternário
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao.lower() == "q":
        break
    
    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")