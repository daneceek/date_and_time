from datetime import datetime

def second_from_midnight(time_str):
    try:
        time_object = datetime.strptime(time_str, '%H:%M:%S')
        seconds_since_midnight = (time_object - time_object.replace(hour=0, minute=0, second=0)).total_seconds()
        return int(seconds_since_midnight)
    except ValueError as e:
        raise ValueError("Neplatný formát") from e