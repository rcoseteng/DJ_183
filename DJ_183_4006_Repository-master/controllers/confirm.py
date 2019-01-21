from app import app
from flask import render_template, session, request, redirect, url_for, Flask
from helpers import GENRES_LIST, get_score, clear_score
from question import question


@app.route('/confirm', methods=['GET', 'POST'])
def confirm():

	final_score = get_score()

	
	if session.get('num_total') == 0:
		clear_score()
		final_score = "N/A"

	

	data = {
	    "final_score": final_score
	}
	return render_template("confirm.html", **data)
