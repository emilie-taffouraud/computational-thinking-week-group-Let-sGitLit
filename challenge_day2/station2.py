import datetime

def solution_station_2(year, month, day):
    
    weekday_translation = {
        "Monday": "月曜日",
        "Tuesday": "火曜日",
        "Wednesday": "水曜日",
        "Thursday": "木曜日",
        "Friday": "金曜日",
        "Saturday": "土曜日",
        "Sunday": "日曜日"
    }
    
    
    date = datetime.datetime(year, month, day)
    weekday_name = date.strftime("%A")
    weekday_name_chinese = weekday_translation[weekday_name]
    return weekday_name_chinese

