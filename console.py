from models.contestant import Contestant
from models.team import Team

import repositories.contestant_repository as contestant_repository
import repositories.team_repository as team_repository

team_01 = Team("Dead Hospitable", 389)
team_repository.save(team_01)


contestant_01 = Contestant("Cilla Black", "Game Show Host", "It takes two to tango", team_01)
contestant_repository.save(contestant_01)
contestant_02 = Contestant("Brucie", "Game Show Host", "In for a penny, in for a pound", team_01)
contestant_repository.save(contestant_02)