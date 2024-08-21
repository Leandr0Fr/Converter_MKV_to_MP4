from datetime import datetime


def get_hours_minutes_seconds(time: float):
    hours, rem = divmod(time, 3600)
    minutes, seconds = divmod(rem, 60)
    return hours, minutes, seconds


def get_local_time() -> str:
    local_time = datetime.now()
    return local_time.strftime("%H:%M:%S")
