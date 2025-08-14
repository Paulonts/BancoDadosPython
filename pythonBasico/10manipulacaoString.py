curso = "pYtHon"
print(curso.upper()) #deixa todas letra maiusculas
print(curso.lower()) #deixa todas letra minusculas
print(curso.title()) #deixa a primeira letra maiuscula e o resto minuscula

curso = "      Python   "
print(curso.strip()) #revome espaço em branco da esquerda e da direita
print(curso.lstrip()) #revome espaço em branco da esquerda
print(curso.rstrip()) #revome espaço em branco da direita

curso = "Python"
print(curso.center(10, "*")) #centraliza a string
print("." .join (curso)) #coloca caractere no meio das letras
