import datetime

time_str = '20220506T000051'
def TranferTimestamp(time_str):
    time_format = "%Y%m%dT%H%M%S"
    now = datetime.datetime.strptime(time_str, time_format)
    now_utc = now.replace(tzinfo=datetime.timezone.utc)
    now_local = now_utc.astimezone()
    return now_local

print(TranferTimestamp(time_str))

