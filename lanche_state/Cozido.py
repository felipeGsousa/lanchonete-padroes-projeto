from lanche_state.State import State
from modelo.Lanche import Lanche

class Cozido(State):

    def __init__(self, lanche:Lanche) -> None:
        super().__init__(lanche)

    def cru(self) -> None:
        return f"Status ==> {self._lanche.getNome()} cozido, pronto para montar!!! \n"

    def cozinhando(self) -> None:
        return f"Status ==> {self._lanche.getNome()} cozido, pronto para montar!!! \n"

    def cozido(self) -> None:
        return f"Status ==> {self._lanche.getNome()} cozido, pronto para montar!!! \n"

    def montando(self) -> None:
        return f"Status ==> {self._lanche.getNome()} cozido, pronto para montar!!! \n"

    def pronto(self) -> None:
        return f"Status ==> {self._lanche.getNome()} cozido, pronto para montar!!! \n"