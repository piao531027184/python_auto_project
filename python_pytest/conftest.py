import pytest


@pytest.fixture(scope="module")  # module，每一个.py文件调用一次，该文件内又有多个function和class
def login():
    print("打开浏览器")
    yield  # yield相当于return上一步,调用该fixture的用例每次执行到yield之前
    print("执行teardown")  # 再所有模块执行结束时执行yiled后面的结果
    print("最后关闭浏览器")


def pytest_configure(config):
    marker_list = ["SingleSuccess", "SingleFail"]
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )
