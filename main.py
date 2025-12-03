import time
from logging_setup import setup_loggers
from health_check import run_health_check
from test_cases import run_test_cases
from reporter import record_run
from config import RUN_ITERATIONS, SLEEP_BETWEEN_CHECKS_SECONDS, API_URL

def main():
    service_logger, alert_logger = setup_loggers()

    service_logger.info(f"Starting API reliability monitor for: {API_URL}")
    service_logger.info(f"Planned iterations: {RUN_ITERATIONS}")

    for i in range(1, RUN_ITERATIONS + 1):
        service_logger.info(f"--- Check {i}/{RUN_ITERATIONS} ---")

        # 1) Health check (SRE-style)
        health_result = run_health_check()
        service_logger.info(
            f"Health check result: status={health_result.get('status_code')}, "
            f"latency={health_result.get('latency_ms')} ms, error={health_result.get('error')}"
        )

        # 2) Tester-style functional checks
        tests = run_test_cases(health_result)
        for t in tests:
            msg = f"Test: {t['name']} -> {'PASS' if t['passed'] else 'FAIL'} ({t['details']})"
            if t["passed"]:
                service_logger.info(msg)
            else:
                alert_logger.warning(msg)

        # 3) Record run in CSV report
        record_run(health_result, tests)

        # 4) Alerts for failed overall health
        if not health_result.get("ok"):
            alert_logger.error(
                f"Health check FAILED: status={health_result.get('status_code')}, "
                f"latency={health_result.get('latency_ms')} ms, error={health_result.get('error')}"
            )

        if i < RUN_ITERATIONS:
            time.sleep(SLEEP_BETWEEN_CHECKS_SECONDS)

    service_logger.info("Monitoring completed.")

if __name__ == "__main__":
    main()
