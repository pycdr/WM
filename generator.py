# used in text() function
d = " ·!┼║▒▓█"
def char(number):
	return d[number*len(d)//256]

# make text from array(frame)
def text(array):
	out = ""
	for x in array:
		for y in x:
			out += char(y)
		out += "\n"
	return out

# convert function (video -> TXTs)
def convert(path, output, w, h, log):
	log.info("importing...")
	from cv2 import (
		VideoCapture,
		cvtColor,
		COLOR_BGR2GRAY,
		resize,
		CAP_PROP_FRAME_COUNT,
		CAP_PROP_FPS
	)
	from os.path import join
	log.info("create VideoCapture object...")
	cap = VideoCapture(path)
	log.info("get details of video...")
	count = int(cap.get(CAP_PROP_FRAME_COUNT))
	fps = int(cap.get(CAP_PROP_FPS))
	n = 1
	log.info("start convert loop")
	while cap.isOpened():
		ret, frame = cap.read()
		if not ret:
			break
		gray = cvtColor(frame, COLOR_BGR2GRAY)
		out = resize(gray, (w, h))
		txt = text(out)
		with open(join(output, str(n)+".txt"), "w+") as f:
			f.write(txt)
			f.close()
		n+=1
		print(f"converting to text files: {n*100//count}%", end='\r')
	log.info("converting finished. release VideoCapture")
	cap.release()
	return {
		"fps": fps,
		"count": count
	}

# function which is run when the program is running
def main():
	from argparse import ArgumentParser
	from os import makedirs, get_terminal_size as size
	from os.path import exists
	
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

# run if it is not imported as a module
if __name__ == "__main__":
	main()
