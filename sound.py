from threading import Thread
from os import system
from os.path import exists


def getaudio(path, output, log):
	log.info("start ffmpeg to extract audio...")
	system(f"ffmpeg -i {path} -acodec libmp3lame -loglevel quiet -metadata TITLE=\"from WM player\" {output}")

class Audio:
	def __init__(self, path):
		self.path = path
	def start(self):
		if not exists(self.path):
			return
		self.thread = Thread(target = self.play, args=())
		self.thread.start()
	def play(self):
		system("play "+self.path+" >/dev/null 2>&1")
