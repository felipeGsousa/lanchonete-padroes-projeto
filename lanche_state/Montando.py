from lanche_state.State import State
from modelo.Lanche import Lanche

class Montando(State):
    
    def __init__(self, lanche:Lanche) -> None:
        super().__init__(lanche)

    def cru(self) -> None:
        return f"## {self._lanche.getNome()} já está sendo montado!!! ##\n"

    def cozinhando(self) -> None:
        return f"## {self._lanche.getNome()} já está sendo montado!!! ##\n"

    def cozido(self) -> None:
        return f"## {self._lanche.getNome()} já está sendo montado!!! ##\n"

    def montando(self) -> None:
        return f"## {self._lanche.getNome()} já está sendo montado!!! ##\n"

    def pronto(self) -> None:
        return f"## {self._lanche.getNome()} já está sendo montado!!! ##\n"