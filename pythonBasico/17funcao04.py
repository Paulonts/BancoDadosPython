def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado (10, 10, somar) #30 resultado da operação 10 + 10 = 20


def subtrair():
    a=20
    b=10
    resultado = a-b
    return resultado

def exibir_resultado(valor):
    print(f"O resultado da operação = {valor}")

exibir_resultado (subtrair())

op = somar
print(op(1,23))
    



salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus 
    return salario



salario_com_bonus = salario_bonus(500) # 2500
print(salario_com_bonus)
