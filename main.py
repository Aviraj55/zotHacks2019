import spotipy 
import spotipy.util as util 
from json.decoder import JSONDecodeError
import spotify_data


# MY USER ID: spotify:user:yridp68vzs69q3cn7rdijnyo4


def main():
    sp = spotify_data.get_spotify_token()
    user_recent_tracks = spotify_data.get_recent_tracks(sp)
    print(user_recent_tracks)

if __name__ == "__main__":
    main()  