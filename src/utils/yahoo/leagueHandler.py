
import requests

from src import _YAHOO
from .oAuthHandler import OAuth2Handler

_LEAGUE = f"{_YAHOO}/league"

class LeagueHandler(OAuth2Handler):

    def __init__(self, leagueKey = "28654"):
        super().__init__()
        self.gameKey = self.session.session.get(f"{_YAHOO}/game/nba/?format=json").json()["fantasy_content"]["game"][0]["game_key"]
        self.leagueKey = f"{self.gameKey}.l.{leagueKey}"
        self.leagueUri = f"{_LEAGUE}/{self.leagueKey}"
        self.teams = self.get_teams()

    def get(self, endpoint):
        return self.session.session.get(f"{self.leagueUri}/{endpoint}/?format=json")

    def get_teams(self):
        standings = self.get('standings').json()
        print(standings)
