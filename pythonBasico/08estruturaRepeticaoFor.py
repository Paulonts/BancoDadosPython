texto = input("informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
        print()

#range
print (list(range(4)))

#range juntom com for
for numero in range(0, 11):
    print(numero, end=" ")
print()
for numero in range(0, 51, 5):
    print(numero, end=" ")
