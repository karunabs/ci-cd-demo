import pytest

@pytest.fixture()
def numbers():
  
  ## this fixture provides test data. 
  ## It runs before each test, which uses it. 
  
  return 2,3

@pyteest.fixture():
def calculator():
  class Calculator:
    def add_func(self, a, b):
      return a + b

  return Calculator()


