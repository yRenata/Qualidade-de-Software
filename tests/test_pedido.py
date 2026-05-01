import pytest
from src.pedido import calcular_total_pedido


def test_deve_calcular_total_quando_valor_minimo_atingido():
    itens = [{"preco": 10}, {"preco": 20}]
    valor_minimo = 15

    resultado = calcular_total_pedido(itens, valor_minimo)

    assert resultado == 30

def test_deve_gerar_erro_quando_valor_minimo_nao_atingido():
    itens = [{"preco": 5}, {"preco": 5}]
    valor_minimo = 20

    with pytest.raises(ValueError):
        calcular_total_pedido(itens, valor_minimo)

def test_deve_aceitar_valor_igual_ao_minimo():
    itens = [{"preco": 10}, {"preco": 5}]
    valor_minimo = 15

    resultado = calcular_total_pedido(itens, valor_minimo)

    assert resultado == 15

