import logging
from os import system

class Atributo_Invalido(Exception):
    pass

def limpiar_pantalla():
    
    system('clear')

def validar_tipo(tipo):
    
    tipo = tipo.strip().lower()
    if tipo != 'guerrero' and tipo != 'mago':
            logging.error(f'Tipo de personaje inválido: {tipo}')
            raise ValueError('Ingrese un Tipo de personaje entre (guerrero/mago)\n')
    limpiar_pantalla()
    return tipo

def validar_nombre(nombre):
    
    """Valida que el nombre no esté vacío y solo contenga letras y espacios"""
    nombre = nombre.strip()
    if not nombre: #or not nombre_personaje or nombre_personaje.isspace()
        logging.error("Nombre vacío ingresado")
        raise ValueError("El nombre no puede estar vacío\n")
    if not nombre.isalpha():
        logging.error(f"Nombre con caracteres inválidos: {nombre}")
        raise ValueError("El nombre solo puede contener letras\n")
    limpiar_pantalla()
    return nombre

def validar_atributo_numerico(nombre_atributo):
    while True:
        try:
            valor = input(f'{nombre_atributo}')
            num = int(valor)
            if num < 0:
                logging.error(f"{nombre_atributo} negativo: {num}")
                raise Atributo_Invalido(f"{nombre_atributo} debe ser un número entero no negativo")
            return num
        
        except Atributo_Invalido as e:
            print(f'ERROR PERSONALIZADO: {e}')
        except ValueError as e:
            print(f"ERROR: {nombre_atributo} debe ser un número entero válido")
        
def valida_personajes(lista_personajes = list):
    
    if len(lista_personajes) < 2:
        limpiar_pantalla()
        print('ERROR. No hay suficientes personajes para hacer eso. \n')
        return False