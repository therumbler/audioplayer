#!venv/bin/python
import urllib2
import os
import pygame

from config import soundcloud_client_id
from soundcloud import Soundcloud
import uuid

class Track():
	def __init__(self, **params):
		#initialize the pygame stuff
		pygame.mixer.init()

		#the soundcloud_client_id comes from the config.py file
		self.soundcloud = Soundcloud(client_id = soundcloud_client_id, client_secret = "")

		#for testing (see main() below) we'll be in the lib directory
		#change to parent directory for working with 
		#relative file paths (the etc/ directory)
		if "lib" in os.getcwd():
			os.chdir("..")

		if "url" in params:
			self.load_track(url = params["url"])
		self.is_playing = False

	def load_track(self, url):

		if "soundcloud.com" in url:
			#must be a soundcloud.com url
			self.audio_url = self.soundcloud.get_mp3_url(url = url)
			#print self.audio_url
			self.filename = "etc/audio/%s.mp3" % str(uuid.uuid4())
			print "filename = %s" % self.filename
			
			#download track to disk
			response = urllib2.urlopen(self.audio_url)
			with open("etc/audio/%s" % self.filename, "wb") as f:
				f.write(response.read())

		if ".mp3" in url:
			#it must be a filename
			filename = "etc/audio/%s" % url
			self.filename = filename
	
	def start(self):
		#load some music
		if not self.is_playing:
			pygame.mixer.music.load(self.filename)
			
			pygame.mixer.music.play()
			self.is_playing = True
def main():
	#Test code
	track = Track()
	url = "https://soundcloud.com/mixunion/fractall-gabe-fkls-take-over-free-download"
	url = "a215af12-925a-4147-ac0a-f1d98902fafd.mp3"
	track.load_track(url = url)

if __name__ == '__main__':
	main()