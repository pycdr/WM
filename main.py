from generator import convert
from sound import Audio, getaudio

def main():
	from argparse import ArgumentParser
	from os import system, listdir, makedirs, get_terminal_size as size
	from os.path import exists, join

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
	
	details = convert(path, out, width, height)
	fps = details["fps"]
	
	getaudio(path, join(out, "sound.mp3"))
	audio = Audio(join(out, "sound.mp3"))
	audio.start()
	
	system(f"go run reader.go {fps} {out}")

if __name__ == "__main__":
	main()
