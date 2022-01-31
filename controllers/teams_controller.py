from flask import Flask, redirect, render_template, request
from flask import Blueprint
from repositories.contestant_repository import *
from repositories.team_repository import *
from models.team import Team

teams_blueprint = Blueprint("teams", __name__)

#Index
@teams_blueprint.route("/teams")
def team():
    teams = team_repository.select_all()
    return render_template("teams/index.html", teams=teams)

# team info displaying members
# @teams_blueprint.route("/teams/<id>")
# def show(id):
#     team = team_repository.select(id)
#     contestants = team_repository.show_members(team)
#     return render_template("/teams/show.html", team=team, contestants=contestants)

#Create
@teams_blueprint.route("/teams/new", methods =["GET"])
def new_team_form():
    return render_template("/teams/new.html")

@teams_blueprint.route("/teams", methods = ["POST"])
def new_team():
    name = request.form['name']
    points = request.form['points']
    team = Team(name, points)
    team_repository.save(team)
    return redirect("/teams")


#Read
#Edit
#Update
#Delete


# @locations_blueprint.route("/locations/<id>")
# def show(id):
#     location = location_repository.select(id)
#     users = location_repository.users(location)
#     return render_template("locations/show.html", location=location, users=users)
