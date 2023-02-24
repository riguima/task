from dataclasses import dataclass
from abc import ABC, abstractmethod
from datetime import datetime


@dataclass
class Task:
    id: int
    name: str
    created_at: datetime = datetime.now()


class ITaskRepository(ABC):

    @abstractmethod
    def all(self) -> list[Task]:
        raise NotImplementedError()
    
    @abstractmethod
    def append(self, name: str) -> Task:
        raise NotImplementedError()

    @abstractmethod
    def pop(self, id: int) -> None:
        raise NotImplementedError()

    @abstractmethod
    def remove(self, name: str) -> None:
        raise NotImplementedError()
