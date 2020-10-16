#metodo estactico decoarador
def singleton(cls):
    
    instances = dict()

    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrap
@singleton
class Pokemon(object):
    """
    Clase pokenmon
    """
    # __instance = None
    # # metodo statico
    # def __new__(cls):
    #     if Pokemon.__instance is None:
    #         print('Nueva instancia')
    #         Pokemon.__instance=object.__new__(cls)
    #     return Pokemon.__instance
    def __init__(self,nombre,vidad,ataque):
        self.nombre = nombre
        self.vidad = vidad
        self.ataque = ataque
@singleton
class Entrenador(object):
    """
    clase de entrenador
    """
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
if  __name__== '__main__':
    pokemon1 = Pokemon('picachu',100,20)
    pokemon2 = Pokemon('chamander',100,15)
    entrenador1 = Entrenador('ask',10)
    entrenador2 = Entrenador('Misty',11)
    # validad is es la misma clase
    print (pokemon1 is pokemon2)
    print (entrenador1 is entrenador2)