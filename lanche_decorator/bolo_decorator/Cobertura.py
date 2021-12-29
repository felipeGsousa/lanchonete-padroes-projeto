from lanche_decorator.bolo_decorator.Bolo_decorator import Bolo_decorator


class Cobertura(Bolo_decorator): 
    def operation(self) -> str:
        print("- Adiciona cobertura\n")