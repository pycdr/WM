# used in <text> and < function
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

# like <text> function, but render coloring output!
def colorhex(array):
	l = [hex(x)[2:] for x in array]
	l = [(x+"0" if len(x)<2 else x) for x in l]
	return "".join(l)

def ctext(array):
	out = ""
	for x in array:
		for y in x:
			c = colorhex(y)
			out += c
			d = sum(y)//3
			out += char(d)
		out += "\n"
	return out

# convert function (video -> TXTs)
def convert(path, output, w, h, log, color):
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
	func = ctext if color else text
	while cap.isOpened():
		ret, frame = cap.read()
		if not ret:
			break
		if not color:
			frame = cvtColor(frame, COLOR_BGR2GRAY)
		out = resize(frame, (w, h))
		txt = func(out)
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
