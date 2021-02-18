def main():
	from log import log
	log.info("start main proccess and importing")
	from generator import convert
	from sound import Audio, getaudio
	from argparse import ArgumentParser
	from os import system, listdir, makedirs, remove, get_terminal_size as size
	from os.path import exists, join
	log.info("imported")
	
	log.info("parsing arguments...")
	parser = ArgumentParser()
	parser.add_argument("path")
	parser.add_argument("-o", "--out", required = False)
	parser.add_argument("--width", type = int, required = False)
	parser.add_argument("--height", type = int, required = False)
	parser.add_argument("-c", "--color", action = "store_true")
	parser.add_argument("-s", "--save", action = "store_true")
	args = parser.parse_args()
	log.info("parsed")
	
	path = args.path
	out = args.out or "output"
	if not exists(out):
		makedirs(out)
	else:
		log.warning("output path is existing. text files will be overwritten.")
	log.info("set width and height of output...")
	width = args.width or size().columns
	height = args.height or size().lines - 1
	
	log.info("start convert proccess")
	details = convert(path, out, width, height, log, args.color)
	fps = details["fps"]
	
	log.info("extracting audio...")
	getaudio(path, join(out, "sound.mp3"), log)
	log.info("extracted. make Audio object")
	audio = Audio(join(out, "sound.mp3"))
	log.info("start sound player and texts reader proccess...")
	
	audio.start()
	system(f"go run reader.go {fps} {out} {int(args.color)}")
	
	if not args.save:
		log.info("removing files...")
		remove(join(out,"sound.mp3"))
		for x in range(1,details["count"]+1):
			remove(join(out, str(x)+".frm"))

if __name__ == "__main__":
	main()
