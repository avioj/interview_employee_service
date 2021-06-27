from setuptools import setup

setup(name='employee_client',
      version='0.1',
      description='robot service client',
      author='Vladimir Tsyuman',
      author_email='vladimir.tsyuman@gmail.com',
      install_requires=['requests', 'furl', 'pytest', 'allure-pytest'],
      packages=['employee_client'],
      entry_points={"pytest11": ["employee_client = employee_client.pytest_plugin"]},
      # custom PyPI classifier for pytest plugins
      classifiers=["Framework :: Pytest"],
      )
