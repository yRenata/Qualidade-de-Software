def calcular_total_pedido(itens, valor_minimo):
    if not itens:
        raise ValueError("Pedido vazio")

    total = sum(item.get("preco", 0) for item in itens)

    minimo_atingido = total >= valor_minimo
    if not minimo_atingido:
        raise ValueError("Valor mínimo do pedido não atingido")

    return total