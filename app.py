#!venv/bin/python
from lib.mixer import Mixer
from lib.track import Track
import time
url = "https://soundcloud.com/mixunion/fractall-gabe-fkls-take-over-free-download"
url = "a215af12-925a-4147-ac0a-f1d98902fafd.mp3"
track = Track(url = url)
mixer = Mixer()
track.start()
mixer.add_track(track)




while True:
	time.sleep(1)