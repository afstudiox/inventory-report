from collections import Counter
from datetime import datetime


class SimpleReport:
    def __init__(self, list_products):
        self.list_products = list_products

    # data de fabricação mais antiga
    def oldest_date(self, list_products):
        oldest_date = min(
            [product["data_de_fabricacao"] for product in list_products]
        )
        return oldest_date

    # validade mais próxima sem estar vencida
    def closest_date(self, list_products):
        closest_date = min(
            [
                product["data_de_validade"]
                for product in list_products
                if datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
                > datetime.now()
            ]
        )
        return closest_date

    # empresa com maio número de produtos
    def company_bigger_stock(self, list_products):
        company_bigger_stock = Counter(
            product["nome_da_empresa"] for product in list_products
        )

        return company_bigger_stock.most_common(1)[0][0]

    @classmethod
    def generate(self, list_products):
        oldest = self.oldest_date(self, list_products)
        closest = self.closest_date(self, list_products)
        company = self.company_bigger_stock(self, list_products)

        return (
            f"Data de fabricação mais antiga: {oldest}\n"
            f"Data de validade mais próxima: {closest}\n"
            f"Empresa com mais produtos: {company}"
        )
