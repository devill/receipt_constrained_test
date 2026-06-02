# receipt-constrained-test

A receipt formatter exercised with [ApprovalTests](https://github.com/approvals/ApprovalTests.Python).

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

## Setup

```sh
uv sync
```

## Run the tests

```sh
uv run pytest
```

In CI (`CI` env var set) approval diffs are reported quietly; locally a diff tool is opened on mismatch.
