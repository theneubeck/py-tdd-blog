# A structure for solving the TDD blog

This is a python template that can be used to solve the tdd-blog workshop. Instructions: https://github.com/theneubeck/tdd-blog-instructions

## Rules

* You can only run your code with tests
* Take turns. One person writes a test - The other writes the code.
* _Always_ write the test **first**

This repo uses python 3.8.12

## Commands

```bash

# install everything
poetry install

# to run tests
poetry run pytest
# to run a specific test
poetry run pytest -k test_request_example
# or
poetry run pytest tests/test_app.py::test_request_example
```

Some useful links:

* https://docs.pytest.org/en/7.2.x/
* https://docs.pytest.org/en/6.2.x/fixture.html
* https://flask.palletsprojects.com/en/2.2.x/testing/
* https://flask.palletsprojects.com/en/2.2.x/quickstart/
* https://flask.palletsprojects.com/en/2.2.x/blueprints/
* https://stackoverflow.com/questions/36456920/is-there-a-way-to-specify-which-pytest-tests-to-run-from-a-file