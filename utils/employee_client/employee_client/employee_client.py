from attr import asdict
from furl import furl
from requests import Session
from .helpers import check_response
from .models import EmployeeDTO, EmployeeResponseDTO


class EmployeeClient:
    def __init__(self, host):
        self.host = host
        self.session = Session()
        self.session.hooks['response'] = [check_response]

    def post(self, employee: EmployeeDTO):
        return self.session.post(furl(host=self.host, path="/create").url, json=asdict(employee)).json()['data']

    def get_all(self):
        return [EmployeeResponseDTO(**args) for args in
                self.session.get(furl(host=self.host, path="/api/v1/employees").url).json()["data"]]

    def get(self, _id):
        return EmployeeResponseDTO(**self.session.get(furl(host=self.host,
                                                           path=f"/api/v1//employee/{_id}").url).json()['data'])

    def put(self, _id, employee):
        return self.session.put(furl(host=self.host, path=f"/api/v1/update/{_id}").url, json=asdict(employee))

    def delete(self, _id):
        return self.session.delete(furl(host=self.host, path=f"/api/v1/update/{_id}").url).json()
