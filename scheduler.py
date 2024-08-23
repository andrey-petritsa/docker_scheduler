import datetime
import time

def set_schedule_at_every_hour(command, hour):
    while(True):
        now = datetime.datetime.now()
        now_hour = now.hour
        if now_hour == hour:
            command.execute()
            one_hour = 3600
            time.sleep(one_hour)
        time.sleep(1)