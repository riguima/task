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
    created_at: datetime = datetime.now()


class TaskSchema(Schema):
    id = fields.Int()
    name = fields.Str()
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
    return list(map(lambda t: TaskSchema().load(t), json.load(open(filename, 'r'))))


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


def get_commits_dir() -> Path:
    return Path(os.getenv('COMMITS_DIR', Path.home() / 'commits'))
