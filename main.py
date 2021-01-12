from generator import convert

def main():
	from argparse import ArgumentParser
	from os import listdir, makedirs, get_terminal_size as size
	from os.path import exists, join
	from time import sleep

	parser = ArgumentParser()
	parser.add_argument("path")
	parser.add_argument("-o", "--out", required = False)
	parser.add_argument("--width", type = int, required = False)
	parser.add_argument("--height", type = int, required = False)
	args = parser.parse_args()
	
	path = args.path
	out = args.out or "output"
	if not exists(out):
		makedirs(out)
	width = args.width or size().columns
	height = args.height or size().lines
	
	convert(path, out, width, height)
	frames = {}
	for x in listdir(out):
		frames[int(x[:-4])] = open(join(out, x), 'r').read()
	for x in sorted(frames.keys()):
		print("\033[2J"+frames[x], end="")
		sleep(.9)

if __name__ == "__main__":
	main()
