from lista_ligada import Lista_Ligada


def criar_lista():
    lista = Lista_Ligada()
    lista.adicionar(10)
    lista.adicionar(20)
    lista.adicionar(30)
    return lista


def test_adicionar():
    lista = Lista_Ligada()

    lista.adicionar(10)
    lista.adicionar(20)

    assert lista.tamanho == 2
    assert lista.exibir() == "10 -> 20 -> null"


def test_exibir():
    lista = criar_lista()

    assert lista.exibir() == "10 -> 20 -> 30 -> null"


def test_exibir_lista_vazia():
    lista = Lista_Ligada()

    assert lista.exibir() == "null"


def test_pesquisar_item_existente():
    lista = criar_lista()

    assert lista.pesquisar(20) == True


def test_pesquisar_item_inexistente():
    lista = criar_lista()

    assert lista.pesquisar(50) == False


def test_obter_posicao_valida():
    lista = criar_lista()

    assert lista.obter(0) == 10
    assert lista.obter(1) == 20
    assert lista.obter(2) == 30


def test_obter_posicao_invalida():
    lista = criar_lista()

    assert lista.obter(5) is None


def test_inserir_posicao_valida():
    lista = criar_lista()

    resultado = lista.inserir(1, 15)

    assert resultado is None or resultado is True
    assert lista.exibir() == "10 -> 15 -> 20 -> 30 -> null"


def test_inserir_posicao_invalida():
    lista = criar_lista()

    resultado = lista.inserir(10, 50)

    assert resultado == False


def test_remover_posicao_valida():
    lista = criar_lista()

    resultado = lista.remover(1)

    assert resultado == True
    assert lista.exibir() == "10 -> 30 -> null"


def test_remover_posicao_invalida():
    lista = criar_lista()

    resultado = lista.remover(10)

    assert resultado == False


def test_remover_item_existente():
    lista = criar_lista()

    resultado = lista.remover_item(20)

    assert resultado == True
    assert lista.exibir() == "10 -> 30 -> null"


def test_remover_item_inexistente():
    lista = criar_lista()

    resultado = lista.remover_item(50)

    assert resultado == False
    
