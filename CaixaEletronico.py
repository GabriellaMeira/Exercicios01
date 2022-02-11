#Simulação da operação de um caixa eletrônica

def mensagem_abertura():
    print("**************************************************")
    print(" Seja bem vindo à transação no caixa eletrônica! ")
    print("**************************************************")

#Um subprograma como uma função para fazer deposito
def deposito(saldo):
    valor = float(input("O valor do deposito: R$ "))
    saldo += valor #saldo = saldo + valor
    return saldo

#Um subprograma para fazer saque
def saque(saldo):
    valor = float(input("O valor do saque: R$ "))
    if (valor > saldo):
        print("Infelizmente o saldo insuficiente e verifique seu saldo!")
    else:
        saldo -= valor #saldo = saldo - valor
    return saldo

#Um subprograma para fazer o consulta
def consulta(saldo):
    print(f"Saldo atual: R$ {saldo:.2f}")

#Um subprograma de mensagem para encerrar programa
def encerra_transacao():
    print("Encerra Sistema !")

#Um subprograma para opção
def menu():
    print("\nMenu para sua transação: ")
    print("(1) Deposito (2) Saque (3) Saldo (4) Sair ")
    print()

#programa principal
mensagem_abertura()
saldo = 1000.0 #saldo inicial
continua = True
while (continua):
    menu()
    opcao = int(input("Escolhe sua opção! "))
    if (opcao == 1):
        saldo = deposito(saldo)
    elif (opcao == 2):
        saldo = saque(saldo)
    elif (opcao == 3):
        consulta(saldo)
    else:
        encerra_transacao()
    continua = not (opcao == 4)

input("Fim das Transações!")
        
