from app import add

def test_add():
  assert add(2,3) == 5

def test_add_fail():
  assert add(3,3) == 6

def test_add_with_fixtures(numbers):
  a, b = numbers
  assert add(a, b) == 5
