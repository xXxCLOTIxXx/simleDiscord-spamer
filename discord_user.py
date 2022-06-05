import requests
from time import time
from json import dumps


class Client():
    def __init__(self):
        self.api = "https://discord.com/api/v9"
        self.headers = {
            "Content-Type": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36"
        }

    # authorization
    def login(self, email: str, password: str):
        data = dumps({
            "login": email,
            "password": password,
            "undelete": False,
            "captcha_key": None,
            "login_source": None,
            "gift_code_sku_id": None
        })
        response = requests.post(
            f"{self.api}/auth/login",
            headers=self.headers,
            data=data).json()
        try:
            self.email = email
            self.password = password
            self.token = response["token"]
            self.headers["Authorization"] = self.token
        except BaseException:
            exit(response)
        return response

    def my_channels(self):
        return requests.get(
            f"{self.api}/users/@me/channels",
            headers=self.headers).json()

    def send_message(self, content: str = None, channel_id: int = None):
        data = dumps({"content": content})
        return requests.post(
            f"{self.api}/channels/{channel_id}/messages",
            headers=self.headers,
            data=data).json()