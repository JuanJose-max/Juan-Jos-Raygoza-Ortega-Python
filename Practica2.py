print("Ingrese cualquier frase")
frase = input()

print("La frase es:", frase)
print("La frase en mayusculas es:", frase.upper())
print("La frase en minusculas es:", frase.lower())
print("La frase tiene", len(frase), "caracteres")
print(f"La {frase} ",frase.split(" "))

for frase in frase.split(" "):
    print(frase.upper())
print("Escrscribe una palabra que quieras buscar dentro de la frase")
palabra = input()
if palabra in frase:
    print("La palabra", palabra, "se encuentra en la frase")
else:
    print("La palabra", palabra, "no se encuentra en la frase")


print("La frase tiene", len(frase), "caracteres")
print("Fin del programa")