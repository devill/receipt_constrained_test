import re
from datetime import date
from pathlib import Path
from approvaltests.namer.namer_base import NamerBase

APPROVED_DIR = Path(__file__).parent / "approved"


class FixtureNamer(NamerBase):
    def __init__(self, name):
        super().__init__(extension=".txt")
        self._name = name

    def get_file_name(self):
        return self._name

    def get_directory(self):
        return str(APPROVED_DIR)

    def config_directory(self):
        return str(APPROVED_DIR)


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


def receipt_provider():
    for approved_file in sorted(APPROVED_DIR.glob("*.approved.txt")):
        yield ParsedReceipt(approved_file)
