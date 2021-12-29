from modelo.Bolo import Bolo

class Bolo_decorator(Bolo):

    _bolo: Bolo = None

    def __init__(self, bolo: Bolo) -> None:
        self._bolo = bolo

    @property
    def bolo(self) -> str:
        return self._bolo

    def operation(self) -> str:
        return self._bolo.operation()