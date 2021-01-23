# Spotify-Top50Playlists

The intention of this project was to use the Spotify API to pull the Top-50 playlists for every country and look at differences in music taste globally.

This data pipeline uses the Spotify API to grab all tracks from each of the Spotify's Top 50 country-specific playlists (64 playlists in total).
It then fetches the audio features for each track using a separate function (description of these can be found here: https://developer.spotify.com/documentation/web-api/reference/#endpoint-get-audio-features).

The Country table stores the track name and artist along with what playlist it was on. The Track table stores the audio features for each track. This structure was chosen to limit the number of API calls needed to grab the audio features keeping in mind there were duplicate tracks across the country playlists.

These two tables can be JOINED to get a master view of all the tracks and their features for every playlist.

