1. How many tests to write? 
Test must be written for the following arguments:
    1. Bad arguments
    2. Special arguments
    3. Normal arguments

Note: Not all functions have bad or special arguments. 

    1. Bad arguments:
        Are values that raise an exception, not a value.

    2. Special arguments: 
        a. Boundary values
            Represents the arguments that produce values where the return value is "close" or neighbouring a bad or special value. 
            Boundaries are what separate bad and special values from normal values.
            For example: if we know a function should return >1, the argument that returns 2 is a boundary value. 
            This tests the function works properly with values close to those that produce the unwanted values.

        b. Specific arguments values where the function uses a special logic.
            These are the arguments that trigger the specific cases in a function and not the general logic.
            For example, arguments in an "if" statement that makes sure certain values are treated different
            are special arguments. 

    3. Normal arguments:
        Those that return the expected values of the function. 
        It is recommended to test 3 normal values.

2. Test-driven development

    In escence, write the tests first, to fulfill the requirements of a function. 
    That will make us think about the bad, special, and normal arguments. 
    Once done, write the function and make sure they pass. 
    This ensures tests are written and makes writing the function a lot easier. 


3. Structure and organization:

Tree should look something like this. 
Packages ('functions') and tests folder at the same level.
Then for every sublevel in a package dir, a dir should be made. 
__init__.py in tests is optional. In general, it helps python to find the packages.
src
    ├── Notes.txt
    ├── README.md
    |
    ├── functions
    │   ├── __init__.py
    │   ├── convert_to_int.py
    │   └── sumar.py
    ├── setup.py
    |
    └── tests
        ├── __init__.py
        └──functions
            ├── test_covert_to_int.py
            └── test_sumar.py

Then we can use Test classes to keep test files organised.

4. How to run tests effectively
    1. To run all tests:
        cd into tests dir and run pytest
    2. Run until failure
        `pytest -x`. Runs all and stops when 1 test fails.
    3. Specific module:
        `pytest path to module`
    4. Specific class:
        a. using Node IDs:
            i. `pytest -k <path/to/module>::<test class name>`
            ii `pytest -k <path/to/module>:<:<test class name>::unit test name>`
        
        b. Keywords and logical operators
        `pytest -k "<Unique test class/unit test name>"`
        `pytest -k "<test 1 name> and not <test two name>"`
    

5. Expected failures and conditional skipping:
    1. General expected failure:
        Uses the `@pytest.mark.xfail` decorator before the test or class
        Returns an x in the output, but raises no errors.
        Optionally takes a reason argument, see below. 

    2. Conditional failures:
        Uses decorator `@pytest.mark.skipif(boolean expression, reason = 'Reason to skip')`
        Skips if its met. ex: 
        for version missmatch @pytest.mark.skipif(sys.version_info != (3,0), reason = "Requires python 3.0")

        Output shows the test was skipped.
        To show the reason in the report: `pytest -r` and add arguments (s for skipping, x for xfail.)
        ex: `pytest -rs` shows the reason for skipping
        
    3. All flags in `pytest -h`:
        - (s)kip
        - (x)failed
        - (X)Passed

6. Continuous integration (CI) and coverage
    For this we use Travis CI and codecov, these show us if the codebase is stable and how much of it is tested.
    Travis CI is used to filter any failures after a change was made to the codebase. Before a commit is implemented, it builds the app,
    runs the tests, and only allows to continue if it passes. Having this badge on GitHub points to a stable codebase.

    codecov shows how much of the codebase is tested. It gives the number of lines that ran over testing/total number of lines in the app as a percetange. This badge shows how robust the code is and is updated on every build.

    This is all implemented through a configuration file.: .travis.yml
    Once that is done, make sure to install travis and codecov from github marketplace. 

    

