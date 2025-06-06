import json
from datetime import datetime

def log_action(agent_name, action, details=None):
    log = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "agent": agent_name,
        "action": action,
        "details": details or {}
    }
    print(json.dumps(log, indent=2))