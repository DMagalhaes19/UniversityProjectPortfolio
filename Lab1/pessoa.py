import abc

class Pessoas(abc.ABC):
    def __init__(self,nome):
        self.nome = nome
    
    def obter_nome(self):
        return self.nome        