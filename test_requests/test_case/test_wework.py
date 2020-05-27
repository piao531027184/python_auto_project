from test_requests.api.base_api import BaseApi
from test_requests.api.wework import WeWork
from jsonpath import jsonpath


class Test_WeWork():
    def test_get_token(self):
        secret = "heLiPlmyblHRiKAgGWZky4-KdWqu1V22FeoFex8RfM0"
        WeWork().get_token(secret)
