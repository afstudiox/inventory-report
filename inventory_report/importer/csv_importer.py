from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class CsvImporter(Importer):
    @staticmethod
    def import_data(PATH):
        if PATH.endswith(".csv"):
            return Inventory.read_csv_file(PATH)
        else:
            raise ValueError("Arquivo inválido")
