import schedule
import time
import subprocess


def printing():
    print("5 seconds")


schedule.every(5).seconds.do(printing())

# Keep the script running to execute the schedule
while True:
    schedule.run_pending()
    time.sleep(1)