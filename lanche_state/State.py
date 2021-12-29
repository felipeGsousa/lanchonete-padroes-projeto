from __future__ import annotations
from abc import ABC, abstractmethod

class State(ABC):

    _lanche = None
    
    def __init__(self, lanche) -> None:
        self._lanche = lanche
        super().__init__()

    @abstractmethod
    def cru(self) -> None:
        pass

    @abstractmethod
    def cozinhando(self) -> None:
        pass

    @abstractmethod
    def cozido(self) -> None:
        pass

    @abstractmethod
    def montando(self) -> None:
        pass

    @abstractmethod
    def pronto(self) -> None:
        pass