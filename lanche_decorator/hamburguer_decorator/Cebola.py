from lanche_decorator.hamburguer_decorator.Hamburguer_decorator import Hamburguer_decorator


class Cebola(Hamburguer_decorator): 
    def operation(self) -> str:
        print("- Adiciona cebola\n")