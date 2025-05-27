import time
import requests

def run_scheduler():
    while True:
        try:
            requests.get("https://pulsetrack24.onrender.com/run")
        except Exception as e:
            print(f"Scheduler error: {e}")
        time.sleep(3600)  # Run every hour

if __name__ == "__main__":
    run_scheduler()