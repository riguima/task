from dataclasses import dataclass
from datetime import datetime
import json
import os
from marshmallow import Schema, fields, post_load
from pathlib import Path


@dataclass
class Task:
    id: int
    name: str
    is_checked: bool = False
    created_at: datetime = datetime.now()


class TaskSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    is_checked = fields.Bool()
    created_at = fields.DateTime()

    @post_load
    def make_task(self, data: dict, **kwargs) -> Task:
        return Task(**data)


def commit(function: callable) -> callable:
    def decorator(*args, **kwargs) -> list[Task]:
        last_commit_number = len(os.listdir(get_commits_dir()))
        filename = get_commits_dir() / f'{last_commit_number + 1}.json'
        if last_commit_number == 0:
            json.dump([], open(filename, 'w'))
        tasks = function(*args, **kwargs)
        json.dump([TaskSchema().dump(t) for t in tasks], open(filename, 'w'))
        return tasks
    return decorator


def checkout(index: int = -1) -> list[Task]:
    commits = list(map(lambda f: f.split('.')[0], os.listdir(get_commits_dir())))
    filename = get_commits_dir() / f'{sorted(commits)[index]}.json'
    return [TaskSchema().load(t) for t in json.load(open(filename, 'r'))]


@commit
def add(name: str) -> list[Task]:
    tasks = checkout()
    tasks.append(Task(len(tasks) + 1, name))
    return tasks


@commit
def rm(index: int) -> list[Task]:
    tasks = checkout()
    tasks.pop(index)
    return tasks


def show() -> None:
    result = f'{"ID": ^10}{"NAME": ^50}CHECKED'
    for task in checkout():
        result += f'\n{task.id: ^10}{task.name: <50}{"V" if task.is_checked else "X": ^7}'
    print(result)


def get_commits_dir() -> Path:
    return Path(os.getenv('COMMITS_DIR', Path.home() / 'commits'))
