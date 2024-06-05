# :mag: Pytest Quest :flashlight:

### *Exercise to practice Pytest with fixtures, markers and parametrizes*

### Pre-requirements:

* **Python version: `3.10`**


### Virtual Environment:

* **_To create:_**

`python3 -m venv .venv`

* **_Initialization:_** 

`source .venv/bin/activate`

* **_Installing dependencies:_**

`python3 -m pip install -r dev-requirements.txt`

### **Exercises:**

1. **Creating simple fixture:**

    * Create the file `tests/conftest.py`. Then, create in this file the fixture `custom_fixture`, with the scope of module (or broader, such as session), which returns a Python list with the numbers from 1 to 10, including 1 and 10.

2. **Creating a marker:**

    * Create a file `tests/marker_test.py`. Then, create in this file the test function `test_dependency_mark`, whose test result should always pass. Mark the test with the dependency marker.

3. **Creating parametrized tests:**

    * In the previously created file `tests/parametrized_test.py`, create a parameterized test function called `test_converter` to test the function `src.hex_converter.hexadecimal_to_decimal`.

    * The test function should receive two parameters, the first being the hexadecimal number as a string and the second being the equivalent decimal integer.


4. **Using built in fixtures - _monkeypatch_:**

    * In the previously created file `tests/built_in_fixtures_test.py`, create a test function called `test_monkeypatch`. This function should use the monkeypatch fixture to validate if the call to `src.hex_converter.main` returns 10 when the user inputs the string `"a"`.

5. **Using built in fixtures - _capsys_:**

    * In the previously created file `tests/built_in_fixtures_test.py`, create a test function named `test_capsys`. This function should use the capsys fixture to validate whether the function` src.hex_converter.print_hexadecimal_to_decimal` prints `"10\n"` to the standard output and an empty string to the standard error output when called with the string `"a"`.

6. **Using built in fixtures - *tmp_path*:**

    * In the previously created file `tests/built_in_fixtures_test.py`, create a test function called `test_tmp_path`. This function should use the tmp_path fixture to create a temporary file named "output.txt" within a temporary directory.

    * Then, this directory should be passed as the second parameter to the function `write_hexadecimal_to_decimal`, with the first parameter being the string `"a"`.

    * Finally, the test should verify if the content of the file `"output.txt"` is equal to the string `"10"`.

    _Hint: Use the method pathlib.Path().read_text()._