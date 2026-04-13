#Ejercicio 1.
while True:
    nombre = input("Nombre: ") #pedimos el nombre al usuario
    
    if nombre.isalpha(): #validamos el nombre
        nombre = nombre.title() #pone la primera letra del nombre en mayuscula
        break
    else:
        print("Error: solo letras.")

while True:
    productos = (input("Cantidad de productos: ")) #pedimos la cantidad de productos
    if productos.isdigit(): #validamos el numero
        productos = int(productos)
        if productos > 0:
            break
        else:
            print("Error: solo números enteros positivos.")
    else:
        print("Error: solo números enteros positivos.")

total = 0
total_descuento = 0
resumen = "" #guardamos un string con todos los productos (ya que no podemos utilizar diccionarios)

for i in range(productos): #pedimos el precio por cada producto
    while True:
        precio = (input("Precio: "))
        if precio.isdigit(): #validamos el precio
            precio = int(precio)
            if precio > 0:
                break
            else:
                print("Error: precio inválido.")
        else:
            print("Error: precio inválido.")

    while True:
        descuento = input("¿Tiene descuento? (S/N) ") #preguntamos si tiene descuento
        descuento = descuento.upper() #estandarizamos las opciones
        if descuento == "S": #aplicamos el descuento, y sumamos hacia el total descontado
            precio_descuento = (precio * 0.90)
            total_descuento = (total_descuento + precio_descuento)
            break
        elif descuento == "N":
            total_descuento = (total_descuento + precio)
            break
        else:
            print("Error: descuento debe ser S/N.")

    total = (total + precio) #sumamos hacia el total
    resumen += (f"Producto {i+1} - Precio: ${precio} Descuento (S/N): {descuento}\n\n") #guardamos los datos del producto en resumen

ahorro = (total - total_descuento) #calculamos el ahorro
promedio = (total_descuento / productos) #calculamos el promedio de precio de los productos

#imprimimos el resumen de la compra
print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {productos}")
print(resumen)
print(f"Total sin descuentos: ${total:.2f}\nTotal con descuentos: ${total_descuento:.2f}\nAhorro: ${ahorro:.2f}\nPromedio por producto: ${promedio:.2f}\n")

# Ejercicio 2

#inicializamos las credenciales y otras variables
usuario_correcto = "alumno"
clave_correcta = "python123"
mensaje_motivacional = "Los límites solo existen si los dejas existir."
intentos = 0

while intentos < 3: #ponemos un limite de 3 intentos
    usuario = input(f"Intento {intentos+1}/3 Usuario: ") #pedimos el nombre de usuario
    clave = input("Clave: ") #pedimos la clave al usuario

    if usuario == usuario_correcto and clave == clave_correcta: #si coinciden las credenciales damos acceso
        print("Acceso concedido.")
        print("1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")

        while True: #Loop para elección de opciones
            opcion = input("Opcion: ")

            if (opcion.isdigit()): #validamos la opcion
                opcion = int(opcion)

                if opcion > 4 or opcion < 1:
                    print("Error: opción fuera de rango.")

                elif opcion == 1: #opcion de (Estado)
                    print("Estado: Inscripto")                      

                elif opcion == 2: #opcion de (Cambiar clave)
                    while True:
                        clave_nueva = input("Clave nueva: ") #pedimos clave nueva
                        confirmacion = input("Confirmacion de clave:") #pedimos confirmacion de la misma
                        if len(clave_nueva) >= 6: #validamos que tenga 6+ caracteres
                            if clave_nueva == confirmacion: #verificamos que ambas coincidan
                                print("Clave actualizada")
                                clave_correcta = clave_nueva
                                break
                            elif clave_nueva != confirmacion:
                                print("Error: La clave y su confirmacion deben coincidir") 
                        else:
                            print("Error: mínimo 6 caracteres.")
                elif opcion == 3: #opcion de (Mensaje)
                    print(mensaje_motivacional) #mostramos mensaje motivacional en la terminal

                elif opcion == 4: #opcion de (Salir)
                    print("Sesión finalizada.")
                    break

            else:
                print("Error: ingrese un número válido.")
        break
    else:
        print("Error: credenciales inválidas.")
        intentos += 1 #sumamos un intento al limite
        
