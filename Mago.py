from Personaje import Personaje

class Mago(Personaje):
    
    """
    Personaje tipo mago. Su daño es incrementado por 1.5 gracias a su magia.
    """
    
    def __init__(self, nombre, daño, vida, def_fisica, def_magica, magia):
        super().__init__(nombre, daño, vida, def_fisica, def_magica)
        self.magia = magia
        
    def __str__(self):
        return f'{self.nombre} 🧙  nivel {self.nivel} | ☄️  {self.daño} | ❤️  {self.vida} | 🛡️  fisica: {self.def_fisica} | 🛡️  magica: {self.def_magica} | -Magia: {self.magia} \n'
          
    def atacar(self, enemigo):
        daño_realizado = self.daño * 1.5 - enemigo.def_magica
        if daño_realizado <= 0:
            return f'{self.nombre} no ha causado daño'
        elif daño_realizado > 0:
            enemigo.vida -= daño_realizado
            print(f'{self.nombre} ⚔️  {enemigo.nombre} causandole {daño_realizado} de daño magico | ❤️  restante de {enemigo.nombre}: {enemigo.vida}\n')  
