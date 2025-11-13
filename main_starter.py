# Week7: Simple Temperature Monitor (fill-in-the-blanks)
from data_day1 import temperatures

def mean(nums):
    if len(nums) == 0:
        return None
    total = 0.0
    for n in ___:
        total ___ n
    return total / ___

def hottest_hour(nums):
    if len(nums) == 0:
        return (None, None)
    max_val = nums[0]
    max_idx = 0
    for idx in range(1, len(nums)):
        if nums[idx] ___ max_val:
            max_val = ___
            max_idx = ___
    return (max_val, max_idx)

def count_alerts(nums, threshold):
    count = 0
    for t in nums:
        if t ___ threshold:
            count ___ 1
    return count

def make_report_line(day_label, nums, threshold):
    avg = mean(nums)
    mx, h = hottest_hour(nums)
    alerts = count_alerts(nums, threshold)
    return f"___ | avg=___°C | max=___°C at h=___ | alerts(>={___})=___"

if __name__ == "__main__":
    print("Run the exercise.")
