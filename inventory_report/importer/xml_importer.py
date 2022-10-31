from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class XmlImporter(Importer):
    @staticmethod
    def import_data(PATH):
        if PATH.endswith(".xml"):
            return Inventory.read_xml_file(PATH)
        else:
            raise ValueError("Arquivo inválido")
