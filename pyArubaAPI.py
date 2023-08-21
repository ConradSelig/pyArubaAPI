import re
import requests


class SwitchAPI:
    ip = None
    session_id = None
    request_token = None
    username = None
    password = None

    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password

    def authorize(self):
        self.session_id = self._get_session_id(self.ip)
        self._authorize_session(self.ip, self.session_id, self.username, self.password)
        self.request_token = self._get_request_token(self.ip, self.session_id)

    def call(self, function, *args, **kwargs):
        response = function(self, *args, **kwargs)
        if "Your session has expired" in response.text:
            self.authorize()
            response = function(self, *args, **kwargs)
        return response.text

    def _get_session_id(self, switch):
        url = f"http://{switch}"

        response = requests.request("GET", url)

        return response.cookies['sessionId']

    def _authorize_session(self, switch, session_id, username, password):
        url = f"http://{switch}/html/logincheck?user={username}&pass={password}&Submit=Login"

        headers = {
            'Cookie': f'sessionId={session_id}'
        }

        requests.request("GET", url, headers=headers)

    def _get_request_token(self, switch, session_id):
        url = f"http://{switch}/nextgen/ui/globals.js"

        headers = {
            'Cookie': f'sessionId={session_id}'
        }

        response = requests.request("GET", url, headers=headers)

        return re.search(r"var requestToken = '(.*?)';", response.text).group(1)


def get_system_info(switch: SwitchAPI):
    url = f"http://{switch.ip}/html/json.html?method:uiGetSystem"

    headers = {
        'Cookie': f'sessionId={switch.session_id}',
        'Request-Token': switch.request_token
    }

    return requests.request("GET", url, headers=headers)
