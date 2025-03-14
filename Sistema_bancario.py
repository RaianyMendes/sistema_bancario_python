saldo = 0.00
deposito = 0.00
saque = 0.00
extrato = ""
limite_saque = 500.00
saque_diario = 0
deposito_inicial = False

menu = """

---------- MENU ----------

    [D] DEPOSITAR
    [S] SACAR
    [E] EXTRATO
    [C] SAIR

--------------------------
"""

while True:
    opcao = input(menu).upper()

    if opcao == "D":
       deposito = float(input("Digite o valor do depósito: \n"))
       if deposito > 0:
        saldo += deposito

        if extrato == "\nNenhuma transação realizada!":
            extrato = ""
            
        extrato += f"Depósito  --- R$ {deposito} \n"
        print("\nDepósito realizado com sucesso!")

       else:
          print("\nValor iregular para depósito")
        
    elif opcao == "S":
        if saldo == 0:
             print("\nSaque indisponível. A conta esta zerada!")
        else: 
            saque = float(input("Digite o valor do saque: "))
            saque_diario +=1

            if saque > 500.00:
                print("\nSaque inválido! Valor maior que o limite de saque por transação! (R$ 500.00)")

            elif saque > saldo:
                print("\nSaque inválido por saldo insulficiente")

            elif saque_diario > 3:
                print("\nSaque inválido! Limite diário de transações de saque!(3)")
            
            else: 
                saldo -= saque
                print("\nSaque realizado com sucesso!")
                extrato += f"Saque     --- R$ {saque} \n"
        
    elif opcao == "E":
        if extrato == "":
            extrato = "\nNenhuma transação realizada!" 
        print(extrato)
        print("    Saldo: R$ " + str(saldo))

    elif opcao == "C":
        break

    else:
        print("\nPor favor, insira uma opção válida!")


