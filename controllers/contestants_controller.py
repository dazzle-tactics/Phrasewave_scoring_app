from flask import Flask, redirect, render_template, request
from flask import Blueprint
from repositories import contestant_repository
from repositories import team_repository
from models.contestant import Contestant

contestants_blueprint = Blueprint("contestants", __name__)

#Index
@contestants_blueprint.route("/contestants")
def contestants():
    contestants = contestant_repository.select_all()
    return render_template("contestants/index.html", all_contestants = contestants)

#New
@contestants_blueprint.route("/contestants/new")
def new_contestant():
    teams = team_repository.select_all()
    return render_template("contestants/new.html", all_teams = teams)

#Create
@contestants_blueprint.route("/contestants", methods=["POST"])
def create_contestant():
    name = request.form['name']
    occupation = request.form['occupation']
    fave_phrase = request.form['fave_phrase']
    team_id = request.form['team_id']
    team = team_repository.select(team_id)
    contestant = Contestant(name, occupation, fave_phrase, team)
    contestant_repository.save(contestant)
    return redirect("/contestants")

#Read
#Edit
#Update
#Delete