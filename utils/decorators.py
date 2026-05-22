from datetime import datetime
import os

LOG_FILE = "logs/actions.log"


def log_action(function):
    def wrapper(*args, **kwargs):
        os.makedirs("logs", exist_ok=True)

        result = function(*args, **kwargs)

        with open(LOG_FILE, "a", encoding="utf-8") as file:
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{time_now}] Function used: {function.__name__}\n")

        return result

    return wrapper
