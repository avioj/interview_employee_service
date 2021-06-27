import pytest
from .employee_client import EmployeeClient


@pytest.hookimpl
def pytest_addoption(parser):
    parser.addoption("--employee_host", action="store",
                     default='http://dummy.restapiexample.com')


@pytest.fixture()
def employee_client(request):
    return EmployeeClient(request.config.getoption("--employee_host"))
