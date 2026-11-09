from no import No

class ListaLigada:

    def __init__(self):
        self.primeiro: No = None
        self.tamanho = 0


    def inserir_inicio(self, item):
        """ Adiciona no início da lista """
        
        novo_no = No(item)
        novo_no.proximo = self.primeiro
        self.primeiro = novo_no
        self.tamanho += 1


    def __str__(self):
        """ Monta uma string com os itens da lista """

        no_atual = self.primeiro
        string = ""

        while no_atual:
            string += str(no_atual.item) + " -> "
            no_atual = no_atual.proximo

        return string + "null"


    def adicionar(self, item):
        """ Adiciona no fim da lista """

        novo_no = No(item)
        if self.primeiro is None:
            self.primeiro = novo_no
        else:
            atual = self.primeiro
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no
        self.tamanho += 1


    def pesquisar(self, item):
        """ Retorna True caso o item procurado exista na lista e
        False, em caso contrário. """

        pass


    def obter(self, posicao):
        """ Retorna o item guardado em uma determinada posição da lista.
        Caso a posição não exista na lista, retorna None. """

        pass


    def inserir(self, posicao, item):
         """ Adiciona um item em uma posição da lista
        empurrando os demais itens para o fim da lista.
        Se a posição não é válida, retorna False. """
         
         pass


    def remover_inicio(self):
        """ Remove o primeiro item da lista e o retorna """

        pass        


    def remover(self, posicao):
        """ Remove um item de uma posição da lista
        e puxa os demais itens para o início da lista.
        Ao final, retorna True. Caso a posição não exista na lista, retorna False. """

        pass


    def remover_item(self, item):
        """ Remove um item existente na lista e retorna True.
        Caso o item não seja encontrado, retorna False. """

        pass
