#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-

import urllib2, urllib
import json
import sys

class Soundcloud():
	def __init__(self, client_id, client_secret, url = False):
		self.CLIENT_ID = client_id
		self.CLIENT_SECRET = client_secret

		if url:
			self.track = self.resolve(url)

	def resolve(self, url):
		uri = "https://api.soundcloud.com/resolve.json?url=%s&client_id=%s" % (url, self.CLIENT_ID)
		try:
			response = urllib2.urlopen(uri)
			track = json.load(response)
			return track
			
		except urllib2.HTTPError, e:
			return {
				"error": e.code,
				"reason": str(e),
				"detail": "Soundcloud error"
			}

	def get_mp3_url(self, track):
		url = ""
		if track["downloadable"] == True:
			url = self.track["download_url"] + "/?client_id=" + self.CLIENT_ID
		elif track["streamable"] == True:
			url = track["stream_url"] + "/?client_id=" + self.CLIENT_ID
		else:
			return {
				"error": 403,
				"reason": "Forbidden",
				"detail": "Track at " + url + " is not streamable"
			}

		try:
			request = urllib2.urlopen(url)
			url = request.geturl()
			return url

		except urllib2.HTTPError, e:
			return {
				"error": e.code,
				"reason": str(e),
				"detail": "Stream url for " + url + " is returning an error"
			}

	def get_embed_html(self):
		return '<iframe id="scwidget" width="100%" height="166" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/%s&amp;auto_play=true"></iframe>' % self.track["id"]

	def search(self, **args):
		q = urllib.urlencode(args)
		uri = "https://api.soundcloud.com/tracks.json?client_id=" + self.CLIENT_ID + "&" + q
		#for key, value in args.iteritems():
		#	uri += "&%s=%s" % (key, value)
		#uri += "&limit=50"
		#print uri
		response = urllib2.urlopen(uri)
		#response = request.read()
		return json.load(response)

	def get(self, endpoint, **params):
		if "client_id" not in params.keys():
			params["client_id"] = self.CLIENT_ID

		qs = urllib.urlencode(params)
		bracketed_params = [
			"bpm_to",
			"bpm_from",
			"duration"
		]
		url = "https://api.soundcloud.com/%s?%s" % (endpoint, qs)
		#print url
		response = urllib2.urlopen(url)
		
		return json.load(response)

	def get_track_by_id(self, track_id):
		track = self.get("tracks/%s.json" % track_id)
		return track

	def download_track(self, **params):
		if "track_id" in params.keys():
			track = self.get_track_by_id(params["track_id"])

		if "url" in params.keys():
			track = self.resolve(params["url"])

		mp3_url = self.get_mp3_url(track)
		filename = "%s.mp3" % track["title"]

		response = urllib2.urlopen(mp3_url["mp3_url"])
		with open("audio/%s" % filename, "wb") as f:
			f.write(response.read())
		return True

if __name__ == '__main__':
	CLIENT_ID = "51762b5b2ec86582ea95a9d816077654"
	CLIENT_SECRET = "9923d03b898d96820129c1b6720d915c"
	sc = Soundcloud(CLIENT_ID, CLIENT_SECRET)

	#sc_id = 203876284
	sc_id = 209361534
	sc_id = 218678138
	
	#response = sc.get_track(sc_id)
	#print sc.get_mp3_url()
	#response = sc.get("tracks.json", q = "ben pearce", duration5bto5d = "b")
	#print json.dumps(response, indent = 4)
	#	secret_token%3Ds-pksbV

	#print json.dumps(sc.get_track(sc_id), indent = 4)

	#response = sc.get("playlists/104962322.json", secret_token = "s-zhVNL")
	#print json.dumps(response, indent = 4)

	url = "https://soundcloud.com/dukedumont/mumble-man-for-club-play-only-part-3"
	url = "https://soundcloud.com/tmtrecords/austin-ato-dreams/"
	
	track_id = 267314064
	url = "https://soundcloud.com/user-816750376/gm-feat-drz-back-on-road-mix-1-3db-fix-master"
	url = "https://soundcloud.com/l4xbr0/motorola-prod-by-kendric-newburn"
	url = "https://soundcloud.com/user-660473664/breeze"
	sc.download_track(url = url)
	#print sc.resolve(url)

	args = {
		"duration[to]" : 900000,
		"q": "ben pearce"
	}

	q = urllib.urlencode(args)
	#print q
	#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-

import urllib2, urllib
import json
import sys

