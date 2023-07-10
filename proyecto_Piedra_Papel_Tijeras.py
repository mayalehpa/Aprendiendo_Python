import random #Esta función es para poder usar valores aleatorios según la variable que declare

options = ('piedra', 'papel', 'tijeras') #en esta linea de código estoy creando una tupla

computer_wins =0
jugador_wins = 0

rounds=1

print("""
      [  Vamos a iniciar con el juego Piedra, Papel o Tijeras ]
                  🌷🌷🌷 Elige una opción 🌷🌷🌷
      """)

while True: 
    print('*' * 10)
    print('Round', rounds)
    print ('*' * 10)

    print('computer_wins', computer_wins)
    print('jugador_wins', jugador_wins)


    jugador = input("Jugador . elige: piedra, papel o tijeras: ")
    jugador = jugador.lower() #la función .lower es un método de string para indicar que la palabra ingresada se convierta aútomaticamente en minúscula.

    rounds += 1 #Está linea de código es para que me sume 1 cada ronda

    if not jugador in options:
        print('Por favor, elige una opción válida') #puedo comprobar si un elemento esta en la tupla
        continue # exit() esta linea hace que el código no se siga ejecutando o puedo usar continue

    computer = random.choice(options) #en esta linea de código se esta utilizando la función random (importada anteriormente) y ejecutando la variable options que es una tupla.

    print('jugador =>', jugador)
    print('computer =>', computer )
    print ('🌷' * 10)

    if jugador == computer:
        print("Es un empate!")
        

    elif jugador == "piedra":
        if computer == "papel":
            print ('🌷' * 10)
            print("computer gana!, Papel envuelve Piedra.")
            computer_wins += 1 #esto es para sumarle la ganancia en cada ronda
        else:
            print("Jugador gana. Piedra rompe tijeras.")
            jugador_wins += 1

    elif jugador == "papel":
        if computer == "tijeras":
            print ('🌷' * 10)
            print("computer gana. Tijeras cortan papel.")
            computer_wins += 1
        else:
            print("Jugador gana. Papel envuelve piedra.")
            jugador_wins += 1

    elif jugador == "tijeras":
        if computer == "piedra":
            print ('🌷' * 10)
            print("computer gana. Piedra rompe tijeras.")
            computer_wins += 1
        else:
            print("Jugador gana. Tijeras cortan papel.")
            jugador_wins += 1
            
    '''else:
        print("Entrada inválida. Asegúrate de elegir entre piedra, papel o tijeras.")

    La linea anterior me permite mostrar al usuario cuando este ingresando una opción diferente a las tres iniciales, pero la mejor opción es usar el código de la linea 8 y 9
    '''

    if computer_wins == 2:
        print(f'🎉🎉🎉El ganador es la computadora con {computer_wins} puntos !🎉🎉🎉')
        break 
    if jugador_wins == 2:
        print (f'🎊🎊🎊 El ganador es el jugador con {jugador_wins} puntos! 🎊🎊🎊')
        break