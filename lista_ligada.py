from no import No

class ListaLigada:
    def __init__(self):
        self.primeiro: No = None
        self.tamanho = 0
        # Custo de inicializar a lista vazia: O(1)
    
    def inserir_inicio(self, item):
        """ Adiciona no início da lista """
        novo_no = No(item)
        novo_no.proximo = self.primeiro
        self.primeiro = novo_no
        self.tamanho += 1
        # Custo pra inserir no inicio: O(1)
       
    def __str__(self):
        """ Monta uma string com os itens da lista """
        no_atual = self.primeiro
        elementos = []

        while no_atual:
            elementos.append(str(no_atual.item))
            no_atual = no_atual.proximo

        return " -> ".join(elementos) + (" -> " if elementos else "") + "null"

        # Custo para percorre todos os nó : O(n)

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

        # Custo pra percorrer a lista até encontrar o último nó: O(n), se tiver vazia é O(1).

    def pesquisar(self, item):
        """ Retorna True caso o item exista na lista.
        Caso contrário, retorna False. """

        atual = self.primeiro

        while atual:
            if atual.item == item:
                return True

            atual = atual.proximo

        return False

        # Custo: O(n), no pior caso, percorre todos os nós até encontrar o item ou chegar ao final da lista.


    def obter(self, posicao):
        """ Retorna o item guardado em uma determinada posição.
        Caso a posição não exista, retorna None. """

        if posicao < 0 or posicao >= self.tamanho:
            return None

        atual = self.primeiro
        indice = 0

        while indice < posicao:
            atual = atual.proximo
            indice += 1

        return atual.item

        # Custo: O(n), percorre os nós até alcançar a posição que deseja

    def inserir(self, posicao, item):
        """ Adiciona um item em uma posição da lista,
        empurrando os demais itens para o fim.
        Se a posição não for válida, retorna False. """

        if posicao < 0 or posicao > self.tamanho:
            return False

        if posicao == 0:
            self.inserir_inicio(item)
            return True

        novo_no = No(item)
        atual = self.primeiro
        indice = 0

        while indice < posicao - 1:
            atual = atual.proximo
            indice += 1

        novo_no.proximo = atual.proximo
        atual.proximo = novo_no
        self.tamanho += 1

        return True

        # Custo: O(n), percorrer a lista até encontrar a posição anterior 

    def remover_inicio(self):
        """ Remove o primeiro item da lista e o retorna """

        if self.primeiro is None:
            return None

        removido = self.primeiro
        self.primeiro = removido.proximo
        self.tamanho -= 1

        return removido.item

        # Custo: O(1), remove o primeiro nó, sem percorrer a lista.


    def remover(self, posicao):
        """ Remove um item de uma posição da lista.
        Ao final, retorna True.
        Caso a posição não exista, retorna False. """

        if posicao < 0 or posicao >= self.tamanho:
            return False

        if posicao == 0:
            self.remover_inicio()
            return True

        atual = self.primeiro
        indice = 0

        while indice < posicao - 1:
            atual = atual.proximo
            indice += 1

        removido = atual.proximo
        atual.proximo = removido.proximo
        self.tamanho -= 1

        return True

        # Custo: O(n), percorre a lista até encontrar o nó anterior

    def remover_item(self, item):
        """ Remove a primeira ocorrência de um item existente
        na lista e retorna True.
        Caso não seja encontrado, retorna False. """

        if self.primeiro is None:
            return False

        if self.primeiro.item == item:
            self.remover_inicio()
            return True

        atual = self.primeiro

        while atual.proximo:
            if atual.proximo.item == item:
                atual.proximo = atual.proximo.proximo
                self.tamanho -= 1
                return True

            atual = atual.proximo

        return False

        # Custo: O(n), percorre os nós até encontrar a primeira ocorrência do item ou chegar ao final da lista.
