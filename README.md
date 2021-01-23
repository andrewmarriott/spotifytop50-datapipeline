# Spotify-Top50Playlists

The goal of this project was to use the Spotify API to pull the 'Spotify Top-50' playlist for every country and look at differences in music taste globally.

The first API call fetches the tracks from all 64 playlists. It then fetches the audio features for each individual track using a separate function, as this data could not be obtained with the first call (description of the audio features be found here: https://developer.spotify.com/documentation/web-api/reference/#endpoint-get-audio-features).

The Country table stores the track name and artist along with what playlist it was on. The Track table stores the audio features for each track. This structure was chosen to limit the number of API calls needed to grab the audio features keeping in mind there were duplicate tracks across the country playlists.

These two tables can be JOINED to get a master view of all the tracks and their features for every playlist.

