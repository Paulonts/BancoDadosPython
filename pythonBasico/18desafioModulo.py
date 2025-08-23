menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""
opcao = -1
saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3   

def depositar():
    global saldo, extrato
    valorStr = (input("digite a quantidade que deseja depositar: "))
   
    if "." in valorStr or "," in valorStr:
        print("nao é permitido numero quebrado")
        return 
    if not valorStr.isdigit():
        print("Entrada inválida, digite apenas inteiros positivos.")
        return

    valor = int(valorStr) 
    
    if valor <= 0:
        print("nao é possivel depositar")
        return

    saldo += valor
    print(f"deposito no valor de {valor}, foi realizado com sucesso!")
    print(f"{saldo}")


def sacar():
    global numero_saques, LIMITE_SAQUES, limite, saldo
    print("Saque".center(10, "*"))
    print(f"Seu saldo é de {saldo}")

    if saldo <= 0:
        print("voce nao tem saldo para saque")
        return 0

    saqueStr = (input("digite a quantia que deseja sacar: "))

    if "." in saqueStr or "," in saqueStr:
        print("nao é permitido numero quebrado")
        return 0

    saque = int(saqueStr)

    if saque > limite:
        print("so é permitido saque de ate 500 reais")
        return 0
    if numero_saques > LIMITE_SAQUES:
        print("voce atingiu o limite de saques diarios")
        return 0
    
    numero_saques += 1
    saldo -= saque
    print(f"voce sacou {saque} reais, seu saldo agora é de {saldo} reais")
    print(f"quantia de saque que podem ser realizados hoje {numero_saques} de {LIMITE_SAQUES} saques")

def main():
    print("escolha uma opcao")
    while opcao != 0:
        opcao = int(input("[1]Depositar  [2]Sacar  [3]Extrato: "))
        if opcao == 1:
            depositar()
        elif opcao == 2:
            sacar()

main()


        