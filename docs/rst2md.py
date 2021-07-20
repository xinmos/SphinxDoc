import os
import markdown

html = '''
<html lang="zh-cn">
<head>
<meta content="text/html; charset=utf-8" http-equiv="content-type" />
<link href="github.css" rel="stylesheet">
</head>
<body>
'''
footer = '''
</body>
</html>
'''

EXTENSIONS = [
	'markdown.extensions.tables',
	"markdown.extensions.fenced_code",
	"markdown.extensions.sane_lists",
	"markdown.extensions.smarty",
	"markdown.extensions.codehilite",
	"markdown.extensions.footnotes",
	"markdown.extensions.meta",
	"markdown.extensions.toc"
]

NOT_SAVE_DIR = []

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
		if files and dir not in NOT_SAVE_DIR:
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

	# with open("./readme.md", "wt", encoding="utf-8") as f:
	# 	f.write(file_str)

	html_str = html + markdown.markdown(file_str, extensions=EXTENSIONS) + footer
	with open("./readme.html", "wt", encoding="utf-8") as f:
		f.write(html_str)