import re
import requests

from copy import deepcopy


class SwitchAPI:
    ip = None
    session_id = None
    request_token = None
    username = None
    password = None
    headers = None
    url_base = None

    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password
        self.url_base = f"http://{self.ip}/html/json.html?method:"

    def authorize(self):
        self.session_id = self._get_session_id(self.ip)
        self._authorize_session(self.ip, self.session_id, self.username, self.password)
        self.request_token = self._get_request_token(self.ip, self.session_id)
        self.headers = {
            'Cookie': f'sessionId={self.session_id}',
            'Request-Token': self.request_token
        }

    def get(self, endpoint, *args, **kwargs):

        if self.headers is None:
            self.authorize()

        if "params" not in kwargs:
            kwargs['params'] = {}

        return requests.get(f"{self.url_base}{endpoint.replace('/', '')}", headers=self.headers, params=kwargs['params'])

    @staticmethod
    def _get_session_id(switch):
        url = f"http://{switch}"

        response = requests.request("GET", url)

        return response.cookies['sessionId']

    @staticmethod
    def _authorize_session(switch, session_id, username, password):
        url = f"http://{switch}/html/logincheck?user={username}&pass={password}&Submit=Login"

        headers = {
            'Cookie': f'sessionId={session_id}'
        }

        requests.request("GET", url, headers=headers)

    @staticmethod
    def _get_request_token(switch, session_id):
        url = f"http://{switch}/nextgen/ui/globals.js"

        headers = {
            'Cookie': f'sessionId={session_id}'
        }

        response = requests.request("GET", url, headers=headers)

        return re.search(r"var requestToken = '(.*?)';", response.text).group(1)


def get_system_info(switch: SwitchAPI):
    url = f"http://{switch.ip}/html/json.html?method:uiGetSystem"

    return requests.request("GET", url, verify=False, headers=switch.headers)
