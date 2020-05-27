import requests

from test_requests.api.base_api import BaseApi


class WeWork(BaseApi):
    # 获取token
    corpid = 'wwd6da61649bd66fea'

    def get_token(self, secret):
        data = {
            "method": 'get',
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            "params": {
                "corpid": self.corpid,
                "corpsecret": secret
            }
        }
        # **的形式用来解包，比如将data中的"url":'https://qyapi.weixin.qq.com/cgi-bin/gettoken'，转换为url=''
        return self.send_api(data)['access_token']
