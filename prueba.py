
class Gato:
    def __init__(self,name):
        self.name = name
    def rename(self,toga):
        self.name = toga.name
    def __repr__(self):
        return 'soy un lindo gatico' + self.name
    
p = Gato('manchas')
f = Gato('pepe')

x = 'hola'
print(x.center(6,'3'))