if intentos >= 3: #si pasa de 3 intentos se bloquea la cuenta
    print("Cuenta bloqueada.")

# ejercicio 3

#inicializamos las variables de las reservas y cantidad de reservas
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

cant_reservas = 0
cant_reservas2 = 0

while True:
    nombre = input("Nombre del operador: ") #pedimos el nombre al usuario
    if nombre.isalpha(): #validamos el nombre
        nombre = nombre.title() #estandarizamos la variable
        break

    else:
        print("El nombre solo debe contener letras.")

while True:
    print(f"Nombre de operador: {nombre}.") #nombre de operador y opciones
    print("1. Reservar turno\n2. Cancelar turno (por nombre)\n3. Ver agenda del día\n4. Ver resumen general\n5. Cerrar sistema ")
    opcion = input("opcion: ") #preguntamos la opcion que quiera el usuario

    if opcion.isdigit() and int(opcion) >= 1 and int(opcion) <= 5: #validamos la opcion
        opcion = int(opcion) #convertimos la opcion a un integer

        if opcion == 1: #opcion (reservar turno)
            while True:
                dia_reserva = input("Elegir dia (1=Lunes, 2=Martes): ")
                if dia_reserva.isdigit():
                    dia_reserva = int(dia_reserva)
                    if dia_reserva >= 1 and dia_reserva <= 2:
                        break
                    else:
                        print("Error: dia invalido.")
                else:
                    print("Error: dia invalido.")
            while True:
                nombre_reserva = input("Nombre de la reserva: ") #pedimos el nombre de reserva
                if nombre_reserva.isalpha():
                    break
                else:
                    print("Error: nombre invalido.")
            if dia_reserva == 1:
                if (nombre_reserva == lunes1 or nombre_reserva == lunes2 or nombre_reserva == lunes3 or nombre_reserva == lunes4):
                    print("ya hay una reserva en ese día.")
                elif lunes1 == "":
                    lunes1 = nombre_reserva
                    cant_reservas += 1
                elif lunes2 == "":
                    lunes2 = nombre_reserva 
                    cant_reservas += 1
                elif lunes3 == "":
                    lunes3 = nombre_reserva 
                    cant_reservas += 1
                elif lunes4 == "":
                    lunes4 = nombre_reserva
                    cant_reservas += 1
                else:
                    print("No hay turnos disponibles.") 
            elif dia_reserva == 2:
                if (nombre_reserva == martes1 or nombre_reserva == martes2 or nombre_reserva == martes3):
                    print("ya hay una reserva en ese día.")
                elif martes1 == "":
                    martes1 = nombre_reserva
                    cant_reservas2 += 1                     
                elif martes2 == "":
                    martes2 = nombre_reserva
                    cant_reservas2 += 1
                elif martes3 == "":
                    martes3 = nombre_reserva
                    cant_reservas2 += 1
                else:
                    print("No hay turnos disponibles.") 

        elif opcion == 2: #opcion (cancelar turno)
            while True:
                dia_cancelar = input("Elegir dia (1=Lunes, 2=Martes): ")
                if dia_cancelar.isdigit():
                    dia_cancelar = int(dia_cancelar)
                    if 1 <= dia_cancelar <= 2:
                        break
                    else:
                        print("Error: dia invalido.")
                else:
                    print("Error: dia invalido.")
            while True:
                nombre_reserva = input("Nombre de la reserva: ") #pedimos el nombre de la reserva
                if nombre_reserva.isalpha():
                    break
                else:
                    print("Error: nombre invalido.")
            if dia_cancelar == 1:
                if lunes1 == nombre_reserva:
                    lunes1 = ""
                    cant_reservas -= 1
                elif lunes2 == nombre_reserva:
                    lunes2 = ""
                    cant_reservas -= 1 
                elif lunes3 == nombre_reserva:
                    lunes3 = "" 
                    cant_reservas -= 1 
                elif lunes4 == nombre_reserva:
                    lunes4 = ""
                    cant_reservas -= 1 
                else:
                    print("No hay turnos con ese nombre reservados.") 
            elif dia_cancelar == 2:
                if martes1 == nombre_reserva:
                    martes1 = ""  
                    cant_reservas2 -= 1                    
                elif martes2 == nombre_reserva:
                    martes2 = ""
                    cant_reservas2 -= 1
                elif martes3 == nombre_reserva:
                    martes3 = ""
                    cant_reservas2 -= 1
                else:
                    print("No hay turnos con ese nombre reservados.") 
        elif opcion == 3: #opcion (agenda del dia)
            while True:
                dia_reserva = input("Elegir dia (1=Lunes, 2=Martes): ")
                if dia_reserva.isdigit():
                    dia_reserva = int(dia_reserva)
                    if 1 <= dia_reserva <= 2:
                        break
                    else:
                        print("Error: Día invalido.")
                else:
                    print("Error: Día invalido.")
            if dia_reserva == 1:
                print("Agenda Lunes:")
                print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
                print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
                print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
                print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
            elif dia_reserva == 2:
                print("Agenda Martes:")
                print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
                print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
                print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

        elif opcion == 4: #opcion (resumen general)
            print(f"turnos disponibles Martes: {3 - cant_reservas2}")
            print(f"turnos ocupados Martes: {cant_reservas2}")
            print(f"turnos disponibles Lunes: {4 - cant_reservas}")
            print(f"turnos ocupados Lunes: {cant_reservas}")
            if cant_reservas > cant_reservas2:
                print("El día lunes tiene mas turnos.")
            elif cant_reservas2 > cant_reservas:
                print("El día martes tiene mas turnos.")
            else:
                print("Ambos días tienes la misma cantidad de turnos.")
        elif opcion == 5: #opcion (cerrar sistema)
            print("Cerrando sistema.")
            break
        else:
            print("Error: opcion invalida.")
