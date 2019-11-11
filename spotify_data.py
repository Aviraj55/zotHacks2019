import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError

SPOTIPY_CLIENT_ID = '6172eeb69049476891564b4272c977ed'
SPOTIPY_CLIENT_SECRET = 'cc58a40c94fd40c6b16cd225f1d20084'
SPOTIPY_REDIRECT_URI = 'http://localhost:3000'



def get_spotify_recent_played_token(username):
    scope = 'user-read-recently-played'
    token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

    if token:
        sp = spotipy.Spotify(auth = token)
        return sp
    return None 

def get_recent_tracks(sp):
    recent_tracks = sp.current_user_recently_played(limit = 50)
    return recent_tracks


def get_spotify_create_playlist_token(username):
    scope = 'playlist-modify-public'
    token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

    if token:
        sp = spotipy.Spotify(auth = token)
        return sp
    return None

def create_playlist(sp, username = 'yridp68vzs69q3cn7rdijnyo4'):
    new_playlist = sp.user_playlist_create(username, "Your Top Hits!", public = True, description = "A playlist made for you courtesy of zotHacks :)")
    return new_playlist


def get_playlist_id(playlist):
    return playlist['id']

def add_tracks(sp, playlist_id, tracks, username = 'yridp68vzs69q3cn7rdijnyo4'):
    sp.user_playlist_add_tracks(username, playlist_id, tracks)

def get_user_id(sp, id):
    sp.current_user()

