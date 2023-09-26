import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from requests import get
from requests import patch
import os
import time
import random









error_message = '{"error":true,"message":"lyrics for this track is not available on spotify!"}'
scope = "user-read-currently-playing"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.currently_playing()
print(results['item']['name'])
curr_track_id = results['item']['id']
def get_lyrics(track_id):
	try : 
		lyrics = get(f"https://spotify-lyric-api.herokuapp.com/?trackid={track_id}").content
		if lyrics.decode() != error_message : 
			lyrics = json.loads(lyrics)
			while lyrics['error'] :
				lyrics = get(f"https://spotify-lyric-api.herokuapp.com/?trackid={track_id}").content
				lyrics = json.loads(lyrics)
			return lyrics
	except : 
		print('connection lost ')
		return ' '
lyrics = get_lyrics(curr_track_id)
previous_time = 0
current_top = 0 
current_bottom = 0


while True : 
	while results['is_playing'] and lyrics != ' ':
		try :
			results = sp.currently_playing()
			current_time = int(results['progress_ms'])
			if results['timestamp'] > 0 :
				lyrics = get_lyrics(results['item']['id'])
			if lyrics != ' ' : 
				for i in range(len(lyrics['lines']) - 1):
					if current_time > int(lyrics['lines'][i]['startTimeMs']) and current_time < int(lyrics['lines'][i + 1]['startTimeMs']) and current_time > previous_time :
						print(lyrics['lines'][i]['words'])
						previous_time = int(lyrics['lines'][i + 1]['startTimeMs'])
						curr_lyrics = (lyrics['lines'][i]['words'])
						with open('lyrics.txt', 'w',encoding='utf8') as f:
							f.write(curr_lyrics)

						current_top = int(lyrics['lines'][i + 1]['startTimeMs'])
						current_bottom = int(lyrics['lines'][i]['startTimeMs'])


			if current_time < current_bottom or current_time > current_top:
				previous_time = 0
		except : 
			print('connection lost')


	time.sleep(1)
	try :
		results = sp.currently_playing()
		if results['timestamp'] > 0 :
			lyrics = get_lyrics(results['item']['id'])
	except : 
		print('Connection lost')
