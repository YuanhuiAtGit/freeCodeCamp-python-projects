##Time Calculator##

def add_time(start, duration, day_of_week=None):
    """
    >>> add_time("3:00 PM", "3:10")
    6:10 PM

    >>> add_time("11:30 AM", "2:32", "Monday")
    2:02 PM, Monday

    >>> add_time("11:43 AM", "00:20")
    12:03 PM

    >>> add_time("10:10 PM", "3:30")
    1:40 AM (next day)

    >>> add_time("11:43 PM", "24:20", "tueSday")
    12:03 AM, Thursday (2 days later)

    >>> add_time("6:30 PM", "205:12")
    7:42 AM (9 days later)


    Do not import any Python libraries. Assume that the start times 
    are valid times. The minutes in the duration time will be a whole 
    number less than 60, but the hour can be any whole number.
    """
    start = start.split()
    start[0] = start[0].split(":")
    duration = duration.split(":")
    dw = day_of_week.capitalize() if day_of_week else None    

    raw_hour = int(start[0][0]) + int(duration[0])
    raw_minute = int(start[0][1]) + int(duration[1])
    original_marker = start[1]
    
    half_days = (raw_hour + (raw_minute // 60)) // 12
    hour = 12 if (raw_hour + (raw_minute // 60)) % 12 == 0 else (raw_hour + (raw_minute // 60)) % 12
    minute = raw_minute % 60

    markers = ['AM', 'PM']
    marker = markers[1- markers.index(original_marker)] if half_days % 2 != 0 else original_marker
    past_hours = int(duration[0]) + (int(duration[1]) / 60)
    if original_marker == 'PM' and marker == 'AM':
        past_days = int(past_hours / 24) + 1 
    else:
        past_days = int(past_hours / 24)
    week = ['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday','Saturday','Sunday']
    new_dw = week[week.index(dw) + int(past_days) % 7] if dw else None


    new_minute = str(minute) if minute >= 10 else '0'+str(minute)
    time = "".join([str(hour), ":", new_minute," ", marker, ",", " ", new_dw]) if new_dw else "".join([str(hour), ":", new_minute," ", marker])
    
    if past_days == 0:
        print(time)
    elif past_days == 1:
        print(time, "(next day)")
    else:
        print(time, f"({past_days} days later)")
    

        





