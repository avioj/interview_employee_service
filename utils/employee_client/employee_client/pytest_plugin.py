import pytest


@pytest.hookimpl
def pytest_addoption(parser):
    parser.addoption("--employee_host", action="store",
                     default='http://dummy.restapiexample.com')


@pytest.fixture()
def employee_client(request):
    request.config.getoption("--employee_host")
