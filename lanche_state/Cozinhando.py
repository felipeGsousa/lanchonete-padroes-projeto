from lanche_state.State import State
from modelo.Lanche import Lanche

class Cozinhando(State):
    
    def __init__(self, lanche:Lanche) -> None:
        super().__init__(lanche)

    def cru(self) -> None:
        return f"## Cozinhando o {self._lanche.getNome()} ##\n"

    def cozinhando(self) -> None:
        return f"## Cozinhando o {self._lanche.getNome()} ##\n"

    def cozido(self) -> None:
        return f"## Cozinhando o {self._lanche.getNome()} ##\n"

    def montando(self) -> None:
        return f"## Cozinhando o {self._lanche.getNome()} ##\n"

    def pronto(self) -> None:
        return f"## Cozinhando o {self._lanche.getNome()} ##\n"