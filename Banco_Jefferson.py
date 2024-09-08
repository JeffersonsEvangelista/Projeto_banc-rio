saldo = 0
limite = 500
extrato = ""
numeros_saque = 0
QUANTIDADE_SAQUES = 3
menu = "menu"
E = "EXTRATO"

print(menu.center(24, "-"))

menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato    
    [0] Sair

Digite sua opção:"""



while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        print("")
        valor = float(input("Digite o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"

        else:
            print("Operação falhou. Tente novamente!")

    elif opcao == "2":
        valor = float(input("Digite o valor que deseja sacar: "))

        limite_saque = valor > saldo
        valor_por_saque = valor > limite
        limite_retirada = numeros_saque >= QUANTIDADE_SAQUES

        if limite_saque:
            print("Saldo insuficiente!")

        elif valor_por_saque:
            print("Valor ultrapassou o limite por dia!")

        elif limite_retirada:
            print("Quantidade de saque ultrapassado!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numeros_saque += 1
        
        else:
            print("Operação falhou! O valor informado é inválido.")


    elif opcao == "3":

        print(E.center(24, "$"))
        print(f"\nSaldo: R$ {saldo:.2f}\n")
        print("Movimentações." if not extrato else extrato)
        print("$$$$$$$$$$$$$$$$$$$$$$$$")
        

    elif opcao == "0":
        break

    else:
        print("Operação incorreta, por favor selecione novamente a operação desejada!")