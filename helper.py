"""Helper functions."""

from datetime import datetime


def create_timestamp():
    now = datetime.now()
    timestamp = now.strftime("%Y/%m/%d %H:%M:%S")
    return timestamp
    
def is_float(element):
    try:
        float(element)
        return True
    except ValueError:
        return False
