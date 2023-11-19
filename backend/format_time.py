from datetime import datetime


def formatted_time(str_time):
    time_obj = datetime.strptime(str_time, '%H:%M')
    return time_obj.time()