class Soundcloud():
	def __init__(self, client_id, client_secret, url = False):
		self.CLIENT_ID = client_id
		self.CLIENT_SECRET = client_secret

		if url:
			self.track = self.resolve(url)

	def resolve(self, url):
		uri = "https://api.soundcloud.com/resolve.json?url=%s&client_id=%s" % (url, self.CLIENT_ID)
		print url
		try:
			response = urllib2.urlopen(uri)
			track = json.load(response)
			return track
			
		except urllib2.HTTPError, e:
			return {
				"error": e.code,
				"reason": str(e),
				"detail": "Soundcloud error"
			}

	def get_mp3_url(self, track):
		url = ""
		if track["downloadable"] == True:
			url = self.track["download_url"] + "/?client_id=" + self.CLIENT_ID
		elif track["streamable"] == True:
			url = track["stream_url"] + "/?client_id=" + self.CLIENT_ID
		else:
			return {
				"error": 403,
				"reason": "Forbidden",
				"detail": "Track at " + url + " is not streamable"
			}

		try:
			request = urllib2.urlopen(url)
			url = request.geturl()
			return {
				"mp3_url" : url
			}

		except urllib2.HTTPError, e:
			return {
				"error": e.code,
				"reason": str(e),
				"detail": "Stream url for " + url + " is returning an error"
			}

	def get_embed_html(self):
		return '<iframe id="scwidget" width="100%" height="166" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/%s&amp;auto_play=true"></iframe>' % self.track["id"]

	def search(self, **args):
		q = urllib.urlencode(args)
		uri = "https://api.soundcloud.com/tracks.json?client_id=" + self.CLIENT_ID + "&" + q
		#for key, value in args.iteritems():
		#	uri += "&%s=%s" % (key, value)
		#uri += "&limit=50"
		#print uri
		response = urllib2.urlopen(uri)
		#response = request.read()
		return json.load(response)

	def get(self, endpoint, **params):
		if "client_id" not in params.keys():
			params["client_id"] = self.CLIENT_ID

		qs = urllib.urlencode(params)
		bracketed_params = [
			"bpm_to",
			"bpm_from",
			"duration"
		]
		url = "https://api.soundcloud.com/%s?%s" % (endpoint, qs)
		#print url
		response = urllib2.urlopen(url)
		
		return json.load(response)

	def get_track_by_id(self, track_id):
		track = self.get("tracks/%s.json" % track_id)
		return track

	def download_track(self, **params):
		if "track_id" in params.keys():
			track = self.get_track_by_id(params["track_id"])

		if "url" in params.keys():
			track = self.resolve(params["url"])

		mp3_url = self.get_mp3_url(track)
		filename = "%s.mp3" % track["title"]

		response = urllib2.urlopen(mp3_url["mp3_url"])
		with open("audio/%s" % filename, "wb") as f:
			f.write(response.read())
		return True

if __name__ == '__main__':
	CLIENT_ID = "51762b5b2ec86582ea95a9d816077654"
	CLIENT_SECRET = "9923d03b898d96820129c1b6720d915c"
	sc = Soundcloud(CLIENT_ID, CLIENT_SECRET)

	#sc_id = 203876284
	sc_id = 209361534
	sc_id = 218678138
	
	#response = sc.get_track(sc_id)
	#print sc.get_mp3_url()
	#response = sc.get("tracks.json", q = "ben pearce", duration5bto5d = "b")
	#print json.dumps(response, indent = 4)
	#	secret_token%3Ds-pksbV

	#print json.dumps(sc.get_track(sc_id), indent = 4)

	#response = sc.get("playlists/104962322.json", secret_token = "s-zhVNL")
	#print json.dumps(response, indent = 4)

	url = "https://soundcloud.com/dukedumont/mumble-man-for-club-play-only-part-3"
	url = "https://soundcloud.com/tmtrecords/austin-ato-dreams/"
	
	track_id = 267314064
	url = "https://soundcloud.com/user-816750376/gm-feat-drz-back-on-road-mix-1-3db-fix-master"
	url = "https://soundcloud.com/l4xbr0/motorola-prod-by-kendric-newburn"
	url = "https://soundcloud.com/user-660473664/breeze"
	sc.download_track(url = url)
	#print sc.resolve(url)

	args = {
		"duration[to]" : 900000,
		"q": "ben pearce"
	}

	q = urllib.urlencode(args)
	#print q
	#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-

import urllib2, urllib
import json
import sys

