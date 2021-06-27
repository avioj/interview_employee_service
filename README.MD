## Employee Testing framework

### why tests are as much "high-level"?

To be honest the chosen technic is aimed to start an integration testing process in nearest future, cos all the
contract-testing could be dynamically generated from OpenApi or similar documentation.

### Tech Stack

Talking about technology stack

[pytest](https://docs.pytest.org/en/6.2.x/contents.html)  has nice DI system included from the box and it is needless to
care about duplication in "set_up" and "tear_down" and so on.Another strong argument of that choise is ["hooks" customization]( https://docs.pytest.org/en/latest/how-to/writing_hook_functions.html)

[allure](https://github.com/allure-framework/allure-python) - hierarchy-based, tags-suporing, scalable and just good-looking 

[faker](https://faker.readthedocs.io/en/master/) - dev-friendly interface, and a huge amounts of "randomizers" for any
needs
###TODO: run example, parameters etc