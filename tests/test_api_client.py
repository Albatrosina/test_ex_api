from ..src.api_client import get_task, update_task, list_tasks, delete_task


def test_create_task(create_test_task):
    # This test verifies that a task can be created with the specified content and completion status.
    # The task is created using a predefined fixture.
    task = create_test_task

    # Assert that the content of the created task matches the expected content.
    assert task.content == 'test content', \
        f'Content differs from the requested {task.content}'

    # Assert that the created task is marked as not done.
    assert not task.is_done, f'The status of task supposed to be False, got {task.is_done} instead.'


def test_get_task(create_test_task):
    # This test checks if a task can be successfully retrieved by its ID after creation.
    task = create_test_task

    # Fetch the task using its ID.
    fetched_task = get_task(task.task_id)

    # Assert that the fetched task's ID matches the original task's ID.
    assert fetched_task.task_id == task.task_id, (f'Seems like created task id - {task.task_id} differs from fetched '
                                                  f'task id - {fetched_task.task_id}')

    # Assert that the content of the fetched task matches the content of the original task.
    assert fetched_task.content == task.content, (f'Fetched task content - {fetched_task.content} differs from '
                                                  f'created task content - {task.content}')


def test_update_task(create_test_task):
    # This test verifies that a task can be updated and that the updated task reflects the new content.
    task = create_test_task
    new_content = 'The content after update'

    # Update the task's content.
    task.content = new_content
    updated_task = update_task(task)

    # Fetch the task again to verify the update took effect.
    fetched_task = get_task(updated_task.updated_task_id)

    # Assert that the updated task's ID remains unchanged.
    assert updated_task.updated_task_id == task.task_id, (f'Updated task id should be {task.task_id}, '
                                                          f'got {updated_task.updated_task_id} instead')

    # Assert that the fetched task's content matches the new content.
    assert fetched_task.content == new_content, (f'The content of fetched task should be {new_content}, '
                                                 f'got {fetched_task.content} instead.')


def test_list_tasks_for_user_and_delete_them(test_user_id, create_multiple_tasks, task_cleanup):
    # This test lists all tasks for a user, verifies the correct number of tasks, and then deletes them.
    # It uses a fixture to create multiple tasks and another to clean them up.
    task_list = list_tasks(test_user_id)

    # Assert that at least three tasks exist for the user before deletion.
    assert len(task_list.tasks) == 3, (f'Expected len of tasklist for the user {task_list.tasks[0].user_id} == 3. '
                                       f'Got {len(task_list.tasks)} instead.')

    # Iterate through the list of tasks and delete each one.
    for task in task_list.tasks:
        task_cleanup(task.task_id)
        delete_task(task.task_id)

    # Fetch the list of tasks again to verify that all tasks have been deleted.
    new_task_list = list_tasks(test_user_id)

    # Assert that no tasks remain for the user after deletion.
    assert len(new_task_list.tasks) == 0, (f'Expected len of tasklist for the user {test_user_id} == 0. '
                                          f'Got {len(new_task_list.tasks)} instead.')









