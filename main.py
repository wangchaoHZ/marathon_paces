def calculate_pace(marathon_time):
    # 提取小时和分钟
    hours = marathon_time // 100
    minutes = marathon_time % 100

    # 将总时间转换为分钟
    total_minutes = hours * 60 + minutes

    # 计算全程马拉松配速（42.195公里）
    full_marathon_km = 42.195
    full_marathon_pace = total_minutes / full_marathon_km

    # 计算半程马拉松配速（21.0975公里）
    half_marathon_km = 21.0975
    half_marathon_pace = total_minutes / half_marathon_km

    # 将配速格式化为分钟和秒
    def format_pace(pace):
        pace_minutes = int(pace)
        pace_seconds = int((pace - pace_minutes) * 60)
        return f"{pace_minutes}分{pace_seconds}秒每公里"

    return {
        "full_marathon_pace": format_pace(full_marathon_pace),
        "half_marathon_pace": format_pace(half_marathon_pace)
    }

marathon_time = 400
paces = calculate_pace(marathon_time)
print("全程马拉松配速:", paces["full_marathon_pace"])
marathon_time = 140
paces = calculate_pace(marathon_time)
print("半程马拉松配速:", paces["half_marathon_pace"])
