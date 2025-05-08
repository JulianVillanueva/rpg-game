from abc import ABC, abstractmethod
from os import system
import logging
from Validaciones import *

logging.basicConfig(level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s')

class Personaje(): 
    
    nivel = 1
    pocion = 1
    
    def __init__(self, nombre, daño, vida, def_fisica, def_magica):
        self.nombre = nombre
        self.daño = daño
        self.vida = vida
        self.def_fisica = def_fisica
        self.def_magica = def_magica
        
    @abstractmethod
    def __str__(self):
        pass 
    
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self, personajes):
        self.vida = 0
        print(f'{self.nombre} ha muerto')
        personajes.remove(self)
        
    def pocion_vida(self):
        
        if self.vida > 0:
            if self.pocion > 0:
                self.vida += 25
                self.pocion -= 1
                print(f'{self.nombre} ha recuperado 25 ❤️ . Tiene {self.pocion} pociones de vida restantes.\n')
            else:
                print(f'❌  {self.nombre} no tiene pociones de vida.\n')
        else:
            print('\nEl personaje no esta vivo 💀 \n')
        
    def subir_nivel(self):
        
        if self.vida > 0:
            self.nivel += 1     
            self.daño += 1
            self.vida += 10
            self.def_fisica += 1
            self.def_magica += 1
            self.pocion += 1
            print(f'{self.nombre} ha subido al nivel {self.nivel}  🆙 ✔️\n')
        else:
            print('\nEl personaje no esta vivo 💀 \n')
        
    @abstractmethod
    def atacar(self, enemigo):
        pass
    
    def duelo_a_muerte(self, enemigo, personajes):
        
        while self.esta_vivo() and enemigo.esta_vivo():
            self.atacar(enemigo)
            if not enemigo.esta_vivo(): 
                break    
            enemigo.atacar(self)
        ganador = self if self.esta_vivo() else enemigo
        perdedor = enemigo if self.esta_vivo() else self
        perdedor.morir(personajes)
        print(f'{ganador.nombre} ha ganado la batalla  🎉')
        print(f'Vida final: 👑 {ganador.nombre} (❤️  {ganador.vida}) vs 💀 {perdedor.nombre} (❤️  {perdedor.vida})\n')
        ganador.subir_nivel()
     
def inputs_personaje():
    
    limpiar_pantalla()
    
    tipo_arma = ''
    
    while True:
        try:
            tipo = validar_tipo(input('Digite el tipo de personaje (guerrero/mago): '))
            break
        except ValueError as e:
            print(f'ERROR. Datos incorrectos. {e}')
            continue
            
    while True:   
        try:     
            nombre_personaje = validar_nombre(input('Nombre del personaje: '))
            break
        except ValueError as e:
            print(f'ERROR. Datos incorrectos. {e}')
            continue
            
    daño = validar_atributo_numerico('Daño del personaje: ')
    vida = validar_atributo_numerico('Vida del personaje: ')
    defensa_fisica = validar_atributo_numerico('Defensa física del personaje: ')
    defensa_magica = validar_atributo_numerico('Defensa mágica del personaje: ')

    while True:
        try:
            if tipo == 'guerrero':
                tipo_arma = input('Digite la espada del personaje: ')
            elif tipo == 'mago':
                tipo_arma = input('Digite la magia del personaje: ')
            if not tipo_arma.strip():
                raise ValueError(f'El tipo de arma no puede estar vacio\n')
            if not tipo_arma.isalpha():
                raise ValueError(f'El tipo de arma que ingresaste no es valido: {tipo_arma}\n')
            break
        except Exception as e:
            print(f'Error: {e}')
    return tipo, nombre_personaje, daño, vida, defensa_fisica, defensa_magica, tipo_arma
    
def listar_personajes(personajes):
    
    for personaje in personajes:
        print(f'''{personajes.index(personaje)+1}. {personaje}''')  