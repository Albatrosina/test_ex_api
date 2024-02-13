import pytest
from ..src.api_client import create_task, delete_task
from ..src.models import ModifyTaskPayload


@pytest.fixture(scope='module')
def test_user_id():
    """
    Provides a consistent user ID for testing purposes.
    This user ID is used across all tests in the module that require a user context.
    """
    return 'test_kdv'


@pytest.fixture(scope='module')
def create_test_task(test_user_id):
    """
    A fixture to create a single test task with predefined content and properties.
    It uses the `test_user_id` fixture to associate the task with a test user.

    Yields:
    - The created task object for use in tests.

    After the test execution, no cleanup is done here as the `task_cleanup` fixture is responsible for that.
    """
    task_payload = ModifyTaskPayload(content='test content', user_id=test_user_id, task_id='test_task_1', is_done=True)
    response = create_task(task_payload)
    yield response.task


@pytest.fixture(scope='function')
def create_multiple_tasks(test_user_id):
    """
    A fixture to create multiple tasks for the same user.
    This is scoped to function, meaning it will run for each test function that requires it.

    Yields:
    - A list of created task objects for use in tests.
    """
    tasks = []
    for i in range(2):
        task_payload = ModifyTaskPayload(
            content=f'test content {i+1}',
            user_id=test_user_id,
            task_id=f'test_task_{i+1}',
            is_done=True
        )
        response = create_task(task_payload)
        tasks.append(response.task)
    yield tasks


@pytest.fixture(scope="function")
def task_cleanup():
    """
    A fixture to register tasks for cleanup.
    It provides a helper function to register task IDs and performs the actual deletion after the test finishes.

    Yields:
    - A helper function to register tasks by their IDs for cleanup.

    After the test function yields, all registered tasks are deleted.
    """
    tasks_to_cleanup = []

    def register_task_to_cleanup(task_id: str):
        """
        Adds a task ID to the list of tasks to be cleaned up after test execution.
        """
        tasks_to_cleanup.append(task_id)

    yield register_task_to_cleanup

    # Cleanup registered tasks
    for task_id in tasks_to_cleanup:
        delete_task(task_id)



