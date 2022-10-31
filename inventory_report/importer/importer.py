from abc import ABC, abstractmethod


class Importer(ABC):  # Interface
    @abstractmethod
    def import_data(path):
        pass
