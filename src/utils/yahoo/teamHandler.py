
from src import _YAHOO
import requests
import json

from .imageHandler import ImageHandler
from .leagueHandler import LeagueHandler

_TEAM = f"{_YAHOO}/team"

class TeamMatchupManager:
    pass

class TeamStatManager:
    pass

class TeamHandler:

    def __init__(self, league, teamKey):
        self.league = league
        self.teamKey = teamKey
        self.teamURI = f"{_TEAM}/{self.teamKey}"

        self._setup()

    def _setup(self):
        teamInfo = self.get('roster')['fantasy_content']['team'][0]
        self.teamID = teamInfo[1]
        self.teamName = teamInfo[2]
        teamLogo = teamInfo[5]['team_logos']['team_logo']
        self.teamLogo = ImageHandler(teamLogo['size'], teamLogo['url'])
        self.teamWWPrio = teamInfo[7]
        self.teamMoves = teamInfo[9]
        self.teamTrades = teamInfo[10]
        self.teamManager = ManagerHandler(teamInfo[19]['managers'][0]['manager']['manager_id'])
        self.teamRoster = [PlayerHandler(teamInfo[20]['roster']['0']['players'][player]['player'][0][0]['playerKey']) for player in teamInfo[20]['roster']['0']['players'].keys()]


    def get(self, endpoint=''):
        if endpoint is None:
            return self.league.session.session.get(f"{self.teamURI}/?format=json").json()
        else:
            return self.league.session.session.get(f"{self.teamURI}/{endpoint}/?format=json").json()
