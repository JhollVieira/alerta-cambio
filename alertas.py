def verificar_alerta(preco_atual, valor_maximo=None, valor_minimo=None):
    if valor_maximo is not None and preco_atual >= valor_maximo:
        return f"ALERTA: preço atual {preco_atual} atingiu ou passo o maximo definido ({valor_maximo})"

    if valor_minimo is not None and preco_atual <= valor_minimo:
        return f"ALERTA: preço atual {preco_atual} atingiu ou passou o minimo definido ({valor_minimo})"

    return None