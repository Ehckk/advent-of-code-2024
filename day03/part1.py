from util import get_input
import re

def solve():
	puzzle_input = get_input(3, 1)
	# puzzle_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
	matches: list[str] = re.findall(r"mul\(\d+,\d+\)", puzzle_input)
	total = 0
	for match in matches:
		product = 1
		for val in re.findall(r"\d+", match):
			product *= int(val)
		total += product
	print(total)


if __name__ == "__main__":
	solve()