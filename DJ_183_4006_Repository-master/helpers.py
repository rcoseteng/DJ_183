# Add more import statements as you need them!
from utility import get_four_choices, get_three_choices, get_five_choices
import billboard
from flask import session



"""
Our dictionary to hold which genres we are giving to our users. Play around with
this dictionary to see how the starter code changes on index.html. The keys
represent the names as they appear on the website, and the values represent the
chart IDs for Billboard to use.

TODO: Add at least two more genres to this dictionary. Information on how to find
      more Billboard chart IDs is on the Billboard library documentation, as
      linked on the core page of the spec. Make sure you only choose charts that
      contain SONGS (not artists, albums, etc.).
"""

GENRES_LIST = {
    "Current Pop Hits": "hot-100",
    "Dance Club Hits": "dance-club-play-songs",
    "Rock": "rock-songs",
    "Holiday Classics": "hot-holiday-songs",
    "Latin": "latin-songs" 
}

"""
REQUIRES: a valid chart name that corresponds to a chart name on Billboard
MODIFIES: nothing
EFFECTS: chooses four random songs from the valid Billboard chart and returns
         result in a list. Uses get_four_choices() and the Billboard library.
         Remember: if you want to use a library in Python, what must we put at
         the top of the file to access its member functions?
"""
def get_four_songs(chart_name):
    # return get_four_choices(chart_name)
    # get a list of 4 numbers
    # use billboard to get 4 songs -> numbers
    # return list of songs
    chart = billboard.ChartData(chart_name)
    numsongs = get_four_choices(chart)
    songs = []
    for num in numsongs:
      songs.append(chart[num])
    return songs
"""
REQUIRES: nothing
MODIFIES: nothing
EFFECTS: returns a string with the score to print
"""
def get_score():
    # final_score = str(session.num_correct) + "/" + str(session.num_total)
    # return final_score
    final_score = str(session.get('num_correct')) + ' / ' + str(session.get('num_total'))
    return final_score
    
"""
REQUIRES: nothing
MODIFIES: num_correct, num_total in session
EFFECTS: sets the num_correct and num_total to 0
"""
def clear_score():
    session['num_correct'] = 0
    session['num_total'] = 0
    
    return 

def get_three_songs(chart_name):
    
    chart = billboard.ChartData(chart_name)
    numsongs = get_three_choices(chart)
    songs = []
    for num in numsongs:
      songs.append(chart[num])
    return songs

def get_five_songs(chart_name):
    
    chart = billboard.ChartData(chart_name)
    numsongs = get_five_choices(chart)
    songs = []
    for num in numsongs:
      songs.append(chart[num])
    return songs