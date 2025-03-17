from Mago import Mago
from Guerrero import Guerrero

class FabricaPersonajes:
    
    @staticmethod
    def crear_personaje(tipo, nombre, daño, vida, def_fisica, def_magica, tipo_arma):
        if tipo == "guerrero":
            return Guerrero(nombre, daño, vida, def_fisica, def_magica, tipo_arma)
        elif tipo == "mago":
            return Mago(nombre, daño, vida, def_fisica, def_magica, tipo_arma)
        else:
            raise ValueError("Tipo de personaje no válido")
        
