import random
"""actividad en clase del bagabundo"""
class Homeless:
    def __innit__(self, name):
        self.name = name

class StandarHomeless(Homeless):
    def __innit__(self, name):
        super().__innit__(name)

    def walk(self):
        return random.choice([(1,0),(-1,0),(0,1),(0,-1)])