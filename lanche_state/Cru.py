from lanche_state.State import State
from modelo.Lanche import Lanche

class Cru(State):

    def __init__(self, lanche:Lanche) -> None:
        super().__init__(lanche)
           
    def cru(self) -> None:
        return f"## {self._lanche.getNome()} cru, pronto para ser cozido!!! ##\n"

    def cozinhando(self) -> None:
        return f"## {self._lanche.getNome()} cru, pronto para ser cozido!!! ##\n"

    def cozido(self) -> None:
        return f"## {self._lanche.getNome()} cru, pronto para ser cozido!!! ##\n"

    def montando(self) -> None:
        return f"## {self._lanche.getNome()} cru, pronto para ser cozido!!! ##\n"

    def pronto(self) -> None:
        return f"## {self._lanche.getNome()} cru, pronto para ser cozido!!! ##\n"