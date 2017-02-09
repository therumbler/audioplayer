#!venv/bin/python
import urllib2
import os
import pygame

from config import soundcloud_client_id
from soundcloud import Soundcloud
import uuid

class Track():
	def __init__(self, **params):
		pygame.mixer.init()
		self.buffer = None
		self.init_soundcloud()
		if "url" in params:
			self.load_track(url = params["url"])

	def init_soundcloud(self):
		self.soundcloud = Soundcloud(client_id = soundcloud_client_id, client_secret = "")
	

	def load_track(self, url):		
		if "lib" in os.getcwd():
			os.chdir("..")

		if "soundcloud" in url:
			self.audio_url = self.soundcloud.get_mp3_url(url = url)
			#print self.audio_url
			self.filename = "etc/audio/%s.mp3" % str(uuid.uuid4())
			print "filename = %s" % self.filename
			#download track
			response = urllib2.urlopen(self.audio_url)
			with open("etc/audio/%s" % self.filename, "wb") as f:
				f.write(response.read())

		if ".mp3" in url:
			filename = "etc/audio/%s" % url
			self.filename = filename

	def get_buffer(self, filename):
		if "etc" not in filename:
			filename = "etc/audio/%s" % filename

		with open(filename) as f:
			self.buffer = filename
	
	def start(self):
		pygame.mixer.music.load(self.filename)
		pygame.mixer.music.play()
	


def main():
	#Test code
	track = Track()
	url = "https://soundcloud.com/mixunion/fractall-gabe-fkls-take-over-free-download"
	url = "a215af12-925a-4147-ac0a-f1d98902fafd.mp3"
	track.load_track(url = url)

if __name__ == '__main__':
	main()