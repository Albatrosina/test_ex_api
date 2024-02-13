from dataclasses import dataclass
from typing import List


@dataclass
class ModifyTaskPayload:
    content: str
    user_id: str
    task_id: str
    is_done: bool


@dataclass
class TaskBody:
    user_id: str
    content: str
    is_done: bool
    created_time: int
    task_id: str
    ttl: int


@dataclass
class CreateTaskResponse:
    task: TaskBody


@dataclass
class UpdatedTaskPayload:
    updated_task_id: str


@dataclass
class TaskList:
    tasks: List[TaskBody]


@dataclass
class DeletedTaskPayload:
    deleted_task_id: str
