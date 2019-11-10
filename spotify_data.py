import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError

SPOTIPY_CLIENT_ID = '6172eeb69049476891564b4272c977ed'
SPOTIPY_CLIENT_SECRET = 'cc58a40c94fd40c6b16cd225f1d20084'
SPOTIPY_REDIRECT_URI = 'http://localhost:3000'

scope = 'user-read-recently-played'


def get_spotify_token(user_name = 'yridp68vzs69q3cn7rdijnyo4'):
    token = util.prompt_for_user_token(user_name, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

    if token:
        sp = spotipy.Spotify(auth = token)
        return sp
    return None 

def get_recent_tracks(sp):

    recent_tracks = sp.current_user_recently_played(limit = 50)

    return recent_tracks



