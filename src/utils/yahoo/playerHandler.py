
from src import _YAHOO
import requests

_PLAYER = f"{_YAHOO}/player"

class PlayerStatManager:
    pass

class PlayerHandler:

    def __init__(self, league, playerKey):
        self.league = league
        self.playerKey = playerKey
        self.playerURI = f"{_PLAYER}/{self.playerKey}"

        self._setup()

    def _setup(self):
        playerInfo = self.get()['fantasy_content']['player'][0]
        self.playerID = playerInfo[1]
        self.playerName = playerInfo[2]['name']['full']
        self.playerStatus = playerInfo[3]['status']
        self.playerNBATeamKey = playerInfo[6]['editorial_team_key']
        self.playerNBATeamName = playerInfo[8]['editorial_team_abbr']
        playerPicture = teamInfo[11]['headshot']
        self.playerPicture = ImageHandler(playerPicture['size'], playerPicture['url'])
        self.playerDroppability = playerInfo[12]['is_undroppable']

    def get(self, endpoint=''):
        if endpoint is None:
            return self.league.session.session.get(f"{self.playerURI}/?format=json").json()
        else:
            return self.league.session.session.get(f"{self.playerURI}/{endpoint}/?format=json").json()
