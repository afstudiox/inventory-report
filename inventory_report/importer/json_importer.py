from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class JsonImporter(Importer):
    @staticmethod
    def import_data(PATH):
        if PATH.endswith(".json"):
            return Inventory.read_json_file(PATH)
        else:
            raise ValueError("Arquivo inválido")
