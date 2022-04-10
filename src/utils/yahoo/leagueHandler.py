
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

        self._setup()

    def _setup(self):
        """ LeagueHandler information """
        self.leagueInfo = self.getLeague()

    def get(self, endpoint=''):
        if endpoint is None:
            return self.session.session.get(f"{self.leagueUri}/?format=json").json()
        else:
            return self.session.session.get(f"{self.leagueUri}/{endpoint}/?format=json").json()

    def getLeague(self):
        """
        League Specific Content
        League data is specifically under the 'league' key

        API Output:
        {
            'xml:lang': 'en-US',
            'yahoo:uri': '/fantasy/v2/league/410.l.28654/',
            'league': [                                     <---- RETURN OUTPUT
                {
                    'league_key': '410.l.28654',
                    'league_id': '28654',
                    'name': 'N0sketball 2.0',
                    'url': 'https://basketball.fantasysports.yahoo.com/nba/28654',
                    'logo_url': False,
                    'draft_status': 'postdraft',
                    'num_teams': 12,
                    'edit_key': '2022-01-04',
                    'weekly_deadline': 'intraday',
                    'league_update_timestamp': '1641284000',
                    'scoring_type': 'headpoint',
                    'league_type': 'private',
                    'renew': '402_155452',
                    'renewed': '',
                    'iris_group_chat_id': '',
                    'allow_add_to_dl_extra_pos': 1,
                    'is_pro_league': '0',
                    'is_cash_league': '0',
                    'current_week': 12,
                    'start_week': '1',
                    'start_date': '2021-10-19',
                    'end_week': '23',
                    'end_date': '2022-04-03',
                    'game_code': 'nba',
                    'season': '2021'
                }
            ],
            'time': '17.541170120239ms',
            'copyright': 'Data provided by Yahoo! and STATS, LLC',
            'refresh_rate': '60'
        }

        """
        league = self.get()
        return league['fantasy_content']['league'][0]
