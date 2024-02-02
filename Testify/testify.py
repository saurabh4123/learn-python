#Testify is a Python module that replaces the unittest module and nose. It is modeled after unittest, and it fully supports existing unittest classes.

# Testify includes functionalities that go beyond unittest:
    # Teardown fixture methods and Class-level setup are run only once for an entire class of test methods.
    # A decorator-based approach to fixture methods allows for features like lazy attribute evaluation and test context managers.
    # Test discovery has been improved. Testify can search across packages for test cases (similar to nose).
    # Support for finding and running test suites organized by modules, classes, or test methods.
    # The output of the test runner is attractive (color).
    # Extensible plugin system for providing new reporting functions.
    # Turtle (for mocking), code coverage integration, profiling, and various everyday assertion helpers for faster debugging are among the other helpful testing facilities included.
    # More naming standards in Python.


#example test case
from testify import *

class AdditionTestCase(TestCase):

    @class_setup
    def init_the_variable(self):
        self.variable = 0

    @setup
    def increment_the_variable(self):
        self.variable += 1

    def test_the_variable(self):
        assert_equal(self.variable, 1)

    @suite('disabled', reason='ticket #123, not equal to 2 places')
    def test_broken(self):
        # raises 'AssertionError: 1 !~= 1.01'
        assert_almost_equal(1, 1.01, threshold=2)

    @teardown
    def decrement_the_variable(self):
        self.variable -= 1

    @class_teardown
    def get_rid_of_the_variable(self):
        self.variable = None

if __name__ == "__main__":
    run()

# Testify provides the following fixtures for your enjoyment:

# @setup: Run before each individual test method on the TestCase(that is, all methods that begin with 'test').

# @teardown: Like setup, but run after each test completes (regardless of success or failure).

# @class_setup: Run before a TestCase begins executing its tests. Note that this not a class method; you still have access to the same TestCase instance as your tests.

# @class_teardown: Like class_setup, but run after all tests complete (regardless of success or failure).

# @setup_teardown: A context manager for individual tests, where test execution occurs during the yield. For example:

@setup_teardown
def mock_something(self):
    with mock.patch('foo') as foo_mock:
        self.foo_mock = foo_mock
        yield
    # this is where you would do teardown things
# @class_setup_teardown: Like setup_teardown, but all of the TestCase's methods are run when this yields.

# @let: This declares a lazily-evaluated attribute of the TestCase. When accessed, this attribute will be computed and cached for the life of the test (including setup and teardown). For example:

@let
def expensive_attribute(self):
    pass
#   return expensive_function_call()

def test_something(self):
  assert self.expensive_attribute

def test_something_else(self):
  # no expensive call
  assert True



# Order of Execution of test cases
# In pseudo code, Testify follows this schedule when running your tests:
#    Run all 'class_setup' methods
#    Enter all 'class_setup_teardown' context managers
#    For each method beginning with 'test':
#        Run all 'setup' methods
#        Enter all 'setup_teardown' context managers
#            Run the method and record failure or success
#        Exit all 'setup_teardown' context managers
#        Run all 'teardown' methods
#    Exit all 'class_setup_teardown' context managers
#    Run all 'class_teardown' methods