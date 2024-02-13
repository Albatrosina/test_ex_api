# Test API Project

This repository contains a Python project for testing the Todo API. It includes a series of automated tests that validate the functionality of the Todo API endpoints.

## Project Structure

The project is structured as follows:

- `src/`: Contains the source code of the API client and models.
  - `api_client.py`: Functions to interact with the Todo API.
  - `models.py`: Data classes representing request and response payloads.
- `tests/`: Contains the pytest test cases for the API.
  - `conftest.py`: Contains the core fixtures to be used in the tests.
  - `test_api_client.py`: Module with all test cases to test the API.
- `requirements.txt`: Lists the Python dependencies for the project.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository: git clone https://github.com/Albatrosina/test_ex_api.git
2. Change directory to the newly added folder. ```cd test_ex_api```
3. Set up a virtual environment (recommended): ```python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate```
4. Install the dependencies: ```pip install -r requirements.txt```
5. Run the tests with command: ```pytest```
## Running Tests

The tests are designed to be run with pytest. You can run all tests using the following command:
```pytest```
To run a specific test file:
```pytest tests/test_api_client.py```
If you want to run the specific function within the test file follow this pattern:
```path/filename.py/::name_of_the_function```


## Licensing

The code in this project is licensed under MIT license. See the [LICENSE](LICENSE) file for details.

## Contact

For any additional questions or comments, please contact the repository owner.



