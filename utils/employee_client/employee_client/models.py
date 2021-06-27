from attr import attrs, attrib


# TODO:add default values for some DTOs

@attrs
class EmployeeRequestDTO:
    name = attrib(type=str)
    salary = attrib(converter=str)
    age = attrib(converter=str)


@attrs
class EmployeeResponseDTO:
    name = attrib(type=str)
    salary = attrib(converter=str)
    age = attrib(converter=str)
    id = attrib(type=int)


@attrs
class EmployeeResponseDTO:
    id = attrib(type=int)
    employee_name = attrib(type=str)
    employee_salary = attrib(type=int)
    employee_age = attrib(type=int)
    profile_image = attrib(type=str)
