from pathlib import Path
import pytest
import os
from task.domain import Task, commit, jsonify, add, checkout, rm
import re


@pytest.fixture(scope='function')
def tasks() -> list[Task]:
    return [Task(1, 'Tarefa para teste')]


@pytest.fixture(scope='module')
def path() -> Path:
    return Path('./tests/commits')


def test_commit(tasks: list[Task], path: Path) -> None:
    commits_count = len(os.listdir(path))
    commit(tasks, path)
    assert os.listdir(path) == commits_count + 1
    assert tasks == checkout(path)


def test_checkout(tasks: list[Task], path: Path) -> None:
    assert tasks == checkout(path, 0)


def test_add(path: Path) -> None:
    task = add('Tarefa teste 2', path)
    assert task in checkout(path)


def test_rm(path: Path) -> None:
    task = rm(2, path)
    assert task not in checkout(path)


def test_jsonify(tasks: list[Task]) -> None:
    assert {'id': 1, 'name': 'Tarefa de teste'} in jsonify(tasks)[0]
    regex = re.compile(r'\d{4}(-\d{2}){2} \d{2}:\d{2}')
    assert regex.findall(jsonify(tasks)[0])
