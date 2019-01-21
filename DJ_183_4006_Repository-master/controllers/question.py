# You might need to add more of these import statements as you implement your controllers.
from app import app
from flask import render_template
from flask import request, redirect, session
from helpers import GENRES_LIST, get_four_songs, get_score, clear_score, get_three_songs, get_five_songs
import billboard
from utility import get_preview_url
import random



@app.route('/q', methods=['POST'])
def q():
	difficulty_level = request.form['difficulty']	
	session['difficulty_level'] = difficulty_level
	data = {
		'genre': GENRES_LIST[request.form['genre']],
	}
	return redirect('/question/{}'.format(data['genre']))
    	

@app.route('/question/<genre>', methods=['GET', 'POST'])
def question(genre):
	
	
	if session.get('difficulty_level') == "Normal":
		choice = random.randrange(0,4)
		songs = get_four_songs(genre)
		try:
			url = get_preview_url(songs[choice].title, songs[choice].artist)["url"]
		except:
			songs = get_four_songs(genre)
			url = get_preview_url(songs[choice].title, songs[choice].artist)["url"]
	elif session.get('difficulty_level') == "Easy":
		choice = random.randrange(0,3)
		songs = get_three_songs(genre)
		try:
			url = get_preview_url(songs[choice].title, songs[choice].artist)["url"]
		except:
			songs = get_three_songs(genre)
			url = get_preview_url(songs[choice].title, songs[choice].artist)["url"]
	else:
		choice = random.randrange(0,5)
		songs = get_five_songs(genre)
		try:
			url = get_preview_url(songs[choice].title, songs[choice].artist)["url"]
		except:
			songs = get_five_songs(genre)
			url = get_preview_url(songs[choice].title, songs[choice].artist)["url"]


	final_score = get_score()
	if session.get('num_total') == 0:
		clear_score()
		final_score = "N/A"


	
	return render_template("question.html", songs=songs, url=url, choice=choice, genre=genre, final_score=final_score)


