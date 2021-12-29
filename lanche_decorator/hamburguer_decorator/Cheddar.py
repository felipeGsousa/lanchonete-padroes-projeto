from lanche_decorator.hamburguer_decorator.Hamburguer_decorator import Hamburguer_decorator


class Cheddar(Hamburguer_decorator): 
    def operation(self) -> str:
        print("Decorador Hamburguer ==> Adiciona cheddar\n")