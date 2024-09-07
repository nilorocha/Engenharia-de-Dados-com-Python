menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 800
extrato = ''
numeros_saques = 0
LIMITE_SAQUES = 5

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        #Regras deposito, só pode ser valor positivo e registrar em extrato
        #Deposito
        valor = float(input("Informe o valor do deposito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            
        else: print("Operação falhou! O valor informado é inválido")
        
        
    elif opcao == "s":
        #Regras Saque , limite de 3 saques diarios, verificar se tem saldo em conta
        # e registrar valor em extrato
        #Saque
        
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numeros_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Não a saldo suficiente na conta.")
            
        elif excedeu_limite:
            print("Operação falhou! O valor de saque excede o limite.")
            
        elif excedeu_saques:
            print("Operação falhou! Número de máximo de saque excedido")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numeros_saques +=1
            
        else:
            print("Operação falhou! O valor informado é invalido.")
            
        
    elif opcao == "e":
        #Exibir Extrato
        print("\n================= Extrato =================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==============================================")
        
    elif opcao == "q":
        break
    
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")

        