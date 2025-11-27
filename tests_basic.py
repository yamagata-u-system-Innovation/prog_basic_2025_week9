# tests_basic.py
# Week7/8「温度モニタ」実習用 自動テスト
# 実行方法: python tests_basic.py
#
# main_starter.py に以下の関数が定義されている前提:
#   - mean(nums)
#   - hottest_hour(nums)
#   - count_alerts(nums, threshold)
#   - make_report_line(day_label, nums, threshold)

from main_starter import mean, hottest_hour, count_alerts, make_report_line
from data_day1 import temperatures


def approx(a: float, b: float, eps: float = 1e-6) -> bool:
    """浮動小数点同士のほぼ一致判定"""
    return abs(a - b) < eps


def test_mean():
    print("▶ mean(nums) のテスト中...")
    # 基本チェック
    assert mean([1, 2, 3, 4]) == 2.5, "mean([1,2,3,4]) は 2.5 になるべきです。"
    # 空リスト
    assert mean([]) is None, "空リストのときは None を返す仕様にしてください。"
    # 小数の平均（近似チェック）
    assert approx(mean([18.5, 19.5]), 19.0), "平均値の計算が正しくありません。"
    print("  ✓ mean() OK")


def test_hottest_hour():
    print("▶ hottest_hour(nums) のテスト中...")
    mx, h = hottest_hour([10, 20, 15])
    assert mx == 20, "最大値が正しくありません。"
    assert h == 1, "最大値のインデックス（位置）が正しくありません。"

    # data_day1 の temperatures でも整合性チェック
    mx2, h2 = hottest_hour(temperatures)
    expected_max = max(temperatures)
    expected_idx = temperatures.index(expected_max)
    assert approx(mx2, expected_max), "temperatures に対する最大値が正しくありません。"
    assert h2 == expected_idx, "temperatures に対する最大値の位置が正しくありません。"

    print("  ✓ hottest_hour() OK")


def test_count_alerts():
    print("▶ count_alerts(nums, threshold) のテスト中...")
    # 境界をまたぐ値
    assert count_alerts([27.9, 28.0, 28.1], 28.0) == 2, \
        "しきい値以上の個数が正しくカウントされていません。"
    # すべて下回る
    assert count_alerts([10, 20, 27.9], 28.0) == 0, \
        "しきい値未満のみの場合は 0 になるべきです。"
    # すべて上回る
    assert count_alerts([28.0, 29.0, 30.0], 28.0) == 3, \
        "すべてしきい値以上のときのカウントが正しくありません。"
    print("  ✓ count_alerts() OK")


def test_make_report_line():
    print("▶ make_report_line(day_label, nums, threshold) のテスト中...")
    day_label = "Day1"
    threshold = 28.0
    line = make_report_line(day_label, temperatures, threshold)

    # 文字列の基本構造をゆるめにチェック
    assert isinstance(line, str), "make_report_line は文字列を返す必要があります。"
    assert day_label in line, "日付ラベルがレポート文字列に含まれていません。"
    assert "avg=" in line, "平均値(avg=...) の表示が含まれていません。"
    assert "max=" in line, "最大値(max=...) の表示が含まれていません。"
    assert "alerts(>=" in line, "アラート数(alerts(>=...)=...) の表示が含まれていません。"

    # しきい値の数値が文字列に含まれているか（28.0 のような形）
    assert str(threshold) in line, "しきい値の値がレポート文字列に含まれていません。"

    print("  ✓ make_report_line() OK")


if __name__ == "__main__":
    print("=== Week7/8 温度モニタ 自動テスト開始 ===")
    test_mean()
    test_hottest_hour()
    test_count_alerts()
    test_make_report_line()
    print("=== すべてのテストに合格しました！ ✔ ===")
