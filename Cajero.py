print("Bienvenido al cajero automático")
pin_correcto = 1234
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    pin = int(input("Ingrese el PIN de 4 dígitos: "))
    if pin == pin_correcto:
        print("🔓 Bienvenido")
        break
    else:
        intentos += 1
        print("❌ Contraseña incorrecta")
        if intentos == max_intentos:
            print("🚫 Se han agotado los intentos, su cuenta ha sido bloqueada")
            exit()
        else:
            print(f"⚠ Le quedan {max_intentos - intentos} intentos")

saldo = 1000 

def consultarsaldo(saldo) :
    print(f"💰 Su saldo es de ${saldo}")
    return saldo
def retirar (saldo , monto) : 
     if monto > saldo :
          print("❌ Fondos insuficientes")
     else : 
        saldo -= monto 
        print(f"✅ Ha retirado ${monto}. Nuevo saldo: ${saldo}")
     return saldo
def depositar(saldo ,monto) : 
     if monto <= 0 :
        print("⚠ El monto debe ser mayor a cero")
     else : 
        saldo += monto 
        print(f"✅ Ha depositado ${monto}. Nuevo saldo: ${saldo}")
        return saldo
     
while True :
        print("Seleccione una opcion")
        print("1. Consultar saldo")
        print("2. Retirar dinero")
        print("3. Depositar dinero")
        print("4. Salir")

    

        opcion = input("Ingrese el numero de la opcion deseada: ")
        if opcion == "1" :
            consultarsaldo(saldo)
        elif opcion == "2" :
            monto = float(input ("ingrese el monto a retirar: "))
            saldo = retirar(saldo, monto)
        elif opcion == "3" : 
            monto = float (input ("ingresa el monto que desea depositar"))
            saldo = depositar(saldo, monto)
        elif opcion == "4" :
            print("Gracias por usar el cajero automatico")
            break
        
        else :
            print("Opcion no valida, intente de nuevo") 
            