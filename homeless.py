import random
"""actividad en clase del bagabundo"""
class Homeless:
    def __init__(self, name):
        self.name = name

class StandarHomeless(Homeless):
    def __innit__(self, name):
        super().__init__(name)

    def walk(self):
        return random.choice([(1,0),(-1,0),(0,1),(0,-1)])

"""Super es para heredar de la clase padre"""



"""el random.choice tiene 2 argumentos 1,0. pero puede tener mas de estos como unos 5 o 6 dimensiones o datos"""