import os


def parse_rst_file(file, level):
	title = ""
	if level >= 5:
		level = 5
	head = "#" * level + " "
	with open(file, "rt", encoding="utf-8") as f:
		file_lines = f.readlines()
		for line_num in range(len(file_lines) - 1):
			if file_lines[line_num + 1].startswith("="):
				title = head + file_lines[line_num]

	return title


def parse_md_file(file, level):
	content = ""
	if level >= 5:
		level = 5
	head = "#" * level
	with open(file, "rt", encoding="utf-8") as f:
		file_lines = f.readlines()
		for line in file_lines:
			if line.startswith("#"):
				line = head + line
			if line.startswith(">>"):
				line = line.replace(">>", ">")
			content += line
	return content

if __name__ == '__main__':

	file_str = ""

	file_path = os.path.join(os.getcwd(), "source")

	level = 1
	for root, _, files in os.walk(file_path):
		dir = os.path.basename(root)
		if files and dir != "config":
			md_file = [item for item in files if item.endswith(".md")]
			rst_file = [item for item in files if item.endswith(".rst")]
			if rst_file:
				for rst in rst_file:
					title = parse_rst_file(file=os.path.join(root, rst), level=level)
					if title:
						file_str += title
			if md_file:
				for md in md_file:
					md_content = parse_md_file(file=os.path.join(root, md), level=level)
					if md_content:
						file_str += md_content
		level += 1

	with open("./readme.md", "wt", encoding="utf-8") as f:
		f.write(file_str)