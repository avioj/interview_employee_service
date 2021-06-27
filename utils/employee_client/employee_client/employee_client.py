from allure import step
from attr import asdict
from furl import furl
from requests import Session
from .helpers import check_response
from .models import EmployeeRequestDTO, EmployeeResponseDTO


class EmployeeClient:
    def __init__(self, host):
        self.host = host
        self.session = Session()
        self.session.hooks['response'] = [check_response]

    @step("Create an employee")
    def post(self, employee: EmployeeRequestDTO):
        return EmployeeResponseDTO(**self.session.post(furl(self.host, path="/create").url).json()['data'])

    @step("Get list of  all existing employees")
    def get_all(self):
        return [EmployeeResponseDTO(**kw) for kw
                in self.session.get(furl(self.host, path="/api/v1/employees").url).json()["data"]]

    @step("Get employee by id {1}")
    def get(self, _id):
        return EmployeeResponseDTO(
            **self.session.get(furl(self.host, path=f"/api/v1//employee/{_id}").url).json()['data'])

    @step("Update employee with id {1}")
    def put(self, _id, employee):
        return self.session.put(furl(self.host, path=f"/api/v1/update/{_id}").url, json=asdict(employee))

    @step("Delete employee with id {1}")
    def delete(self, _id):
        return self.session.delete(furl(self.host, path=f"/api/v1/update/{_id}").url).json()
