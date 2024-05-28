def sacar(valor):

    saldo = 500

    if saldo >= valor:
        saldo -= valor
        print("valor de R$", valor, "sacado!")
        print("retire o seu dinheiro na boca do caixa.")


sacar(100)