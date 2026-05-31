from pathlib import Path

import pytest
from approvaltests import Options, verify

from receipt import format_receipt
from receipt_approval_provider import FixtureNamer, receipt_provider

APPROVED_DIR = Path(__file__).parent / "approved"


@pytest.mark.parametrize(
    "parsed_receipt",
    list(receipt_provider(APPROVED_DIR)),
    ids=lambda parsed: parsed.name(),
)
def test_receipt_matches_approved(parsed_receipt):
    actual = format_receipt(
        parsed_receipt.prices(),
        parsed_receipt.quantities(),
        today=parsed_receipt.today(),
    )
    verify(
        actual,
        options=Options().with_namer(FixtureNamer(parsed_receipt.name(), APPROVED_DIR)),
    )
