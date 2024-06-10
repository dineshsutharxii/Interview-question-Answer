# how to run a specific method before each test method in a class using fixture
import pytest


class Test:
    @pytest.fixture(autouse=True)  # fixtures default scope is always 'function'
    def FixtureMethod(self):
        print("Fixture method is called")

    def test_method1(self):
        print("Method 1 is called")

    def test_method2(self):
        print("Method 2 is called")


# how to run a specific method before all test method in a class using fixture and not before each testcases

class Test1:
    @pytest.fixture(scope='class', autouse=True)
    def FixtureMethod(self):
        print("Class Fixture method is called")

    def test_method3(self):
        print("Method 3 is called")

    def test_method4(self):
        print("Method 4 is called")


# how to run a specific method before all test method before all classes using fixture
# check conftest.py the function "fixtureForClass" with @pytest.fixture(scope='session', autouse=True) is called once before all class
class Test2:
    def test_method5(self):
        print("Method 5 is called")

    def test_method6(self):
        print("Method 6 is called")


# How to execute a fixture automatically on running any file
class Test3:
    @pytest.fixture(autouse=True)  # fixtures default scope is always 'function'
    def FixtureMethod(self):
        print("Fixture method is called")

    def test_method1(self):
        print("Method 1 is called")

    def test_method2(self):
        print("Method 2 is called")


# How to call fixture from a test method
class Test4:
    @pytest.fixture()
    def FixtureMethod(self):
        print("Fixture method is called")

    def test_method1(self, FixtureMethod):
        print("Method 1 is called")

    def test_method2(self):
        print("Method 2 is called")


# how to run same test method for multiple set of test data
class Test5:
    @pytest.mark.parametrize('values', ["Hello", 'from', 'pytest'])
    def test_parameterized(self, values):
        print("Values are called -- {}".format(values))
