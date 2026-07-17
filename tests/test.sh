#!/bin/bash
# Verifier: runs the outcome tests and reports the result.
#   - /logs/verifier/ctrf.json : structured CTRF test report
#   - /logs/verifier/reward.txt : 1 if all tests passed, else 0
# pytest and pytest-json-ctrf are baked into the environment image
# (environment/Dockerfile).
set -uo pipefail

REPORT_DIR="/logs/verifier"
mkdir -p "$REPORT_DIR"

pytest /tests/test_outputs.py -rA --ctrf "$REPORT_DIR/ctrf.json"
rc=$?

if [ "$rc" -eq 0 ]; then
  echo 1 > "$REPORT_DIR/reward.txt"
else
  echo 0 > "$REPORT_DIR/reward.txt"
fi

# The verdict is carried by reward.txt; exit 0 so the verifier itself is
# reported as having run cleanly.
exit 0
