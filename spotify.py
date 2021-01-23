import base64
from urllib.parse import urlencode
import requests


client_id = ''
client_secret = ''


def get_client_creds():
	client_creds = f"{client_id}:{client_secret}"
	client_creds_b64 = base64.b64encode(client_creds.encode())
	return client_creds_b64.decode()


#request access token from Spotify server
def authentication():
	client_creds_b64 = get_client_creds()
	token_url = "https://accounts.spotify.com/api/token"
	token_data = {
			"grant_type": "client_credentials" 
		}
	token_headers = { 
			"Authorization": f"Basic {client_creds_b64}"
		}
	r = requests.post(token_url, data=token_data, headers=token_headers)
	data = r.json()
	access_token = data['access_token']
	return access_token


#use access token to pull playlist tracks from Spotify API (playlist endpoint)
def get_playlist_data(playlist_links):
	playlist_data = []
	access_token = authentication()
	headers = {
			"Authorization": f"Bearer {access_token}" 
        }
	for link in playlist_links:
		playlist_id = link[17:]
		endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}"
		lookup_url = endpoint
		r = requests.get(lookup_url, headers=headers)
		playlist_data.append(r.json())
	return playlist_data



def get_track_audio_data(track):
	track_data = []
	access_token = authentication()
	headers = {
		"Authorization": f"Bearer {access_token}"
	}
	success = False
	while success != True:
		try:
			track_uri = track['track']['uri']
			track_ids = track_uri[14:]
			endpoint = "https://api.spotify.com/v1/audio-features/"
			data = urlencode({"ids": track_ids})
			lookup_url = f"{endpoint}?{data}"
			r = requests.get(lookup_url, headers=headers)
			track_audio_data = r.json()
			success = True
		except:
			print(f"Spotify API connection failed for {track['track']['name']}! trying again...")
	return track_audio_data


