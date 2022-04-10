
from src import _YAHOO
import requests

_TRANSACTION = f"{_YAHOO}/transaction"

class transactionHandler(LeagueHandler):

    def __init__(self, transactionKey):
        self.transactionKey = transactionKey
        self.transactionURI = f"{_TEAM}/{self.playerKey}"

        self._setup()

    def _setup(self):
        self.getTransaction()

    def get(self, endpoint=''):
        if endpoint is None:
            return self.session.session.get(f"{self.transactionURI}/?format=json").json()
        else:
            return self.session.session.get(f"{self.transactionURI}/{endpoint}/?format=json").json()

    def getTransaction(self):
        transaction = self.get()
        return transaction['transaction'][0]
