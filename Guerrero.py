from Personaje import Personaje

class Guerrero(Personaje):
    
    """
    Personaje tipo Guerrero. Su daño fisico es incrementado x2 gracias a su espada
    """
    
    def __init__(self, nombre, daño, vida, def_fisica, def_magica, espada):
        super().__init__(nombre, daño, vida, def_fisica, def_magica)
        self.espada = espada
    
    def __str__(self):
        return f'{self.nombre} 🤺  nivel {self.nivel} | 🗡️  {self.daño} | ❤️  {self.vida} | 🛡️  Fisica: {self.def_fisica} | 🛡️  Magica: {self.def_magica} | -Espada: {self.espada}\n'
        
    def atacar(self, enemigo):
        daño_realizado = self.daño * 2 - enemigo.def_fisica
        if daño_realizado <= 0:
            return f'{self.nombre} no ha causado daño'
        elif daño_realizado > 0:
            enemigo.vida -= daño_realizado
            print(f'{self.nombre} ⚔️  {enemigo.nombre} causandole {daño_realizado} de daño fisico | ❤️  restante de {enemigo.nombre}: {enemigo.vida}\n')
            