
def get_songs(data: dict) -> dict:
    """ Returns a dictionary of song titles: playbacks from data given."""
    songs = dict()
    for item in data["items"]:
        name = item["track"]["name"]
        if name in songs:
          songs.update({name: songs[name]+1})
        else:
          songs[name] = 1
    return songs
 


def average_playcount(songs : dict) -> float:
    """ Returns the average number of playbacks. """
    sum = 0
    number_of_playcounts = len(songs)
    for playback in songs.values():
        sum += playback
    average = sum / number_of_playcounts
    return average

def above_average_songs(average: float, songs: dict)-> [str]:
    """ Returns a list of song titles with playbacks greater than average playbacks."""
    songs = sorted(songs.items(), key = 
             lambda kv:(kv[1], kv[0]), reverse = True)
    top_songs = []
    if average == 1:
        print("You've only played each song once.")
        return songs.keys()
    for song in songs:
        name = song[0]
        plays = song[1]
        if plays > average:
            top_songs.append(name)
    return top_songs

    



            
            
        




