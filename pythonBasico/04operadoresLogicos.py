# Operaador E
saldo = 1000
saque = 200
limite = 100

operadorE = saldo >= saque and saque <=limite
print(operadorE)

# Operaador OU
saldo = 1000
saque = 200
limite = 100

operadorOr = saldo >= saque or saque <=limite
print(operadorOr)


# Parenteses
saldo = 1000
saque = 250
limite = 200
contaEspecial = True

parenteses = (saldo >= saque and saque <=limite) or (contaEspecial and saldo >= saque)
print(parenteses)