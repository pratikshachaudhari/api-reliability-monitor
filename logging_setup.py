import logging
import os
from config import SERVICE_LOG_PATH, ALERT_LOG_PATH, REPORTS_DIR

def ensure_directories():
    os.makedirs(REPORTS_DIR, exist_ok=True)

def setup_loggers():
    ensure_directories()

    # Service log 
    service_logger = logging.getLogger("service")
    service_logger.setLevel(logging.INFO)

    service_handler = logging.FileHandler(SERVICE_LOG_PATH)
    service_formatter = logging.Formatter("%(asctime)s [SERVICE] %(levelname)s: %(message)s")
    service_handler.setFormatter(service_formatter)
    service_logger.addHandler(service_handler)

    # Alert log 
    alert_logger = logging.getLogger("alerts")
    alert_logger.setLevel(logging.WARNING)

    alert_handler = logging.FileHandler(ALERT_LOG_PATH)
    alert_formatter = logging.Formatter("%(asctime)s [ALERT] %(levelname)s: %(message)s")
    alert_handler.setFormatter(alert_formatter)
    alert_logger.addHandler(alert_handler)

    # Quick debugging
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter("%(asctime)s [CONSOLE] %(levelname)s: %(message)s")
    console_handler.setFormatter(console_formatter)
    service_logger.addHandler(console_handler)
    alert_logger.addHandler(console_handler)

    return service_logger, alert_logger
