# You might need to add more of these import statements as you implement your controllers.
from app import app
from flask import render_template
from flask import request, redirect, session
from helpers import GENRES_LIST, get_four_songs, get_score, clear_score
import billboard
from utility import get_preview_url
import random
from firebase import firebase

@app.route('/answer', methods=['GET', 'POST'])
def answer():
	leaderboard = firebase.FirebaseApplication('https://dj183-6a1a1.firebaseio.com/')

	answer = request.args.get('answer', None)
	genreAgain = request.args.get('genreAgain', None)
	user_input = request.form['song']
	if (answer == user_input):
		result = 'Correct!'
		session['num_correct'] += 1
		session['num_total'] += 1
		if leaderboard.get('/Percent', answer) != None:
			song_correct = leaderboard.get('/Correct', answer) + 1
			leaderboard.put('/Correct', answer, song_correct)

			song_total = leaderboard.get('/Total', answer) + 1
			leaderboard.put('/Total', answer, song_total)

			song_percent = float(song_correct) / song_total
			leaderboard.put('/Percent', answer, song_percent)

		else:
			song_correct = 1
			song_total = 1
			leaderboard.put('/Correct', answer, song_correct)
			leaderboard.put('/Total', answer, song_total)
			song_percent = float(song_correct) / song_total
			leaderboard.put('/Percent', answer, song_percent)

	else:
		result = 'Incorrect!'
		session['num_total'] += 1

		if leaderboard.get('/Percent', answer) != None:
			song_correct = leaderboard.get('/Correct', answer)

			song_total = leaderboard.get('/Total', answer) + 1
			leaderboard.put('/Total', answer, song_total)

			song_percent = float(song_correct) / song_total
			leaderboard.put('/Percent', answer, song_percent)

		else:
			song_correct = 0
			song_total = 1
			leaderboard.put('/Correct', answer, song_correct)
			leaderboard.put('/Total', answer, song_total)
			song_percent = float(song_correct) / song_total
			leaderboard.put('/Percent', answer, song_percent)

	final_score = get_score()
	final_song_percent = leaderboard.get('/Percent', answer) * 100

	indiv_song_comment = leaderboard.get('/Comments', answer)

	if request.form.get('song_like') == None:
		pass
	else:
		prev_song_like = request.form.get('song_like')
		if prev_song_like == "yes":
			if leaderboard.get('/Likes', answer) != None:
				current_song_likes = leaderboard.get('/Likes', answer)
				current_song_likes += 1
				leaderboard.put('/Likes', answer, current_song_likes)
			else:
				current_song_likes = 1
				leaderboard.put('/Likes', answer, current_song_likes)
			
	if leaderboard.get('/Likes', answer) == None:
		current_song_likes = 0
	else:
		current_song_likes = leaderboard.get('/Likes', answer)
	wrong_percent = 100 - final_song_percent







	data = {
		'answer': answer,
		'user_input': user_input,
		'result': result,
		'genre': genreAgain,
		'final_score': final_score,
		'final_song_percent': final_song_percent,
		'indiv_song_comment': indiv_song_comment,
		'current_song_likes': current_song_likes,
		'wrong_percent': wrong_percent
	}

	# print("PRINT SOMETHING PLEASE")
	# print(songs[choice].title)
	# data = {
	# 	'song': request.form['song']
	# }
	# if request.form['song'] == x[choice].title:
 #        	print('yay')
 #    	else:
 #        		print('NAY')
	# if songs[choice].title == request.form['song']:
	# 	print("yay")
		
	# else:
	# 	print("NAY")

	return render_template("answer.html", **data)

