from task.domain import Task, add, checkout, rm


def test_add() -> None:
    tasks = add('Tarefa teste')
    assert tasks == checkout()
    assert tasks[-1].name == 'Tarefa teste'


def test_rm() -> None:
    tasks = rm(0)
    assert tasks == checkout()
    assert tasks == []


def test_checkout() -> None:
    assert len(checkout(0)) == 1
    assert checkout(0)[0].name == 'Tarefa teste'
