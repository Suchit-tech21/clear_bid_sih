# Audit logging
from datetime import datetime

def log_action(actor, action):
    timestamp = datetime.now().isoformat(timespec="seconds")
    print(f"{timestamp} | {actor} | {action}")
