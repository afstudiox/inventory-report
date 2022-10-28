from inventory_report.inventory.product import Product


def test_relatorio_produto():
    new_product = Product(
        7,
        "Spironolactone",
        "REMEDYREPACK",
        "2021-07-17",
        "2023-11-18",
        "SM28",
        "Manter a temperatura ambiente",
    )

    object_product = new_product.__repr__()

    object_match = """O produto Spironolactone fabricado em 2021-07-17
 por REMEDYREPACK com validade até 2023-11-18 precisa ser armazenado
 Manter a temperatura ambiente."""

    assert object_product == object_match.replace("\n", "")
