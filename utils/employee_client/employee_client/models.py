from attr import attrs, attrib


@attrs
class EmployeeDTO:
    name = attrib(type=str)
    salary = attrib(converter=str)
    age = attrib(converter=str)


@attrs
class EmployeeResponseDTO:
    id = attrib(type=int)
    employee_name = attrib(type=str)
    employee_salary = attrib(320800)
    employee_age = attrib(type=int)
    profile_image = attrib(type=str)
