from util import get_input


DIRECTIONS = [
	(-1, -1),
	(-1, 0),
	(-1, 1),
	(0, -1),
	(0, 1),
	(1, -1),
	(1, 0),
	(1, 1)
]
TEST_INPUT = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

def solve():
	puzzle_input = get_input(4, 1)
	# puzzle_input = TEST_INPUT
	matrix = puzzle_input.splitlines()
	total = 0
	for r, row in enumerate(matrix):
		for c in range(len(row)):
			if matrix[r][c] != "X":
				continue
			for d_r, d_c in DIRECTIONS:
				found = True
				for i, letter in enumerate(("M", "A", "S")):
					r_offset = r + (d_r * (i + 1))
					if not (0 <= r_offset < len(matrix)):
						found = False
						break
					c_offset = c + (d_c * (i + 1))
					if not (0 <= c_offset < len(matrix[0])):
						found = False
						break
					print(matrix[r_offset][c_offset])
					if matrix[r_offset][c_offset] != letter:
						found = False
						break
				if found:
					total += 1
	print(total)


if __name__ == "__main__":
	solve()