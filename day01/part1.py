from util import get_input


def solve():
	puzzle_input = list(map(lambda line: line.split("   "), get_input(1, 1).splitlines()))
	distances = list(map(lambda pair: tuple(map(int, pair)), puzzle_input))
	left_dist = list(sorted(map(lambda pair: pair[0], distances)))
	right_dist = list(sorted(map(lambda pair: pair[1], distances)))
	total = 0
	for i in range(max(len(left_dist), len(right_dist))):
		total += abs(left_dist[i] - right_dist[i])
	print(total)


if __name__ == "__main__":
	solve()