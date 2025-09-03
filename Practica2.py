print("Ingrese cualquier frase")
frase = input()

print("La frase es:", frase)
print("La frase en mayusculas es:", frase.upper())
print("La frase en minusculas es:", frase.lower())
print("La frase tiene", len(frase), "caracteres")
print(f"La {frase} ", frase.split(" "))

for palabra_frase in frase.split(" "):
    print(palabra_frase.upper())

print("Escribe una palabra que quieras buscar dentro de la frase")
palabra = input()
if frase.count(palabra) != -1:
    print(f"La palabra '{palabra}' se encuentra en la frase, y aparece {frase.count(palabra)} veces.")
else:
    print(f"La palabra{palabra}no se encuentra en la frase")

print("Escribe la palabra que deseas remplazar de la frase")
palabra_remplazar1 = input()

print("Cual es la palabra que deseas remplazar")
palabra_remplazar = input()

frase_nueva = frase.replace(palabra_remplazar1, palabra_remplazar)
print("La nueva frase es:", frase_nueva)