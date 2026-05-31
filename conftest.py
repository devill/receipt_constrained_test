import os

from approvaltests import set_default_reporter
from approvaltests.reporters.diff_reporter import DiffReporter
from approvaltests.reporters.first_working_reporter import FirstWorkingReporter
from approvaltests.reporters.generic_diff_reporter import GenericDiffReporter
from approvaltests.reporters.generic_diff_reporter_config import (
    GenericDiffReporterConfig,
)
from approvaltests.reporters.report_quietly import ReportQuietly

INTELLIJ_REPORTER = GenericDiffReporter(
    GenericDiffReporterConfig(
        name="IntelliJ",
        path="/usr/local/bin/idea",
        extra_args=["diff"],
    )
)


def pytest_configure(config):
    set_default_reporter(_reporter_for_environment())


def _reporter_for_environment():
    if os.environ.get("CI"):
        return ReportQuietly()
    return FirstWorkingReporter(INTELLIJ_REPORTER, DiffReporter())
