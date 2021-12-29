from modelo.Lanche import Lanche


class Hamburguer(Lanche):

    _nome = "Hamburguer"
    _state = None
    
    def __init__(self):
        super().__init__()
        
    def getNome(self):
        return self._nome

    def getStatus(self):
        return self._state

    def setStatus(self, state):
        self._state = state
