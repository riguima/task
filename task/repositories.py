import json
from pathlib import Path
import os

from domain import ITaskRepository, Task


class TaskRepository(ITaskRepository):

    __tasks = json.load(Path(os.getenv('TASK_DIRECTORY') / os.getenv('TASK_PROJECT')))
    
    def all(self) -> list[Task]:
        return [Task(**task) for task in self.__tasks]

    def append(self, name: str) -> None:
        task = Task(len(self.__tasks) + 1, name)
        self.__tasks.append(task.__dict__)

    def pop(self, id: int) -> None:
        self.__tasks.pop(id)

    def remove(self, name: str) -> None:
        task = list(filter(lambda t: t['name'] == name, self.__tasks))
        if task:
            self.__tasks.remove(task[0])
