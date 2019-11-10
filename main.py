import spotipy 
import spotipy.util as util 
from json.decoder import JSONDecodeError
import spotify_data
import logic


# MY USER ID: spotify:user:yridp68vzs69q3cn7rdijnyo4


def main():
    sp_recent = spotify_data.get_spotify_recent_played_token()
    #user_recent_tracks = spotify_data.get_recent_tracks(sp_recent)
    #print(user_recent_tracks)
    sp_playlist = spotify_data.get_spotify_create_playlist_token()

    

if __name__ == "__main__":
    main()  