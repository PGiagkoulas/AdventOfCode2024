from utils import read_input_file


def _is_genuine_monotonic(nums: list[int]) -> bool:
    return all(n > 0 for n in nums) or all(n < 0 for n in nums)


def _is_all_within_range(nums: list[int]) -> bool:
    return all(abs(n) <= 3 for n in nums)


if __name__ == "__main__":
    print("Day 2:")
    input = read_input_file("d2-input.txt")
    all_reports = [[int(r) for r in report.split(" ")] for report in input]

    diffs = [[report[i] - report[i + 1] for i in range(len(report) - 1)] for report in all_reports]
    safe_reports = [1 if _is_genuine_monotonic(report_diff) and _is_all_within_range(report_diff) else 0 for report_diff in diffs]
    num_safe_reports = sum(safe_reports)
    print(f"[>] Number of total safe reports: {num_safe_reports}")

    # TODO: part 2
