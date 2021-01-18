def getaudio(path, output, log):
	from os import system
	print("~ sound exporter...")
	log.info("start ffmpeg to extract audio...")
	system(f"ffmpeg -i {path} -acodec libmp3lame -loglevel quiet -metadata TITLE=\"from WM player\" {output}")

from threading import Thread
#from playsound import playsound
from os import system
from os.path import exists
from time import sleep

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
		#playsound(self.path)
