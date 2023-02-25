from task.domain import checkout
import os


def test_add() -> None:
    os.system('python task/main.py add "Tarefa teste"')
    assert len(checkout()) == 1
    assert checkout()[-1].name == 'Tarefa teste'


def test_rm() -> None:
    os.system('python task/main.py rm 0')
    assert len(checkout()) == 0
    assert checkout() == []
