from typing import Dict, Any, List

def run_test_cases(health_result: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Run simple functional/validation tests on the API response.
    Returns a list of test results with name, passed flag, and details.
    """
    tests = []

    # Test 1: API should respond without network error
    tests.append({
        "name": "No network/timeout error",
        "passed": health_result.get("error") is None,
        "details": health_result.get("error")
    })

    # Test 2: Status code should be 200
    tests.append({
        "name": "Status code is 200",
        "passed": health_result.get("status_code") == 200,
        "details": f"Got {health_result.get('status_code')}"
    })

    # Test 3: Latency under 800 ms
    latency = health_result.get("latency_ms")
    tests.append({
        "name": "Latency under 800 ms",
        "passed": latency is not None and latency <= 800,
        "details": f"Latency {latency} ms"
    })

    # Test 4: JSON response contains expected keys (if JSON)
    data = health_result.get("data") or {}
    expected_keys = ["userId", "id", "title"]  # specific to jsonplaceholder demo API
    missing = [k for k in expected_keys if k not in data]

    tests.append({
        "name": "JSON contains expected keys",
        "passed": len(missing) == 0,
        "details": f"Missing keys: {missing}" if missing else "All keys present"
    })

    return tests
