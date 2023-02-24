from dataclasses import dataclass
from datetime import datetime
import json
import os
from pathlib import Path


@dataclass
class Task:
    id: int
    name: str
    created_at: datetime = datetime.now()


def commit(tasks: list[Task], commits_dir: Path) -> None:
    commit_number = len(os.listdir(commits_dir)) + 1
    json.dump(jsonify(tasks), open(commits_dir / f'{commit_number}.json', 'w'))


def checkout(commits_dir: Path, commit_number: int = -1) -> list[Task]:
    filename = commits_dir / os.listdir(commits_dir)[commit_number]
    return list(map(lambda t: Task(**t), json.load(open(filename, 'w'))))


def add(name: str, commits_dir: Path) -> Task:
    tasks = checkout(commits_dir)
    task = Task(len(tasks) + 1, name)
    tasks.append(task)
    commit(tasks, commits_dir)
    return task


def rm(id: int, commits_dir: Path) -> Task:
    tasks = checkout(commits_dir)
    task = tasks.pop(id)
    commit(tasks, commits_dir)
    return task


def jsonify(tasks: list[Task]) -> list[dict]:
    return list(map(lambda t: t.__dict__, tasks))
