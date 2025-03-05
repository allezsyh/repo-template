"""
日期： 2025.2.12
作者： Harvey Shi
功能：处理时间戳与 datetime 对象之间的转换
1. datetime_to_unix_milliseconds：将 datetime 对象转换为 Unix 时间戳（毫秒）。
2. convert_to_datetime：将 Unix 时间戳（毫秒）转换为 datetime 对象，并转换为北京时间。
"""

from datetime import timezone, datetime, timedelta

def datetime_to_unix_milliseconds(dt):
    """
    datetime对象格式的时间转换为时间戳格式
    """
    # 转换为UTC时间
    dt_utc = dt.astimezone(timezone.utc)
    # Unix 时间戳
    unix_timestamp = int(dt_utc.timestamp() * 1000)
    return unix_timestamp

def convert_to_datetime(unix_timestamp_ms):
    """
    将 Unix 时间戳（毫秒）转换为 datetime 对象（北京时间）
    """
    # 将 Unix 时间戳（毫秒）转换为 Unix 时间戳（秒）
    unix_timestamp_seconds = unix_timestamp_ms / 1000

    # 将 Unix 时间戳（秒）转换为 datetime 对象
    date_time_obj = datetime.utcfromtimestamp(unix_timestamp_seconds)

    # 将 UTC 时间转换为中国时间（北京时间）
    china_timezone = timedelta(hours=8)  # 中国的时区比 UTC 时间快 8 小时
    china_datetime = date_time_obj + china_timezone

    return china_datetime