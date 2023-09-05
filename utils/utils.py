from uuid import uuid4
from datetime import datetime, timedelta

def get_uuid():
    """_summary_

    Returns:
        str: returns uuid4 string
    """
    return str(uuid4())

def last_day_of_month(input_dt):
    next_month = input_dt.replace(day=28) + timedelta(days=4)
    res = next_month - timedelta(days=next_month.day)
    return res

def write_html_receipt(path, content):
    with open(path, 'w', -1, "utf-8") as file:
        file.write(content)
        file.close()
