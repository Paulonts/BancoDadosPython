saldo = 2000.0
saque = float(input("informe o valor que deseja sacar: "))
if saldo >= saque:
    print("realizando saque")
else :
    print("saldo insuficiente")

opcao = int(input("informe uma opção: [1] sacar \n[2] extrato:"))
if opcao == 1:
    valor = float(input("informe a quantia para saque: "))
elif opcao == 2:
    print("exibindo o extrato")
else:
    print("opção invalida")