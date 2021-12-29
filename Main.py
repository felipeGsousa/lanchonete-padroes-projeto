from modelo.Bolo import Bolo
from modelo.Hamburguer import Hamburguer

from lanche_state.Lanche_manager import Manager

from lanche_strategy.Cozinhar import Cozinhar
from lanche_strategy.Montar import Montar

from lanche_decorator.bolo_decorator.Cobertura import Cobertura
from lanche_decorator.bolo_decorator.Recheio import Recheio

from lanche_decorator.hamburguer_decorator.Tomate import Tomate
from lanche_decorator.hamburguer_decorator.Pao import Pao
from lanche_decorator.hamburguer_decorator.Pickles import Pickles
from lanche_decorator.hamburguer_decorator.Cebola import Cebola
from lanche_decorator.hamburguer_decorator.Cheddar import Cheddar
from lanche_decorator.hamburguer_decorator.Alface import Alface

print("===============================#(Início)#===============================\n")

bolo = Bolo()
bolo = Manager(bolo)
bolo.iniciaPreparo(Cozinhar())
bolo.lancheCozido()
bolo.paraMontagem(Montar())
Cobertura(Recheio(bolo).operation()).operation()
bolo.montadoPronto()

print("=======================================================================\n")

hamburguer = Hamburguer()
hamburguer = Manager(hamburguer)
hamburguer.iniciaPreparo(Cozinhar())
hamburguer.lancheCozido()
hamburguer.paraMontagem(Montar())
Pickles(Cheddar(Cebola(Alface(Tomate(Pao(hamburguer).operation()).operation()).operation()).operation()).operation()).operation()
hamburguer.montadoPronto()

print("=======================================================================\n")

bolo = Bolo()
bolo = Manager(bolo)
bolo.iniciaPreparo(Cozinhar())
bolo.lancheCozido()
bolo.paraMontagem(Montar())
Cobertura(bolo).operation()
bolo.montadoPronto()

print(f"=======================================================================\n")

hamburguer = Hamburguer()
hamburguer = Manager(hamburguer)
hamburguer.iniciaPreparo(Cozinhar())
hamburguer.lancheCozido()
hamburguer.paraMontagem(Montar())
Pickles(Cheddar(Pao(hamburguer).operation()).operation()).operation()
hamburguer.montadoPronto()

print("=================================#(Fim)#=================================\n")