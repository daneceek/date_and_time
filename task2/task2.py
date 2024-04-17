import datetime
def second_from_midnight(time):
    pt = datetime.datetime.strptime(time,'%H:%M:%S,%f')
    total_seconds = pt.second + pt.minute*60 + pt.hour*3600
    return total_seconds