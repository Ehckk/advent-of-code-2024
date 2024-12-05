from util import get_input


DIRECTIONS = [((1, -1), (-1, 1)), ((-1, -1), (1, 1))]
TEST_INPUT = """.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
"""

def solve():
	puzzle_input = get_input(4, 1)
	# puzzle_input = TEST_INPUT
	matrix = puzzle_input.splitlines()
	n = len(matrix)
	m = len(matrix[0])
	total = 0
	for r, row in enumerate(matrix):
		for c in range(len(row)):
			if matrix[r][c] != "A":
				continue
			found = True
			for (d_r1, d_c1), (d_r2, d_c2) in DIRECTIONS:
				r1 = r + d_r1
				c1 = c + d_c1
				if not (0 <= c1 < m) or not (0 <= r1 < n):
					found = False
					break
				r2 = r + d_r2
				c2 = c + d_c2
				if not (0 <= c2 < m) or not (0 <= r2 < n):
					found = False
					break
				letters = {matrix[r1][c1], matrix[r2][c2]}
				if len({"M", "S"} - letters) != 0:
					found = False
					break
			if found:
				total += 1
	print(total)


if __name__ == "__main__":
	solve()