import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Target API to monitor 
API_URL = "https://jsonplaceholder.typicode.com/posts/1"

# Thresholds
MAX_ALLOWED_LATENCY_MS = 800          # alert if response time > 800 ms
EXPECTED_STATUS_CODE = 200
MAX_FAILURE_RATE_PERCENT = 5          # for future extension

# Paths
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
SERVICE_LOG_PATH = os.path.join(REPORTS_DIR, "service.log")
ALERT_LOG_PATH = os.path.join(REPORTS_DIR, "alerts.log")
RESULTS_CSV_PATH = os.path.join(REPORTS_DIR, "daily_results.csv")

# Monitor settings
REQUEST_TIMEOUT_SECONDS = 5           # HTTP timeout
RUN_ITERATIONS = 10                   # how many times to run in one execution
SLEEP_BETWEEN_CHECKS_SECONDS = 5      # pause between checks
