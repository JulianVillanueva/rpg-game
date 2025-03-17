from Personaje import *
from Mago import Mago
from Guerrero import Guerrero
from Fabrica import FabricaPersonajes

def partida():
    
    guerrero1 = Guerrero('Hercules', 10, 50, 11, 10, 'Oro')
    guerrero2 = Guerrero('Dave', 9, 50, 9, 6, 'Hierro')
    guerrero3 = Guerrero('Ragnar', 13, 50, 11, 6, 'Diamante')
    mago1 = Mago('Lucas', 12, 50, 7, 11, 'Hielo')
    personajes = [guerrero1, guerrero2, guerrero3, mago1]
    
    while True:
        
        print('\nDEVSENIOR GAME RPG\n')
        print('1. Personaje nuevo')
        print('2. Duelo a muerte')
        print('3. Listado de personajes')
        print('4. Subir de nivel')
        print('5. Recuperar vida')
        print('6. Salir')
        
        opcion = int(input('\nElija una opcion (1-6): '))
        
        if opcion == 1:
            atributos = inputs_personaje()
            personaje = FabricaPersonajes.crear_personaje(*atributos)
            personajes.append(personaje)
        elif opcion == 2:
            if valida_personajes(personajes) == False:
                continue
            else:
                limpiar_pantalla()
                print('Escoja sus luchadores:')
                listar_personajes(personajes)
                personaje1 = personajes[int(input('Luchador uno: '))-1]
                personaje2 = personajes[int(input('Luchador dos: \n'))-1]
                personaje1.duelo_a_muerte(personaje2, personajes)
        elif opcion == 3:
            if valida_personajes(personajes) == False:
                continue
            else:
                listar_personajes(personajes) 
            
        elif opcion == 4:
            if valida_personajes(personajes) == False:
                continue
            else:
                limpiar_pantalla()
                print('¿Cual personaje desea subir de nivel?: ')
                listar_personajes(personajes)
                personaje = personajes[int(input('Personaje: '))-1]
                personaje.subir_nivel()
        elif opcion == 5:
            if valida_personajes(personajes) == False:
                continue
            else:
                limpiar_pantalla()
                print('¿Cual personaje desea recuperar vida?: ')
                listar_personajes(personajes)
                personaje = personajes[int(input('Personaje: '))-1]
                personaje.pocion_vida()
        elif opcion == 6:
            print('\nGracias por jugar !')
            break
        else:
            limpiar_pantalla()
            print('ERROR.Ingrese una opcion valida')
    
partida()