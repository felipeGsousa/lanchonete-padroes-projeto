from lanche_strategy.Strategy import Strategy


class Preparacao:
    def prepara_lanche(strategy: Strategy):
        try:
            strategy.muda_status()
        except:
            raise("Não consigo fazer isso")
            
