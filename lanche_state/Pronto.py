from lanche_state.State import State
from modelo.Lanche import Lanche

class Pronto(State):

    def __init__(self, lanche:Lanche) -> None:
        super().__init__(lanche)

    def cru(self) -> None:
        return (f">>{self._lanche.getNome()} já está pronto!!!\n\n")

    def cozinhando(self) -> None:
        return (f">>{self._lanche.getNome()} já está pronto!!!\n\n")

    def cozido(self) -> None:
        return (f">>{self._lanche.getNome()} já está pronto!!!\n\n")

    def montando(self) -> None:
        return (f">>{self._lanche.getNome()} já está pronto!!!\n\n")

    def pronto(self) -> None:
        return f">>{self._lanche.getNome()} está pronto para ser comido!!!\n\n"
     