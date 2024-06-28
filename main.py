import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from requests import get
from requests import patch
import os
import time
import random


Caching = True
error_message = '{"error":true,"message":"lyrics for this track is not available on spotify!"}'
scope = "user-read-currently-playing"
folder_path = 'Caching'


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.currently_playing()
print(results['item']['name'])
curr_track_id = results['item']['id']
def get_lyrics(track_id):

	# ---------------- Caching
	all_items = os.listdir(folder_path)
	files = [f for f in all_items if os.path.isfile(os.path.join(folder_path, f))]
	if track_id in files and Caching:
		cache_path = f'Caching/{track_id}'
		with open(cache_path, 'r') as json_file:
			data = json.load(json_file)
		return(data)
	else:
		try : 

			lyrics = get(f"https://lyrix.vercel.app/getLyrics/{track_id}").content
			if lyrics.decode() != error_message : 
				lyrics = json.loads(lyrics)
				subfolder_path = 'Caching'
				file_path = os.path.join(subfolder_path, track_id)
				with open(file_path, 'w') as file:
					json.dump(lyrics, file)
				print('Added to cache')


				return lyrics
		except : 
			print('connection lost 1 ')
			return ' '
lyrics = get_lyrics(curr_track_id)['lyrics']
previous_time = 0
current_top = 0 
current_bottom = 0


while True : 
	while results is not None:
		if results['is_playing'] == True and lyrics != ' ':
			try :
				prev_song_playing = results['item']['id']
				results = sp.currently_playing()
				current_time = int(results['progress_ms'])
				if results['timestamp'] > 0 	:
					lyrics = (get_lyrics(results['item']['id']))['lyrics']
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
				print('connection lost ')
		else: 
			break


	time.sleep(1)
	try :
		results = sp.currently_playing()
		if results['timestamp'] > 0 :
			lyrics = get_lyrics(results['item']['id'])
	except : 
		print('Connection lost ')







