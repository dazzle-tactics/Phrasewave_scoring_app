from cProfile import run
from db.run_sql import run_sql

from models.contestant import Contestant
from models.team import Team

#Create
def save(team):
    sql = "INSERT INTO teams (name, points) VALUES (%s, %s) RETURNING *"
    values = [team.name, team.points]
    results = run_sql(sql,values)
    
    id = results[0]['id']
    team.id = id
    return team

#Read
def select_all():
    teams = []

    sql = "SELECT * FROM teams"
    results = run_sql(sql)

    for row in results:
        team = Team(row['name'], row['points'])
        teams.append(team)
    return teams

def select(id):
    team = None
    
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        team = Team(result['name'], result['points'])
    return team

#get team members
def show_members(id):
    members = []

    sql = "SELECT * FROM contestants WHERE team_id = %s"
    values = [team_id]
    result = run_sql(sql, values)

    if result is not None:
        members = Contestant(result['name'], result['occupation'], result['fave_phrase'])
    return members


#Update
def update(team):
    sql = "UPDATE teams SET (name, points) = (%s, %s) WHERE id = %s"
    values = [team.name, team.points, team.id]
    run_sql(sql, values)

#Delete
def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)

