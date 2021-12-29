from __future__ import annotations
from lanche_state.Cru import Cru
from lanche_state.Cozido import Cozido
from lanche_state.Cozinhando import Cozinhando
from lanche_state.Montando import Montando
from lanche_state.Pronto import Pronto
from lanche_strategy.Cozinhar import Cozinhar
from lanche_strategy.Preparacao_service import Preparacao
from lanche_strategy.Strategy import Strategy
from modelo.Lanche import Lanche

class Manager: 

    _lanche = None
    cru = None
    cozinhando = None
    cozido = None
    montando = None
    pronto = None

    def __init__(self, lanche):
        self._lanche = lanche
        self.cru = Cru(lanche)
        self.cozinhando = Cozinhando(lanche)
        self.cozido = Cozido(lanche)
        self.montando = Montando(lanche)
        self.pronto = Pronto(lanche)
        self._lanche.setStatus(self.cru.cru())
    
    preparacao = Preparacao

    def iniciaPreparo(self, strategy: Strategy):
        try:
            print(self._lanche.getStatus())
            self.preparacao.prepara_lanche(strategy)
            self._lanche.setStatus(self.cozinhando.cozinhando())
            print(self._lanche.getStatus())
        except Exception as e:
            print(e) 


    def lancheCozido(self):
        try:
            self._lanche.setStatus(self.cozido.cozido())
            print(self._lanche.getStatus())   
        except Exception as e:
            print(e)


    def paraMontagem(self, strategy: Strategy):
        try:
            self.preparacao.prepara_lanche(strategy)
            self._lanche.setStatus(self.montando.montando())
            print(self._lanche.getStatus())        
        except Exception as e:
            print(e)


    def montadoPronto(self):
        try:
            self._lanche.setStatus(self.pronto.pronto())
            print(self._lanche.getStatus())
        except Exception as e:
            print(e)
   

        





