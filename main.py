import spotipy 
import spotipy.util as util 
from json.decoder import JSONDecodeError
import spotify_data
import logic


# MY USER ID: spotify:user:yridp68vzs69q3cn7rdijnyo4


def main(id):
    print(id)

    sp_recent = spotify_data.get_spotify_recent_played_token(id)          #token with permissions to access user's recent songs
    sp_playlist = spotify_data.get_spotify_create_playlist_token(id)      #token to get access to create a playlist for the user


    user_recent_tracks = spotify_data.get_recent_tracks(sp_recent)      #JSON of recent tracks 
    
    songs = logic.get_songs(user_recent_tracks)                         #Dictionary with ID and number of playbacks
    average = logic.average_playcount(songs)                            #Sums all the playbacks, divides by total number of songs


    above_average_list = logic.above_average_songs(average, songs)      #List of song ids that are above the average
    created_playlist = spotify_data.create_playlist(sp_playlist, id)        #creates empty playlist
    new_playlist_id = spotify_data.get_playlist_id(created_playlist)    #obtains empty playlist id

    spotify_data.add_tracks(sp_playlist, new_playlist_id, above_average_list, id)             #adds tracks to the previously empty playlist
    

if __name__ == "__main__":
    main()  