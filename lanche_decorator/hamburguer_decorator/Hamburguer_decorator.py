from modelo.Hamburguer import Hamburguer

class Hamburguer_decorator(Hamburguer):

    _hamburguer: Hamburguer = None

    def __init__(self, hamburguer: Hamburguer) -> None:
        self._hamburguer = hamburguer

    @property
    def hamburguer(self) -> str:
        return self._hamburguer

    def operation(self) -> str:
        return self._hamburguer.operation()