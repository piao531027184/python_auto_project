from pprint import pprint
from string import Template

import requests
import yaml
from jsonpath import jsonpath


class BaseApi:
    def send_api(self, req: dict):
        pprint(req)
        # **req :对req字典进行解包
        r = requests.request(**req)
        pprint(r.json())
        return r.json()

    @classmethod
    def jsonpath(cls, json, expr):
        return jsonpath(json, expr)

    @classmethod
    def load(cls, path):
        with open(path, 'r') as f:
            return yaml.safe_load(f)

    # 创建模板
    @classmethod
    def template(cls, path, data):
        with open(path, "r") as f:
            return yaml.load(Template(f.read()).substitute(data))
