from bdb import set_trace
from cProfile import run
from db.run_sql import run_sql

from models.contestant import Contestant
from models.team import Team
import repositories.team_repository as team_repository
import pdb

#Create
def save(contestant):
    sql = "INSERT INTO contestants (name, occupation, fave_phrase, team_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [contestant.name, contestant.occupation, contestant.fave_phrase, contestant.team.id]
    results = run_sql(sql,values)
    
    id = results[0]['id']
    contestant.id = id
    return contestant

#Read
def select_all():
    contestants = []

    sql = "SELECT * FROM contestants"
    results = run_sql(sql)

    for row in results:
        team = team_repository.select(row['team_id'])
        contestant = Contestant(row['name'], row['occupation'], row['fave_phrase'], team, row['id'])
        contestants.append(contestant)
    return contestants

def select(id):
    contestant = None
    
    sql = "SELECT * FROM contestants where id = %s"
    values = [id]
    
    result = run_sql(sql, values)[0]
    if result is not None:
        team = team_repository.select(result['team_id'])
        contestant = Contestant(result['name'], result['occupation'], result['fave_phrase'], team, result['id'])
    return contestant

#Update
def update(contestant):
    sql = "UPDATE contestants SET (name, occupation, fave_phrase, team_id) = (%s, %s, %s, %s) WHERE id = (%s)"
    values = [contestant.name, contestant.occupation, contestant.fave_phrase, contestant.team.id, contestant.id]
    run_sql(sql, values)

#Delete
def delete(id):
    sql = "DELETE FROM contestants WHERE id = %s"
    values = [id]
    run_sql(sql, values)

#Delete all
def delete_all():
    sql = "DELETE  FROM contestants"
    run_sql(sql)