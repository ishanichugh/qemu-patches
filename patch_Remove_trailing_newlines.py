import re,mmap
import os

def format_file(path):
	f = open(path,'r')
	lines = f.readlines()
	flag = False
	array = []
	string_pattern = re.compile(r'".+"')
	newline_pattern = re.compile(r'\\n\s*"')
	end_pattern = re.compile(r"\)\s*;")
	for index,line in enumerate(lines):
		if 'error_report' in line:
			flag = True
			array.append(index+1)
		if re.search(end_pattern, line) and flag:
			flag = False
			array.append(index+1)
			for number in range(array[1]-1,array[0]-2,-1):

				a = re.search(string_pattern, lines[number])
				if a:
					b= re.search(newline_pattern, lines[number])
					if b:
						start_pos = b.start()
						lines[number] = lines[number][: start_pos] + lines[number][start_pos+2 :]
						print path
					break
			array =[]
	f= open(path, 'w')
	f.writelines(lines)


for (dir, _, files) in os.walk("/tmp/qemu"):
	for f in files:
		path = os.path.join(dir, f)
		if os.path.exists(path):
			format_file(path)
