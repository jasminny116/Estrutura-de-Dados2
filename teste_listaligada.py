
import pytest
from lista_ligada import ListaLigada

def criar_lista():
    lista = ListaLigada()
    lista.adicionar(10)
    lista.adicionar(20)
    lista.adicionar(30)
    return lista

def test_lista_vazia():
    lista = ListaLigada()

    assert lista.primeiro is None
    assert lista.tamanho == 0

def test_inserir_inicio():
    lista = ListaLigada()

    lista.inserir_inicio(10)
    lista.inserir_inicio(20)

    assert str(lista) == "20 -> 10 -> null"
    assert lista.tamanho == 2

def test_adicionar():
    lista = ListaLigada()

    lista.adicionar(10)
    lista.adicionar(20)
    lista.adicionar(30)

    assert str(lista) == "10 -> 20 -> 30 -> null"
    assert lista.tamanho == 3

def test_pesquisar():
    lista = criar_lista()

    assert lista.pesquisar(20) is True
    assert lista.pesquisar(50) is False

def test_pesquisar_lista_vazia():
    lista = ListaLigada()

    assert lista.pesquisar(10) is False

def test_obter():
    lista = criar_lista()

    assert lista.obter(0) == 10
    assert lista.obter(1) == 20
    assert lista.obter(2) == 30

def test_obter_posicao_invalida():
    lista = criar_lista()

    assert lista.obter(-1) is None
    assert lista.obter(3) is None

def test_inserir_posicao():
    lista = criar_lista()

    assert lista.inserir(1, 15) is True

    assert str(lista) == "10 -> 15 -> 20 -> 30 -> null"
    assert lista.tamanho == 4

def test_inserir_inicio_e_fim():
    lista = criar_lista()

    assert lista.inserir(0, 5) is True
    assert lista.inserir(5, 40) is True

    assert str(lista) == "5 -> 10 -> 20 -> 30 -> 40 -> null"
    assert lista.tamanho == 5

def test_inserir_posicao_invalida():
    lista = criar_lista()

    assert lista.inserir(-1, 5) is False
    assert lista.inserir(4, 50) is False

    assert lista.tamanho == 3

def test_remover_inicio():
    lista = criar_lista()

    removido = lista.remover_inicio()

    assert removido == 10
    assert str(lista) == "20 -> 30 -> null"
    assert lista.tamanho == 2

def test_remover_inicio_lista_vazia():
    lista = ListaLigada()

    assert lista.remover_inicio() is None
    assert lista.tamanho == 0

def test_remover_posicao():
    lista = criar_lista()

    assert lista.remover(1) is True

    assert str(lista) == "10 -> 30 -> null"
    assert lista.tamanho == 2

def test_remover_primeira_posicao():
    lista = criar_lista()

    assert lista.remover(0) is True

    assert str(lista) == "20 -> 30 -> null"
    assert lista.tamanho == 2

def test_remover_ultima_posicao():
    lista = criar_lista()

    assert lista.remover(2) is True

    assert str(lista) == "10 -> 20 -> null"
    assert lista.tamanho == 2

def test_remover_posicao_invalida():
    lista = criar_lista()

    assert lista.remover(-1) is False
    assert lista.remover(3) is False

    assert lista.tamanho == 3

def test_remover_item():
    lista = criar_lista()

    assert lista.remover_item(20) is True

    assert str(lista) == "10 -> 30 -> null"
    assert lista.tamanho == 2

def test_remover_item_inicio():
    lista = criar_lista()

    assert lista.remover_item(10) is True

    assert str(lista) == "20 -> 30 -> null"
    assert lista.tamanho == 2

def test_remover_item_inexistente():
    lista = criar_lista()

    assert lista.remover_item(50) is False
    assert lista.tamanho == 3

def test_remover_item_lista_vazia():
    lista = ListaLigada()

    assert lista.remover_item(10) is False
    assert lista.tamanho == 0

def test_remover_item_repetido():
    lista = ListaLigada()

    lista.adicionar(10)
    lista.adicionar(20)
    lista.adicionar(10)

    assert lista.remover_item(10) is True

    assert str(lista) == "20 -> 10 -> null"
    assert lista.tamanho == 2

def test_str_lista_vazia():
    lista = ListaLigada()

    assert str(lista) == "null"
