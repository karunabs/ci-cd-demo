import pytest

@pytest.fixture()
def numbers():
  
  ## this fixture provides test data. 
  ## It runs before each test, which uses it. 
  
  return 2,3

@pytest.fixture()
def calculator():
  class Calculator:
    def add_func(self, a, b):
      return a + b

  return Calculator()

## This demonstrates db_connection fixture is created for the entire session
@pytest.fixture(scope="session")
def db_connection():
  ## setup a db connection
  connection = "Database Connection"
  yield connection
  ## Teardown connection

@pytest.fixture(scope="function")
def create_data():
  ## creating fresh data for the tests
  data = {"name": []}
  yield data
  ## cleaning up after test runs

@pytest.fixture(scope="module")
def ssh_session():
  ## creates a ssh connection to a host
  session = "SSH Session"
  yield session
  ## close ssh session
  
