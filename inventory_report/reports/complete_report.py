from collections import Counter

from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __init__(self, list_products):
        self.list_products = list_products

    def simple_report(self, list_products):
        simple_report = super().generate(list_products)
        return simple_report

    def companies_list(self, list_products):
        all_registry_company = list()
        companies = ""

        for product in list_products:
            all_registry_company.append(product["nome_da_empresa"])

        count_companies = Counter(all_registry_company).most_common()

        for product, quantity in count_companies:
            companies += f"- {product}: {quantity}\n"

        return companies

    @classmethod
    def generate(self, list_products):
        title = "Produtos estocados por empresa:"
        simple_report = self.simple_report(self, list_products)
        companies_list = self.companies_list(self, list_products)
        print("\nCOMPANIES LIST >>>>>> ", companies_list)
        return f"{simple_report}\n{title}\n{companies_list}"
