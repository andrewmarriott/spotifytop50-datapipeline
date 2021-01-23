import mysql.connector
from spotify import *
from playlists import *
from database import *
import time

#datetime
dt = time.strftime('%Y-%m-%d %H:%M:%S')

#cursor for INSERTING data
mycursor = db.cursor()
#cursor for SELECTING data
selcursor = db2.cursor()



for playlist in get_playlist_data(playlist_links):


	#terminal log
	print('\n')
	print(f"Pulling data for {playlist['name']}")
	print('\n')


	#add tracks to the country table if new and update date if already exists
	for track in playlist['tracks']['items']:
		try:
			mycursor.execute(country_insert_query,

				(	playlist['name'][:-7],
					track['track']['name'],
					track['track']['artists'][0]['name'],
					dt
				)
			)
			print(f"{track['track']['name']} added for country {playlist['name'][:-7]} on country table")

		except mysql.connector.errors.IntegrityError as e:
			mycursor.execute(country_update_query,
				( 	playlist['name'][:-7], 
					track['track']['name'], 
					track['track']['artists'][0]['name'],
					dt
				)
			) 
			print(f"{track['track']['name']} already exists for {playlist['name'][:-7]} on country table - updating date")
	db.commit()


	#add tracks to the track table
	for track in playlist['tracks']['items']:
		#check if the track exists in the table
		selcursor.execute(select_query, 

				(	track['track']['name'],
					track['track']['artists'][0]['name']
				)
			)
		result = selcursor.fetchone()
		#if exists skip
		if result:
			print(f"{track['track']['name']} already exists for artist {track['track']['artists'][0]['name']} on track table")
		#if not add it to track_data table
		else:
			track_audio_data = get_track_audio_data(track)
			mycursor.execute(track_data_query,

				(	track['track']['name'],
					track['track']['artists'][0]['name'],
					None,
					track_audio_data['audio_features'][0]['tempo'],
					track_audio_data['audio_features'][0]['key'],
					track_audio_data['audio_features'][0]['duration_ms'],
					track_audio_data['audio_features'][0]['time_signature'],
					track_audio_data['audio_features'][0]['danceability'],
					track_audio_data['audio_features'][0]['energy'],
					track_audio_data['audio_features'][0]['loudness'],
					track_audio_data['audio_features'][0]['speechiness'],
					track_audio_data['audio_features'][0]['acousticness'],
					track_audio_data['audio_features'][0]['liveness'],
					track_audio_data['audio_features'][0]['valence']
				)
			)
			print(f"{track['track']['name']} added for artist {track['track']['artists'][0]['name']} on track table")
			db2.commit()


print('\n')
print('finished!')
