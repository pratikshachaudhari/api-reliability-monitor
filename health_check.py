# health_check.py

import time
import requests
from typing import Dict, Any
from config import API_URL, REQUEST_TIMEOUT_SECONDS, EXPECTED_STATUS_CODE, MAX_ALLOWED_LATENCY_MS

def run_health_check() -> Dict[str, Any]:
    """
    Performs a single health check against the API.
    Returns a dict with details: status, latency, ok flag, and raw data if available.
    """
    start_time = time.time()
    result = {
        "ok": False,
        "status_code": None,
        "latency_ms": None,
        "error": None,
        "data": None,
    }

    try:
        response = requests.get(API_URL, timeout=REQUEST_TIMEOUT_SECONDS)
        latency_ms = (time.time() - start_time) * 1000

        result["status_code"] = response.status_code
        result["latency_ms"] = round(latency_ms, 2)

        
        try:
            result["data"] = response.json()
        except ValueError:
            result["data"] = None

        
        status_ok = response.status_code == EXPECTED_STATUS_CODE
        latency_ok = latency_ms <= MAX_ALLOWED_LATENCY_MS

        result["ok"] = status_ok and latency_ok

    except requests.exceptions.RequestException as e:
        result["error"] = str(e)

    return result
