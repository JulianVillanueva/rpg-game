from abc import ABC, abstractmethod
from os import system
import logging

logging.basicConfig(level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s')

class Personaje(ABC): 
    
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
     
class Atributo_Invalido(Exception):
    """
    No es recomendable agregar mas logica adicional como por ejemplo:
    si el valor es negativo o no sobrecarga su responsabilidad y hace que sea más difícil de entender y mantener.
    """
    pass
     
        
def inputs_personaje():
    
    tipo_arma = ''
    
    while True:
        try:
            tipo = input('Digite el tipo de personaje (guerrero/mago): ').lower().strip()
            if tipo != 'guerrero' and tipo != 'mago':
                limpiar_pantalla()
                logging.error(f'Tipo de personaje inválido {tipo}')
                raise ValueError('Tipo de personaje inválido')
            
            
            nombre_personaje = input('Nombre del personaje: ').strip()
            # Validacion para evitar numeros, vacios, espacios, caracteres especiales. 
            if not nombre_personaje.isalpha():
                logging.error(f'Nombre INCORRECTO (Numeros, caracteres especiales) {nombre_personaje}')
                raise ValueError('El nombre no debe estar vacio ni contener: Numeros, caracteres especiales')
            # or not nombre_personaje or nombre_personaje.isspace()
            
            daño = int(input('Daño del personaje: '))
            if daño <= 0:
                raise Atributo_Invalido("El daño debe ser un número entero positivo")

            vida = int(input('Vida del personaje: '))
            if vida <= 0:
                raise Atributo_Invalido("La vida debe ser un número entero positivo")

            defensa_fisica = int(input('Defensa fisica del personaje: '))
            if defensa_fisica < 0:
                raise Atributo_Invalido("La defensa física debe ser un número entero no negativo")

            defensa_magica = int(input('Defensa magica del personaje: '))
            if defensa_magica < 0:
                raise Atributo_Invalido("La defensa mágica debe ser un número entero no negativo")
            
            if tipo == 'guerrero':
                tipo_arma = input('Digite la espada del personaje: ')
            elif tipo == 'mago':
                tipo_arma = input('Digite la magia del personaje: ')
        
            return tipo, nombre_personaje, daño, vida, defensa_fisica, defensa_magica, tipo_arma
        
        except ValueError as e:
            print(f'ERROR. Datos incorrectos. {e}')
            continue
        except Atributo_Invalido as e: #Entra a esta excepcion cuando se ingresa un atributo negativo
            print(f'ERROR personalizado. Datos incorrectos. {e}')
            continue
        except Exception as e:
            print(f'ERROR excepcion. Datos incorrectos. {e}')
            continue
    
def limpiar_pantalla():
    
    system('clear')
    
def listar_personajes(personajes):
    
    for personaje in personajes:
        print(f'''{personajes.index(personaje)+1}. {personaje}''')
            
def valida_personajes(lista_personajes = list):
    
    if len(lista_personajes) < 2:
        limpiar_pantalla()
        print('ERROR. No hay suficientes personajes para hacer eso. \n')
        return False
        