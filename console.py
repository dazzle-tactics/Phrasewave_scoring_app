from models.contestant import Contestant
from models.team import Team
import pdb

import repositories.contestant_repository as contestant_repository
import repositories.team_repository as team_repository

contestant_repository.delete_all()
team_repository.delete_all()

team_01 = Team("Dead Hospitable", 389)
team_repository.save(team_01)
team_02 = Team("Lolcats", 79078)
team_repository.save(team_02)

contestant_01 = Contestant("Cilla Black", "Game Show Host", "It takes two to tango", team_01)
contestant_repository.save(contestant_01)
contestant_02 = Contestant("Brucie", "Game Show Host", "In for a penny, in for a pound", team_01)
contestant_repository.save(contestant_02)
contestant_03 = Contestant("Happy Cat", "Lolcat", "I can has cheezburger?", team_02)
contestant_repository.save(contestant_03)
contestant_04 = Contestant("Hello Kitty", "Cutesy Cat", "The early bird gets the worm", team_02)
contestant_repository.save(contestant_04)


# contestant_repository.delete(1)
# team_repository.delete(1)

# team_02.points += 6786
# team_repository.update(team_02)
# contestant_04.team = 9
# contestant_repository.update(contestant_04)


pdb.set_trace()



