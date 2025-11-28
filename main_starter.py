# Week9: Simple Temperature Monitor — Model Answer
# 実行方法: python main_starter.py

from data_day1 import temperatures

def mean(nums):
    """リストの平均値を返す。空リストのときは None。"""
    if len(nums) == 0:
        return None
    total = 0.0
    for n in nums:
        total += n
    return total / len(nums)

def hottest_hour(nums):
    """
    最大値とそのインデックス(時間=0..23)をタプルで返す。
    空リストなら (None, None)
    """
    if len(nums) == 0:
        return (None, None)
    max_val = nums[0]
    max_idx = 0
    for idx in range(1, len(nums)):
        if nums[idx] > max_val:
            max_val = nums[idx]
            max_idx = idx
    return (max_val, max_idx)

def count_alerts(nums, threshold):
    """threshold（しきい値）以上の時間数を数える。"""
    count = 0
    for t in nums:
        if t >= threshold:
            count += 1
    return count

def make_report_line(day_label, nums, threshold):
    """
    1行のレポート文字列を作成する。
    例:
      "Day1 | avg=23.5°C | max=30.2°C at h=14 | alerts(>=28)=5"
    """
    avg = mean(nums)
    mx, h = hottest_hour(nums)
    alerts = count_alerts(nums, threshold)
    return (
        f"{day_label} | avg={avg:.1f}°C | "
        f"max={mx:.1f}°C at h={h} | alerts(>={threshold})={alerts}"
    )

if __name__ == "__main__":
    THRESHOLD = 28.0  # しきい値（自由に変更可）

    print("== Week7/Week8 Temperature Monitor ==")
    print("データ件数:", len(temperatures))
    print("平均:", mean(temperatures))
    print("最大(値, 時間):", hottest_hour(temperatures))
    print("しきい値以上の時間数:", count_alerts(temperatures, THRESHOLD))
    print(make_report_line("Day1", temperatures, THRESHOLD))