class Soundcloud():
	def __init__(self, client_id, client_secret, url = False):
		self.CLIENT_ID = client_id
		self.CLIENT_SECRET = client_secret

		if url:
			self.track = self.resolve(url)

	def resolve(self, url):
		uri = "https://api.soundcloud.com/resolve.json?url=%s&client_id=%s" % (url, self.CLIENT_ID)
		try:
			response = urllib2.urlopen(uri)
			track = json.load(response)
			return track
			
		except urllib2.HTTPError, e:
			return {
				"error": e.code,
				"reason": str(e),
				"detail": "Soundcloud error"
			}

	def get_mp3_url(self, url = False, track = False):		
		if not track:
			track = self.resolve(url)

		if track["downloadable"] == True:
			url = self.track["download_url"] + "/?client_id=" + self.CLIENT_ID
		elif track["streamable"] == True:
			url = track["stream_url"] + "/?client_id=" + self.CLIENT_ID
		else:
			return {
				"error": 403,
				"reason": "Forbidden",
				"detail": "Track at " + url + " is not streamable"
			}

		try:
			request = urllib2.urlopen(url)
			url = request.geturl()
			return url
			

		except urllib2.HTTPError, e:
			return {
				"error": e.code,
				"reason": str(e),
				"detail": "Stream url for " + url + " is returning an error"
			}

	def get_embed_html(self):
		return '<iframe id="scwidget" width="100%" height="166" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/%s&amp;auto_play=true"></iframe>' % self.track["id"]

	def search(self, **args):
		q = urllib.urlencode(args)
		uri = "https://api.soundcloud.com/tracks.json?client_id=" + self.CLIENT_ID + "&" + q
		#for key, value in args.iteritems():
		#	uri += "&%s=%s" % (key, value)
		#uri += "&limit=50"
		#print uri
		response = urllib2.urlopen(uri)
		#response = request.read()
		return json.load(response)

	def get(self, endpoint, **params):
		if "client_id" not in params.keys():
			params["client_id"] = self.CLIENT_ID

		qs = urllib.urlencode(params)
		bracketed_params = [
			"bpm_to",
			"bpm_from",
			"duration"
		]
		url = "https://api.soundcloud.com/%s?%s" % (endpoint, qs)
		#print url
		response = urllib2.urlopen(url)
		
		return json.load(response)

	def get_track_by_id(self, track_id):
		track = self.get("tracks/%s.json" % track_id)
		return track

	def download_track(self, **params):
		if "track_id" in params.keys():
			track = self.get_track_by_id(params["track_id"])

		if "url" in params.keys():
			track = self.resolve(params["url"])

		mp3_url = self.get_mp3_url(track)
		filename = "%s.mp3" % track["title"]

		response = urllib2.urlopen(mp3_url["mp3_url"])
		with open("audio/%s" % filename, "wb") as f:
			f.write(response.read())
		return True

if __name__ == '__main__':
	CLIENT_ID = "51762b5b2ec86582ea95a9d816077654"
	CLIENT_SECRET = "9923d03b898d96820129c1b6720d915c"
	sc = Soundcloud(CLIENT_ID, CLIENT_SECRET)

	#sc_id = 203876284
	sc_id = 209361534
	sc_id = 218678138
	
	#response = sc.get_track(sc_id)
	#print sc.get_mp3_url()
	#response = sc.get("tracks.json", q = "ben pearce", duration5bto5d = "b")
	#print json.dumps(response, indent = 4)
	#	secret_token%3Ds-pksbV

	#print json.dumps(sc.get_track(sc_id), indent = 4)

	#response = sc.get("playlists/104962322.json", secret_token = "s-zhVNL")
	#print json.dumps(response, indent = 4)

	url = "https://soundcloud.com/dukedumont/mumble-man-for-club-play-only-part-3"
	url = "https://soundcloud.com/tmtrecords/austin-ato-dreams/"
	url = "https://soundcloud.com/mixunion/fractall-gabe-fkls-take-over-free-download"
	track_id = 267314064
	url = "https://soundcloud.com/user-816750376/gm-feat-drz-back-on-road-mix-1-3db-fix-master"
	url = "https://soundcloud.com/l4xbr0/motorola-prod-by-kendric-newburn"
	url = "https://soundcloud.com/user-660473664/breeze"
	sc.download_track(url = url)
	#print sc.resolve(url)

	args = {
		"duration[to]" : 900000,
		"q": "ben pearce"
	}

	q = urllib.urlencode(args)
	#print q
	