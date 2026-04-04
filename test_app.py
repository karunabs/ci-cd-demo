from app import add

def test_add():
  assert add(2,3) == 5

def test_add_fail():
  assert add(3,3) == 6

def test_add_with_fixtures(numbers):
  a, b = numbers
  assert add(a, b) == 5

## This test is an example with class implementation
def test_add_func_calculator(calculator):
  result = calculator.add_func(2,3)
  assert result == 5

def test_query_db(db_connection):
  ## here db connection is valid for the entire session
  assert db_connection == "Database Connection"

def test_create_data_one(create_data):
  create_data["name"].append("test1")
  assert create_data["name"] == ["test1"]

def test_create_data_two(create_data):
  create_data["name"].append("test2")
  assert create_data["name"] == ["test2"]

def test_ssh_session(ssh_session):
  assert ssh_session == "SSH Connection"
