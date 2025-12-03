# Service Reliability & API Validation Framework  
---

Overview

This project simulates a real-world **SRE (Site Reliability Engineering)** and **Tester/QA Automation** workflow by continuously validating the reliability of an API using automated health checks, functional tests, alerting, and daily reporting.

It performs:

- API uptime & status verification  
- Latency (response time) measurement  
- Functional validation test cases  
- Negative/error handling checks  
- Structured logging (service logs & alert logs)  
- CSV-based daily reliability reporting  



---

Key Features

1. Automated Health Checks (SRE)
- Validates HTTP status codes  
- Measures response latency  
- Detects network/timeout failures  
- Enforces SRE thresholds (latency, status, errors)

2. Functional Test Suite (QA)
- Positive test cases  
- Negative test cases  
- JSON structure validation  
- Key-value presence checks  
- Response content verification  

3. Alerting System  
Logs warnings/errors to a dedicated **alerts.log** file for:
- slow responses  
- failed status codes  
- missing JSON keys  
- timeouts or network failures  

4. Daily CSV Report  
Saves every run into `reports/daily_results.csv`, including:
- timestamp  
- latency  
- status  
- pass/fail counts  
- error messages  

5. Production-Style Logging  
Two separate log files:
- `service.log` → Normal flow, info logs  
- `alerts.log` → Failures, warnings, threshold violations  


# Sample Log Outputs

# alerts.log
[ALERT] WARNING: Latency over threshold: 1200 ms
[ALERT] ERROR: Status code mismatch: expected 200, got 500

# service.log
[SERVICE] Health check: status=200 latency=150 ms
[SERVICE] Test: JSON keys present -> PASS


# Author
Pratiksha Chaudhari

