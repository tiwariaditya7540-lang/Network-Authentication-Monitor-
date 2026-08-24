from collections import defaultdict, deque
from datetime import datetime, timedelta
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NetworkAuthMonitor:
    def __init__(self, threshold=5, time_window_seconds=120):
        self.threshold = threshold
        self.time_window = timedelta(seconds=time_window_seconds)
        self.failed_attempts = defaultdict(deque)
        self.security_alerts = []
        
        self.valid_users = {
            "aditya78_root": "aditya123"
        }

    def authenticate(self, ip, username, password):
        timestamp = datetime.now()
        
        if username in self.valid_users and self.valid_users[username] == password:
            return {"status": "success", "message": f"Authentication successful for user: {username}", "alert_triggered": False}

        logging.warning(f"Failed login attempt for user '{username}' from IP: {ip}")
        q = self.failed_attempts[ip]
        
        while q and timestamp - q[0] > self.time_window:
            q.popleft()
            
        q.append(timestamp)
        
        if len(q) >= self.threshold:
            alert_message = f"CRITICAL: Brute-Force Attack Detected! IP: {ip} crossed {self.threshold} failed attempts."
            if alert_message not in self.security_alerts:
                self.security_alerts.insert(0, alert_message)
            return {"status": "failed", "message": "Invalid credentials!", "alert_triggered": True, "alert": alert_message}
            
        return {"status": "failed", "message": "Invalid credentials. Attempt recorded.", "alert_triggered": False}

    def get_alerts(self):
        return self.security_alerts

    def clear_alerts(self):
        self.failed_attempts.clear()
        self.security_alerts.clear()