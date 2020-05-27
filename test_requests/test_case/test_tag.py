import json

import pytest
import yaml

from test_requests.api.base_api import BaseApi
from test_requests.api.tag import Tag
from jsonpath import jsonpath


class Test_Tag:
    tag = Tag()
    test_data = BaseApi.load('./test_requests/test_case/test_tag_data.yaml')

    @classmethod
    def setup_class(cls):
        data = cls.tag.get()
        for name in ["add demo"]:
            # 找到包含zhangsan 属性的tag节点,再通过.id查找到所属id
            tag_id = cls.tag.jsonpath(data, f'$..tag[?(@.name=="{name}")].id')
            if tag_id:
                cls.tag.delete(tag_id[0])

    def setup(self):
        pass

    @pytest.mark.parametrize("name_old,name_new", test_data)
    def test_all(self, name_old, name_new):
        # data = self.tag.get()
        # for name in [name_old, name_new]:
        #     # 找到包含zhangsan 属性的tag节点,再通过.id查找到所属id
        #     tag_id = self.tag.jsonpath(data, f'$..tag[?(@.name=="{name}")].id')
        #     if tag_id:
        #         self.tag.delete(tag_id[0])
        assert self.tag.add(name_old)['errcode'] == 0
        tag_id = self.tag.jsonpath(self.tag.get(), f'$..tag[?(@.name=="{name_old}")].id')[0]
        assert self.tag.update(tag_id, name_new)['errcode'] == 0

    def test_add(self):
        assert self.tag.add("add demo")["errcode"] == 0

    def test_get(self):
        # 格式美化
        assert self.tag.get()['errcode'] == 0
        # print(json.dumps(self.tag.get(), indent=2))

    def test_delete(self):
        print(self.tag.delete("etQKd-CgAAI70aMYm4j37aJyTo0EMRmw"))

    def test_update(self):
        print(Tag().update('etQKd-CgAAE6Zdmx89xoc_LYuIyLWwNw', 'wangwu'))
