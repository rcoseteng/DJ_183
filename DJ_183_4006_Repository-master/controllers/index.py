# You might need to add more of these import statements as you implement your controllers.
from app import app
from flask import render_template, session, request, redirect, url_for, Flask
from helpers import GENRES_LIST, get_score, clear_score
from question import question
from firebase import firebase
import operator




@app.route('/', methods=['GET', 'POST'])
def index():

	leaderboard = firebase.FirebaseApplication('https://dj183-6a1a1.firebaseio.com/')



	clearing_score = request.form.get("choice")
	if clearing_score == "yes":
		temp_score = session["num_correct"]
		if request.form.get("username") == "":
			pass
		else: 
			temp_username = request.form.get("username")
			leaderboard.put('/Highscores', temp_username, temp_score)

		clear_score()

	final_score = get_score()

	if session.get('num_total') > 0:
		temp = 0

	else:
		clear_score()
		final_score = "N/A"



	highscores = leaderboard.get('/Highscores', None)

	sorted_highscores = sorted(highscores.items(), key=operator.itemgetter(1), reverse=True)
	while len(sorted_highscores) > 5:
		sorted_highscores.pop()

	if request.form.get("comment_song") != None:
		song_comment = request.form.get("comment_song")
		song_to_comment = request.form.get("answer_song")
		leaderboard.put('/Comments', song_to_comment, song_comment)

	difficulty = ["Easy", "Normal", "Difficult"]

	data = {
	    "genres": GENRES_LIST,
	    "final_score": final_score,
	    "sorted_highscores": sorted_highscores,
	    "difficulty": difficulty
	}
	

	return render_template("index.html", **data)
