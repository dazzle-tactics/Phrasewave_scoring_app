from flask import Flask, redirect, render_template, request
from flask import Blueprint
from repositories import contestant_repository
from repositories import team_repository
from models.contestant import Contestant

contestants_blueprint = Blueprint("contestants", __name__)

#Index
@contestants_blueprint.route("/contestants")
def contestant():
    contestants = contestant_repository.select_all()
    return render_template("contestants/index.html", contestants = contestants)

#New
@contestants_blueprint.route("/contestants/new")
def new_contestant():
    teams = team_repository.select_all()
    return render_template("contestants/new.html", teams=teams)

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
@contestants_blueprint.route("/contestants/<id>")
def show_contestant(id):
    contestant = contestant_repository.select(id)
    return render_template('contestants/show.html', contestant=contestant)
#Edit
#Update

@contestants_blueprint.route("/contestants/<id>/edit", methods=['GET'])
def edit_contestant_form(id):
    team = team_repository.select_all()
    contestant = contestant_repository.select(id)
    return render_template('contestants/edit.html', contestant=contestant, team=team)

@contestants_blueprint.route("/contestants/<id>/edit", methods = ["POST"])
def update_contestant(id):
    name = request.form['name']
    occupation = request.form['occupation']
    fave_phrase = request.form['fave_phrase']
    team = team_repository.select(request.form['team_id'])
    contestant = Contestant(name, occupation, fave_phrase, team, id)
    contestant_repository.update(contestant)
    return redirect("/contestants")

#Delete
@contestants_blueprint.route("/contestants/<id>/delete", methods = ["POST"])
def delete_contestant(id):
    contestant_repository.delete(id)
    return redirect("/contestants")

