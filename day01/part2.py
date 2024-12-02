from collections import defaultdict
from util import get_input


def solve():
	puzzle_input = list(map(lambda line: line.split("   "), get_input(1, 2).splitlines()))
	distances = list(map(lambda pair: tuple(map(int, pair)), puzzle_input))
	left_dist = list(sorted(map(lambda pair: pair[0], distances)))
	right_dist = list(sorted(map(lambda pair: pair[1], distances)))
	counts = defaultdict(lambda: 0)
	for val in right_dist:
		counts[val] += 1
	score = 0
	for val in left_dist:
		score += val * counts[val]

	print(score)


if __name__ == "__main__":
	solve()