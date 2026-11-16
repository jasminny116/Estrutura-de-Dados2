from lista_ligada import ListaLigada

class Pilha:

    def __init__(self):
        self._elementos = ListaLigada()


    def empilhar(self, item):
        self._elementos.inserir_inicio(item)


    def desempilhar(self):
        return self._elementos.remover_inicio()


    def vazia(self):
        return self._elementos.vazia()


    def topo(self):
        if self.vazia(): 
            return None
        return self._elementos.primeiro.item


    def tamanho(self):
        return self._elementos.tamanho
