import re
from datetime import date
from approvaltests.namer.namer_base import NamerBase


class FixtureNamer(NamerBase):
    def __init__(self, name, approved_dir):
        super().__init__(extension=".txt")
        self._name = name
        self._approved_dir = approved_dir

    def get_file_name(self):
        return self._name

    def get_directory(self):
        return str(self._approved_dir)

    def config_directory(self):
        return str(self._approved_dir)


class ParsedReceipt:
    ITEM = re.compile(r"(\w+) x (\d+) @ ([\d.]+) = [\d.]+")
    DATE = re.compile(r"Date: (\d{4}-\d{2}-\d{2})")

    def __init__(self, approved_file):
        self._name = approved_file.name.removesuffix(".approved.txt")
        self._text = self._load_receipt_text(approved_file)
        self._items = self.ITEM.findall(self._text)
        self._date = date.fromisoformat(self.DATE.search(self._text).group(1))

    @staticmethod
    def _load_receipt_text(approved_file):
        return approved_file.read_text().rstrip("\n")

    def name(self):
        return self._name

    def text(self):
        return self._text

    def today(self):
        return self._date

    def prices(self):
        return [(name, float(price)) for name, _, price in self._items]

    def quantities(self):
        return [(name, int(qty)) for name, qty, _ in self._items]


def receipt_provider(approved_dir):
    for approved_file in sorted(approved_dir.glob("*.approved.txt")):
        yield ParsedReceipt(approved_file)
