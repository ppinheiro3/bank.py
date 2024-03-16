# SEJA BEM VINDO AO NOSSO E-BANK

menu = "SEJA BEM VINDO AO NOSSO BANCO\nESCOLHA UMA DAS OPCOES ABAIXO\n" """
[d] Depositar
[s] Sacar
[e] Extrato
[q] SAIR

=>"""

saldo = 0
limite_por_saque = 500.00
numero_saques = 0
limite_saque = 3
extrato = ""

while True:

    opcao = input(menu)

    if opcao == "d":

        valor = float(input("informe o valor do seu deposito: "))

        if valor > 0:
           
           saldo += valor

           extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("Operacao falhou! O valor informado esta incorreto")  


    elif opcao == "s":

        valor = float(input("informe o valor para saque:   "))


        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite_por_saque

        excedeu_saque =  numero_saques >= limite_saque



        if excedeu_saldo:
            print("Operacao falhou! Voce nao tem saldo suficiente")

        elif excedeu_limite:
            print("Operacao falhou! Voce atingiu seu limite de valor a sacar")

        elif excedeu_saque:
            print("Operacao Falhou! voce atingiu seu limite mensal de saque")    

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:  R$  {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operacao falhou o valor informado esta incorreto")


            

    elif opcao == "e":
        print("\n############# EXTRATO ############")
        print("Nao foram realizado movimentacoes" if not extrato else extrato)
        print(f"\nSaldo:  R$  {saldo:.2f} ")
        print("\n##################################")

    elif opcao == "q":
        break
    

    else:
        print("Nenhuma operacao realizada procure seu gerente.")



                            



