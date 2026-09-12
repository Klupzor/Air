from typing import Optional

from .models import Status, Task


class TaskStore:
    def __init__(self):
        self._tasks: list[Task] = []
        self._next_id = 1

    def add(self, title: str) -> Task:
        task = Task(id=self._next_id, title=title)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def list(self, status: Optional[Status] = None) -> list[Task]:
        if status is None:
            return list(self._tasks)
        return [task for task in self._tasks if task.status == status]

    def mark_done(self, task_id: int) -> Task:
        for task in self._tasks:
            if task.id == task_id:
                task.status = Status.DONE
                return task
        raise KeyError(f"No task with id {task_id}")
