import random

import pytest
from assertpy import assert_that
from employee_client.models import EmployeeRequestDTO


@pytest.fixture()
def fake_employee(faker):
    return EmployeeRequestDTO(faker.first_name(), random.randint(1, 1000), random.randint(1, 100))


def test_employee_creation_1(employee_client, fake_employee):
    created = employee_client.post(fake_employee)
    assert_that(created).has_name(fake_employee.name) \
        .has_age(fake_employee.age) \
        .has_salary(fake_employee.salary)
    assert_that(created.id).is_not_none()


def test_employee_creation_2(employee_client, fake_employee):
    created = employee_client.post(fake_employee)
    response = employee_client.get(created.id)
    assert_that(response).has_id(created.id) \
        .has_salary(created.salary) \
        .has_age(created.age) \
        .has_name(created.name)
    assert_that(response.profile_image).is_not_none()


def test_employee_creation_3(employee_client, fake_employee):
    created = employee_client.post(fake_employee)
    employees = employee_client.get_all()
    assert_that(employees).does_not_contain_duplicates()
    assert_that(next(map(lambda x: x.id == created.id, employees))) \
        .has_salary(created.salary) \
        .has_age(created.age) \
        .has_name(created.name)
