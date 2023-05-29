import sys
from versions import (
    python_version,
    requests_version,
    pytest_version
)

def test_python_version():
    assert sys.version_info.major == 3
    assert sys.version_info.minor >= 9


def test_requests_version():
    assert requests_version() == "2.25.1"


def test_pytest_version():
    assert pytest_version() == "7.3.1"
