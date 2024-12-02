from pathlib import Path

INPUT_FILE_NAME = "part{part}"

def get_input(day: int, part: int):
	day_str = f"day{str(day).zfill(2)}"
	filename = INPUT_FILE_NAME.format(part=part)
	path = Path(__file__).parent.joinpath(day_str, filename)
	with open(f"{path}.txt", "r") as f:
		content = f.read()
	return content