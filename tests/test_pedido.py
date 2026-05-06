import pytest
from src.pedido import calcular_total_pedido

@pytest.mark.parametrize("itens, valor_minimo, resultado_esperado", [
    ([{"preco": 10}, {"preco": 20}], 15, 30),   # acima do mínimo
    ([{"preco": 10}, {"preco": 5}], 15, 15),    # igual ao mínimo
    ([{"preco": 0}, {"preco": 0}], 0, 0),       # valores zero
    ([{"preco": 1000}, {"preco": 2000}], 100, 3000),  # valores altos
])
def test_calcular_total_pedido_valido(itens, valor_minimo, resultado_esperado):
    resultado = calcular_total_pedido(itens, valor_minimo)
    assert resultado == resultado_esperado


@pytest.mark.parametrize("itens, valor_minimo", [
    ([{"preco": 5}, {"preco": 5}], 20),   # abaixo do mínimo
    ([{"preco": 0}], 10),                 # zero abaixo do mínimo
])
def test_calcular_total_pedido_erro(itens, valor_minimo):
    with pytest.raises(ValueError):
        calcular_total_pedido(itens, valor_minimo)