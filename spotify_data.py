import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError

export SPOTIPY_CLIENT_ID = '6172eeb69049476891564b4272c977ed'
export SPOTIPY_CLIENT_SECRET = 'cc58a40c94fd40c6b16cd225f1d20084'
export SPOTIPY_REDIRECT_URI = 'http://www.google.com'

def get_spotify_token(user_name):
    token = util.prompt_for_user_token(user_name, user-read-recently-played)

    if token: 
        return token
    else: 
        print("The user {}'s token cannot be accessed".format(user_name))

def get_recent_tracks(token):

    sp = spotipy.Spotify(auth = token)

    recent_tracks = spotipy.current_user_recently_played(limit = 50)

    return recent_tracks



