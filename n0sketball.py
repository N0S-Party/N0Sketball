
from src.utils.yahoo.leagueHandler import LeagueHandler
from src.utils.yahoo.teamHandler import TeamHandler
from src.utils.yahoo.playerHandler import PlayerHandler

if __name__ == "__main__":
    lh = LeagueHandler()
    # th = TeamHandler(lh, "410.l.28654.t.5")
    ph = PlayerHandler(lh, "410.p.4724")
