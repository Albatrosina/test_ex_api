import requests
from .models import ModifyTaskPayload, CreateTaskResponse, TaskBody, UpdatedTaskPayload, TaskList, DeletedTaskPayload

BASE_URL = "https://todo.pixegami.io"


def create_task(task_payload: ModifyTaskPayload) -> CreateTaskResponse:
    """
    Sends a PUT request to create a new task with the given payload.

    Parameters:
    - task_payload: The payload for the task creation containing content, user ID, task ID, and completion status.

    Returns:
    - An instance of CreateTaskResponse containing the created task details.

    Raises:
    - Exception: If the task creation request fails.
    """
    url = f'{BASE_URL}/create-task'
    payload = task_payload.__dict__
    response = requests.put(url=url, json=payload)

    if str(response.status_code).startswith('2'):
        task_response = TaskBody(**response.json()['task'])
        return CreateTaskResponse(task=task_response)
    else:
        raise Exception(f"Create task request failed. Status code is {response.status_code}")


def get_task(task_id: str) -> TaskBody:
    """
    Fetches a task by its unique ID using a GET request.

    Parameters:
    - task_id: The unique identifier of the task to retrieve.

    Returns:
    - An instance of TaskBody containing the details of the task.

    Raises:
    - Exception: If the task details are not found or the GET request fails.
    """
    url = f'{BASE_URL}/get-task/{task_id}'
    response = requests.get(url)

    if str(response.status_code).startswith('2'):
        task_details = response.json()
        if task_details:
            return TaskBody(**task_details)
        else:
            raise Exception(f'Task details not found in the response! {task_details}')
    else:
        raise Exception(f'Get task request failed. Status code is {response.status_code}')


def update_task(task_payload: ModifyTaskPayload) -> UpdatedTaskPayload:
    """
    Updates an existing task using a PUT request with the provided task payload.

    Parameters:
    - task_payload: The payload for updating the task, which includes the task ID and new values for the task.

    Returns:
    - An instance of UpdatedTaskPayload containing the updated task details.

    Raises:
    - Exception: If the task update request fails or no updated task ID is returned.
    """
    url = f'{BASE_URL}/update-task'
    payload = task_payload.__dict__
    response = requests.put(url=url, json=payload)
    updated_task_id = response.json()

    if updated_task_id:
        return UpdatedTaskPayload(**updated_task_id)
    else:
        raise Exception('Task update failed or the updated task id was not returned.')


def list_tasks(user_id: str) -> TaskList:
    """
    Retrieves a list of tasks for a specific user ID using a GET request.

    Parameters:
    - user_id: The unique identifier of the user whose tasks to retrieve.

    Returns:
    - An instance of TaskList containing all tasks associated with the user.

    Raises:
    - Exception: If the task list is not found in the response or the GET request fails.
    """
    url = f'{BASE_URL}/list-tasks/{user_id}'
    response = requests.get(url)

    if str(response.status_code).startswith('2'):
        task_list = response.json()
        if task_list:
            return TaskList(tasks=[TaskBody(**task) for task in task_list['tasks']])
        else:
            raise Exception(f'Task list not found in the response -> {task_list}')
    else:
        raise Exception(f'Get list request failed. Status code is {response.status_code}')


def delete_task(task_id: str) -> DeletedTaskPayload:
    """
    Deletes a task by its unique ID using a DELETE request.

    Parameters:
    - task_id: The unique identifier of the task to be deleted.

    Returns:
    - An instance of DeletedTaskPayload indicating success of the deletion.

    Raises:
    - Exception: If the task deletion request fails or the deleted task ID is not returned.
    """
    url = f'{BASE_URL}/delete-task/{task_id}'
    response = requests.delete(url)

    if str(response.status_code).startswith('2'):
        deleted_task_id = response.json()
        if deleted_task_id:
            return DeletedTaskPayload(**deleted_task_id)
        else:
            raise Exception('Task delete failed or the deleted task id was not returned.')
    else:
        raise Exception(f'Delete task request failed. Status code is {response.status_code}')




