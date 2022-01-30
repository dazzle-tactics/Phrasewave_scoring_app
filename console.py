from models.contestant import Contestant
from models.team import Team
import pdb

import repositories.contestant_repository as contestant_repository
import repositories.team_repository as team_repository

team_01 = Team("Dead Hospitable", 389)
team_repository.save(team_01)
team_02 = Team("Lolcats", 79078)
team_repository.save(team_02)

# contestant_01 = Contestant("Cilla Black", "Game Show Host", "It takes two to tango", team_01)
# contestant_repository.save(contestant_01)
# contestant_02 = Contestant("Brucie", "Game Show Host", "In for a penny, in for a pound", team_01)
# contestant_repository.save(contestant_02)
# contestant_03 = Contestant("Garfield", "Sarky Cat", "He who dares, wins", team_02)
# contestant_repository.save(contestant_03)
# contestant_04 = Contestant("Hello Kitty", "Cutesy Cat", "The early bird gets the worm", team_02)
# contestant_repository.save(contestant_04)



pdb.set_trace()