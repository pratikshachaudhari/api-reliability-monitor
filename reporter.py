import os
import csv
from datetime import datetime
from typing import Dict, Any, List
from config import RESULTS_CSV_PATH, REPORTS_DIR

CSV_HEADERS = [
    "timestamp",
    "status_code",
    "latency_ms",
    "ok",
    "error",
    "tests_passed",
    "tests_failed"
]

def ensure_reports_file():
    os.makedirs(REPORTS_DIR, exist_ok=True)
    if not os.path.exists(RESULTS_CSV_PATH):
        with open(RESULTS_CSV_PATH, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADERS)

def record_run(health_result: Dict[str, Any], test_results: List[Dict[str, Any]]):
    ensure_reports_file()

    tests_passed = sum(1 for t in test_results if t["passed"])
    tests_failed = sum(1 for t in test_results if not t["passed"])

    row = [
        datetime.utcnow().isoformat(),
        health_result.get("status_code"),
        health_result.get("latency_ms"),
        health_result.get("ok"),
        health_result.get("error"),
        tests_passed,
        tests_failed,
    ]

    with open(RESULTS_CSV_PATH, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)
