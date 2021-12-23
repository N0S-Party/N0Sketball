
import json
from pathlib import Path
import requests

from yahoo_oauth import OAuth2

class OAuth2Handler:

    def __init__(self, client_id=None, client_secret=None, login_file="login.json", token_file="token.json"):

        self._client_id = client_id
        self._client_secret = client_secret
        self._token = None

        if self._client_id and self._client_secret:
            self._client_id = str(self._client_id)
            self._client_secret = str(self._client_secret)
        else:
            if self._client_id or self._client_secret:
                raise RuntimeException()
            else:
                login_file_path = open(f"{login_file}")
                data = json.load(login_file_path)
                if 'CLIENT_ID' in data:
                    self._client_id = data["CLIENT_ID"]
                else:
                    raise RuntimeException()
                if 'CLIENT_SECRET' in data:
                    self._client_secret = data["CLIENT_SECRET"]
                else:
                    raise RuntimeException()

        auth = {"consumer_key": self._client_id, "consumer_secret": self._client_secret}

        token_file_path = Path(f"{token_file}")
        if token_file_path.is_file():
            with open(token_file_path) as token:
                auth = json.load(token)
        else:
            with open(token_file_path, "w") as token:
                json.dump(auth, token)

        if "access_token" in auth.keys():
            self._token = auth["access_token"]

        self.session = OAuth2(None, None, from_file=token_file_path, browser_callback=True)
        if not self.session.token_is_valid():
            self.session.refresh_access_token()