#ejercicio 4

#inicializamos las variables 
energia = 100 
tiempo = 12 
cerraduras_abiertas = 0 
alarma = False 
codigo_parcial = "" 

racha_forzar = 0 

while True:
    nombre = input("Ingrese nombre del agente: ") #pedimos el nombre al usuario
    if nombre.isalpha(): #validamos el nombre
        break
    else:
        print("Error: solo letras.")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3: # implementacion de bloqueo por alarma
        print("Bloqueo por alarma.")
        break
    
    #resumen de variables 
    print("--- ESTADO ---")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    print(f"Alarma: {alarma}")
    print(f"Código parcial: {codigo_parcial}")

    #opciones del jugador
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    while True:
        opcion = input("Elija una opcion: ") #pedimos una opcion al jugador
        if opcion.isdigit() and int(opcion) <= 3 and int(opcion) >= 1: #validamos la opcion
            opcion = int(opcion) #convertimos a integer
            break
        else:
            print("Error: solo numeros enteros del 1 al 3.")
    if opcion == 1: #opcion (Forzar cerradura)
        energia -= 20 #restamos energia y tiempo, tambien sumamos a la racha de forzar
        tiempo -= 2
        racha_forzar += 1

        if racha_forzar >= 3: #si la racha llega a 3 se traba la cerradura
            alarma = True
            print("La cerradura se trabó.")
            racha_forzar = 0
            continue

        if energia < 40 and not alarma: #riesgo de alarma al forzar
            while True:
                num = input("Riesgo de alarma, elija un numero entre 1-3.") #pedimos un numero del 1 al 3
                if num.isdigit() and int(num) <= 3 and int(num) >= 1: #validamos la opcion
                    num = int(num) #convertimos a integer
                    break
            if num == 3: #si coincide activamos la alarma
                alarma = True
                print("Se activo la alarma.")
        if not alarma: #si no se activa la alarma abrimos una cerradura
            cerraduras_abiertas += 1
            print("Abriste una cerradura.")
    elif opcion == 2: #opcion (hackear cerradura), restamos energia, tiempo y reseteamos la racha
        energia -= 10
        tiempo -= 3
        racha_forzar = 0

        print("Hackeando...")
        for i in range(4): #creamos el codigo parcial
            print(f"Progreso {i+1}/4.")
            codigo_parcial += "A"
        
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3: #abrimos la cerradura
            cerraduras_abiertas += 1
            print("Código completo se abrió la cerradura.")
    elif opcion == 3: #opcion (Descansar)
        tiempo -= 1
        racha_forzar = 0

        energia += 15
        if energia > 100: #limite de 100 para la energia
            energia = 100
        
        if alarma: #si la alarma esta activada restamos energia
            energia -= 10
            print("Descansar con la alarma consume energia extra.")
        
        print("Descansaste.")
