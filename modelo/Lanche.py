from abc import abstractmethod


class Lanche:
    _nome = ""
    _state = None

    def __init__(self) -> None:
        pass
        
    @abstractmethod
    def getNome(self) -> None:
        pass

    @abstractmethod
    def getStatus(self) -> None:
        pass
    
    @abstractmethod
    def setStatus(self) -> None:
        pass