from util import get_input


def is_safe(report: list[int]) -> bool:
	n = len(report)
	asc_report = sorted(report)
	inc = True
	for i in range(n):
		if asc_report[i] != report[i]:
			inc = False
			break
	desc_report = sorted(report, reverse=True)
	dec = True
	for i in range(n):
		if desc_report[i] != report[i]:
			dec = False
			break
	if not inc and not dec:
		return False
	diffs = [abs(report[i - 1] - report[i]) for i in range(1, n)]
	if len(list(filter(lambda diff: diff < 1 or diff > 3, diffs))) > 0:
		return False
	return True


def solve():
	puzzle_input = list(map(lambda line: line.split(), get_input(2, 1).splitlines()))
	reports = list(map(lambda line: list(map(int, line)), puzzle_input))
	safe_count = 0
	for report in reports:
		if is_safe(report):
			safe_count += 1
			continue
		n = len(report)
		print(report)
		for i in range(n):
			modified = report[slice(0, i)] + report[slice(i + 1, n)]
			if is_safe(modified):
				safe_count += 1
				break

	print(safe_count)


if __name__ == "__main__":
	solve()