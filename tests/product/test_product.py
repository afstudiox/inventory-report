from inventory_report.inventory.product import Product


def test_cria_produto():
    new_product = Product(
        7,
        "Spironolactone",
        "REMEDYREPACK",
        "2021-07-17",
        "2023-11-18",
        "SM28",
        "Manter a temperatura ambiente",
    )

    assert new_product.id == 7
    assert new_product.nome_do_produto == "Spironolactone"
    assert new_product.nome_da_empresa == "REMEDYREPACK"
    assert new_product.data_de_fabricacao == "2021-07-17"
    assert new_product.data_de_validade == "2023-11-18"
    assert new_product.numero_de_serie == "SM28"
    instrucao = "Manter a temperatura ambiente"
    assert new_product.instrucoes_de_armazenamento == instrucao
