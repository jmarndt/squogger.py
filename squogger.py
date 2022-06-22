import sys
import json
import datetime
import math


def log_squat(squat_time, current_log):
    date = str(datetime.date.today())
    try:
        existing_date = current_log[date]
        sessions = existing_date['sessions']
        sessions.append(squat_time)
        updated_total_time = math.fsum(sessions)
        existing_date['total_minutes'] = updated_total_time
    except KeyError:
        new_date_log = { 'total_minutes': squat_time, 'sessions': [ squat_time ]}
        current_log[date] = new_date_log

    update_squat_log(current_log)


def update_squat_log(current_log):
    with open('squat.json', 'w') as squat_json:
        new_json = json.dumps(current_log, indent=2)
        squat_json.write(new_json)


def parse_squat_time(squat_time):
    time_list = squat_time.split(':')
    minutes = int(time_list[0])
    seconds = int(time_list[1])
    return round(minutes + (seconds / 60), 2)


def init_squat_json():
    current_log = None
    try:
        with open('squat.json', 'r') as squat_json:
            contents = squat_json.read()
            current_log = json.loads(contents)
    except FileNotFoundError:
        with open('squat.json', 'w') as squat_json:
            init_json = json.dumps({}, indent=2)
            squat_json.write(init_json)
            current_log = {}
    return(current_log)


if __name__ == '__main__':
    squat_time = parse_squat_time(sys.argv[1])
    current_log = init_squat_json()
    log_squat(squat_time, current_log)
    