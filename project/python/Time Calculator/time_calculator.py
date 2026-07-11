def add_time(start, duration, day_of_week=None):
    """
    Calculate a new time by adding a duration to a start time.

    Args:
        start (str): Starting time in 12-hour format, e.g. "3:00 PM"
        duration (str): Duration to add, e.g. "2:15"
        day_of_week (str, optional): Starting weekday, e.g. "Monday"

    Returns:
        dict: A dictionary with:
            - time: final time string
            - day: final weekday or None
            - days_later: number of days passed
            - result: formatted readable result
    """

    # -----------------------------
    # type validation
    # -----------------------------
    if not isinstance(start, str):
        raise TypeError("start must be a string")

    if not isinstance(duration, str):
        raise TypeError("duration must be a string")

    if day_of_week is not None and not isinstance(day_of_week, str):
        raise TypeError("day_of_week must be a string or None")

    days_of_week = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]

    # -----------------------------
    # parse and validate start time
    # expected format: H:MM AM/PM
    # -----------------------------
    try:
        time_part, period = start.split()
        start_hour_str, start_min_str = time_part.split(":")
        start_hour = int(start_hour_str)
        start_min = int(start_min_str)
    except ValueError:
        raise ValueError("start must be in the format 'H:MM AM/PM'")

    if period not in ("AM", "PM"):
        raise ValueError("start period must be AM or PM")

    if not (1 <= start_hour <= 12):
        raise ValueError("start hour must be between 1 and 12")

    if not (0 <= start_min <= 59):
        raise ValueError("start minute must be between 0 and 59")

    # -----------------------------
    # parse and validate duration
    # expected format: H:MM
    # -----------------------------
    try:
        dur_hour_str, dur_min_str = duration.split(":")
        dur_hour = int(dur_hour_str)
        dur_min = int(dur_min_str)
    except ValueError:
        raise ValueError("duration must be in the format 'H:MM'")

    if dur_hour < 0:
        raise ValueError("duration hour must be non-negative")

    if not (0 <= dur_min <= 59):
        raise ValueError("duration minute must be between 0 and 59")

    # -----------------------------
    # validate day_of_week if given
    # -----------------------------
    final_day = None
    if day_of_week is not None:
        normalized_day = day_of_week.capitalize()
        if normalized_day not in days_of_week:
            raise ValueError("day_of_week must be a valid weekday name")
    else:
        normalized_day = None

    # -----------------------------
    # convert start time to 24-hour
    # -----------------------------
    if period == "AM":
        start_hour_24 = 0 if start_hour == 12 else start_hour
    else:
        start_hour_24 = 12 if start_hour == 12 else start_hour + 12

    # -----------------------------
    # compute total minutes
    # -----------------------------
    start_total_minutes = start_hour_24 * 60 + start_min
    duration_total_minutes = dur_hour * 60 + dur_min
    final_total_minutes = start_total_minutes + duration_total_minutes

    days_later = final_total_minutes // (24 * 60)
    remaining_minutes = final_total_minutes % (24 * 60)

    final_hour_24 = remaining_minutes // 60
    final_min = remaining_minutes % 60

    # -----------------------------
    # convert back to 12-hour format
    # -----------------------------
    final_period = "AM" if final_hour_24 < 12 else "PM"

    final_hour = final_hour_24 % 12
    if final_hour == 0:
        final_hour = 12

    final_time = f"{final_hour}:{final_min:02d} {final_period}"

    # -----------------------------
    # calculate final weekday
    # -----------------------------
    if normalized_day is not None:
        day_index = days_of_week.index(normalized_day)
        final_day_index = (day_index + days_later) % 7
        final_day = days_of_week[final_day_index]

    # -----------------------------
    # build result text
    # -----------------------------
    result_text = final_time

    if final_day is not None:
        result_text += f", {final_day}"

    if days_later == 1:
        result_text += " (next day)"
    elif days_later > 1:
        result_text += f" ({days_later} days later)"

    return {
        "time": final_time,
        "day": final_day,
        "days_later": days_later,
        "result": result_text,
    }
