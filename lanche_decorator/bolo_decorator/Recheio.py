from lanche_decorator.bolo_decorator.Bolo_decorator import Bolo_decorator


class Recheio(Bolo_decorator): 
    def operation(self) -> str:
        print("Decorador Bolo ==> Adiciona recheio\n")