import os
import pytest

from repositories import TaskRepository


@pytest.fixture(scope='function')
def task_repository() -> TaskRepository:
    result = TaskRepository()
    result.append('Tarefa de teste')
    return result


def test_task_init() -> None:
    os.system('task init ./tests')
    assert 'tasks' in os.listdir('./tests')
    assert 'main.json' in os.listdir('./tests/tasks')


def test_append_task(task_repository: TaskRepository) -> None:
    os.system('task append "Tarefa de teste 2"')
    assert task_repository.get_by_name('Tarefa de teste 2')
    assert len(task_repository.all()) == 2


def test_pop_task(task_repository: TaskRepository) -> None:
    os.system('task pop 1')
    assert len(task_repository.all()) == 0


def test_remove_task(task_repository: TaskRepository) -> None:
    os.system('task remove "Tafera de teste"')
    assert len(task_repository.all()) == 0
