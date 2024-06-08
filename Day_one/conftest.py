import pytest

@pytest.fixture(scope='session', autouse=True)
def fixtureForClass():
    print("conftest fixtureForClass is called")