#resultados del juego
print("--RESULTADO--")
if cerraduras_abiertas == 3:
    print("VICTORIA")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA")
elif alarma and tiempo <= 3:
    print("DERROTA (bloqueo)")

#ejercicio 5

#inicializamos las variables
turno_gladiador = True
vida_gladiador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado = 15
daño_enemigo = 12

print("--- BIENVENIDO A LA ARENA ---")

while True:
    nombre = input("Nombre del Gladiador: ") #pedimos el nombre al usuario
    if nombre.isalpha(): #validamos y estandarizamos
        nombre = nombre.title()
        break
    else:
        print("Error: Solo se permiten letras.")

print("=== INICIO DEL COMBATE ===")
while vida_enemigo > 0 and vida_gladiador > 0: #inicia el juego mientras alguno de los dos tenga vida 
    if turno_gladiador: #inicio turno de gladiador
        #mostramos estadisticas del jugador y el enemigo
        print(f"{nombre} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")

        #mostramos las opciones
        print("Elige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        while True:
            opcion = input("Opción: ") #pedimos la opcion al jugador
            if opcion.isdigit(): #validamos
                opcion = int(opcion) #convertimos a integer
                if opcion >= 1 and opcion <= 3:
                    if opcion == 1: #opcion (Ataque pesado)
                        if vida_enemigo < 20: #si el enemigo tiene menos de 20 de vida el gladiador da un golpe critico
                            vida_enemigo -= float(ataque_pesado * 1.5)
                            print(f">>¡Atacaste al enemigo por {float(ataque_pesado * 1.5)} puntos de daño!")
                            turno_gladiador = False #damos el turno al enemigo
                        else: #ataque pesado (sin golpe critico)
                            print(f">>¡Atacaste al enemigo por {ataque_pesado} puntos de daño!")
                            vida_enemigo -= ataque_pesado 
                            turno_gladiador = False #damos el turno al enemigo
                    elif opcion == 2: #opcion (Rafaga de golpes)
                        print(">> ¡Inicias una ráfaga de golpes! ")
                        for i in range(3): #damos 3 golpes seguidos de 5 de daño
                            vida_enemigo -= 5
                            print("> Golpe conectado por 5 de daño")
                        turno_gladiador = False #damos el turno al enemigo
                    elif opcion == 3: #opcion (Curar)
                        if pociones > 0: #si tenemos pociones disponibles damos +30 de vida al jugador
                            print(">>¡Te curaste 30 puntos!")
                            vida_gladiador += 30
                            pociones -= 1
                            turno_gladiador = False
                        else: #si no tenemos pociones solamente perdemos el turno
                            print(">>¡No quedan pociones!")
                            turno_gladiador = False
                    break
                else:
                    print("Error: Ingrese un número válido.")
            else:
                print("Error: Ingrese un número válido.")
    elif not turno_gladiador: #una vez pasado nuestro turno es el turno del enemigo
        if vida_enemigo > 0: #mientras que tenga vida el enemigo resta 12 de daño
            vida_gladiador -= daño_enemigo
            print(f">>¡El enemigo te atacó por {daño_enemigo} puntos de daño!")
            print("=== NUEVO TURNO === ")
            turno_gladiador = True #devolvemos el turno al gladiador
if vida_gladiador > 0: #si el gladiador sobrevive gana la batalla
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
elif vida_enemigo > 0: #si el enemigo sobrevive el gladiador pierde la batalla
    print(f"DERROTA. Has caído en combate.")