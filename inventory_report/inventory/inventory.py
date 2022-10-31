import csv
import json

import xmltodict

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(self, PATH, TYPE_REPORT):
        if PATH.endswith(".csv"):
            PRODUCTS = self.read_csv_file(PATH)
        elif PATH.endswith(".json"):
            PRODUCTS = self.read_json_file(PATH)
        elif PATH.endswith(".xml"):
            PRODUCTS = self.read_xml_file(PATH)
        return self.type_report(PRODUCTS, TYPE_REPORT)

    @classmethod
    def type_report(self, PRODUCTS, TYPE_REPORT):
        if TYPE_REPORT == "completo":
            return CompleteReport.generate(PRODUCTS)
        elif TYPE_REPORT == "simples":
            return SimpleReport.generate(PRODUCTS)

    @classmethod
    def read_json_file(self, PATH):
        with open(PATH, "r") as file:
            return json.load(file)

    @classmethod
    def read_csv_file(self, PATH):
        product_list = []
        with open(PATH, "r") as file:
            csvReader = csv.DictReader(file)
            for rows in csvReader:
                product_list.append(rows)
        return product_list

    @classmethod
    def read_xml_file(self, PATH):
        with open(PATH, "r") as file:
            data = xmltodict.parse(file.read())
            formatted_data = data["dataset"]["record"]
            return [dict(company) for company in formatted_data]
