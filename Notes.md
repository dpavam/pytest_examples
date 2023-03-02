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

    Alternatively, because Travis CI can be problematic, GitHub Actions is recommended.
    For this we will follow this (tutorial)[https://docs.github.com/es/actions/quickstart]

7. More advanced tests: Beyond assert

    Sometimes we will need to write tests that require a setup (e.g.:an existing file)
    For this we use pytests' fixtures. 

    They require creating an independent function, create the fixture, yield its value, and then a teardown (this is clearing the environment)
    There are two ways to work with these:

    1. Manually:
    
    `
    #Fixture decorator
    @pytest.fixture
    #define the fixture
    def a_fixture():
    #setup the value
    array = np.array([[0,2],[1,4]])
    #yield its contents
    yield array
    #teardown after being called
    os.remove(array)`

    2. tmpdir to automatically teardown for files.
    `@pytest.fixture
    def a_fixture(tmpdir):
    file= tmpdir.join("file.txt")
    open(file, "w").close()
    yield file`


8. Mocking
    Used to tailor test that skip dependencies.
    Packages: 1. pytest-mock (pip install pytest-mock)
              2. unittest.mock (standard python)

    This is highly specific to each test, so this will be skipped in this tutorial. 

9. Testing models
    Testing ML models can be complex, as the results are difficult. 
    Some approaches to test include:
        1. Sanity checks: Check the model returns a slope > 0
        2. Test with known output. Test your modeling functions using special test data for which you know the output. This checks if they are performing as expected.

10. Testing plots

    This is suggested for matplotlib figures using a package called pytest-mpl (`pip install pytest-mpl`)
    It prodouces a baseline visualisation in PNG with ideal data.
    Then, a test can be written to produce a PNG plot, and compare them.
    The tests have the marker: `@pytest.mark.mpl_image_compare` and return the plot. Not an assert statement.
    The baseline is created running the command `pytest -k "<TestforPlot>" --mpl-generate-path visualisation/baseline`. This is accounting for having a visualisation/baseline dir within tests.
    Next, the PNG is created on the baseline dir, and then to actuall test we run: `pytest -k "<TestforPlot>" --mpl`

    Note the PNG images will be saved on the basline folder, where you can visually see the differences. Black is identical, white is difference. 


All code for basing this tutorial is (here)[https://github.com/gutfeeling/univariate-linear-regression]



