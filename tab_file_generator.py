import fileinput
from src.mic import line_splitter, duplication_modifier

def row_generator(file_name, header=None, header_idx=0, delimiter="\t"):
	"""
	reading text file and generate dict files
	"""

	# empty entry with new line character
	EMPTY_ROW = "\n"

	# getting file header if header is not provided
	if not header:
		file_content = fileinput.input(file_name)
		for idx in range(header_idx):
			next(file_content)
		header = line_splitter(next(file_content), delimiter)

	# check duplication in the header
	if len(set(header)) != len(header):
		header = duplication_modifier(header)

	# output dictionay object containing the header info
	for row in file_content:
		if row != EMPTY_ROW:
			row_content = line_splitter(row, delimiter)
			if len(header) < len(row_content):
				raise ValueError(f"Unexpected row value found on line {file_content.lineno()}")
			yield dict(zip(header, row_content))
