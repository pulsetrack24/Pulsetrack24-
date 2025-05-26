import schedule
import time
import subprocess

def run_logger():
    subprocess.run(["python", "product_logger.py"])

schedule.every(6).hours.do(run_logger)

while True:
    schedule.run_pending()
    time.sleep(60)