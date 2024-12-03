from util import get_input
import re


def solve():
	puzzle_input = get_input(3, 1)
	# puzzle_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
	enable = set(match.start() for match in re.finditer(r"do\(\)", puzzle_input))
	disable = set(match.start() for match in re.finditer(r"don't\(\)", puzzle_input))
	sub_strs: list[str] = []
	i = 0
	start = i
	while i < len(puzzle_input):
		if start is not None:
			if i in disable:
				sub_strs.append((start, i))
				start = None
		elif i in enable:
			start = i
		i += 1
	if start is not None:
		sub_strs.append((start, None))
	cleaned_input = "".join(map(lambda x: puzzle_input[x[0]:x[1]], sub_strs))
	matches: list[str] = re.findall(r"mul\(\d+,\d+\)", cleaned_input)
	total = 0
	for match in matches:
		product = 1
		for val in re.findall(r"\d+", match):
			product *= int(val)
		total += product
	print(total)


if __name__ == "__main__":
	solve()
