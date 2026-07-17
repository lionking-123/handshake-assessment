import json
from pathlib import Path

import pytest

REPORT = Path("/app/report.json")

# Ground truth derived by hand from the fixed 6-line /app/access.log shipped in
# the environment image:
#   total_requests = 6 request lines
#   unique_ips     = {192.168.0.1, 192.168.0.2, 10.0.0.5} -> 3 distinct clients
#   paths          = /index.html x3, /about.html x2, /api/login x1 -> top /index.html
EXPECTED = {"total_requests": 6, "unique_ips": 3, "top_path": "/index.html"}


@pytest.fixture(scope="module")
def report():
    """Load the agent's report, failing clearly if it is missing/empty/invalid."""
    assert REPORT.exists(), "no /app/report.json found"
    assert REPORT.stat().st_size > 0, "/app/report.json is empty"
    with REPORT.open() as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            pytest.fail(f"/app/report.json is not valid JSON: {e}")
    assert isinstance(data, dict), "report must be a JSON object"
    return data


def test_total_requests(report):
    """total_requests matches the number of request lines in the log."""
    assert report.get("total_requests") == EXPECTED["total_requests"], (
        f"total_requests={report.get('total_requests')!r}, "
        f"expected {EXPECTED['total_requests']}"
    )


def test_unique_ips(report):
    """unique_ips matches the number of distinct client IPs in the log."""
    assert report.get("unique_ips") == EXPECTED["unique_ips"], (
        f"unique_ips={report.get('unique_ips')!r}, expected {EXPECTED['unique_ips']}"
    )


def test_top_path(report):
    """top_path matches the most frequently requested path in the log."""
    assert report.get("top_path") == EXPECTED["top_path"], (
        f"top_path={report.get('top_path')!r}, expected {EXPECTED['top_path']!r}"
    )
