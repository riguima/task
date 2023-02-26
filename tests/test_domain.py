from task.domain import add, checkout, rm, check


def test_add() -> None:
    tasks = add('Tarefa teste')
    assert tasks == checkout()
    assert tasks[-1].name == 'Tarefa teste'
    assert tasks[-1].is_checked == False


def test_check() -> None:
    tasks = check(0)
    assert tasks[0].is_checked


def test_rm() -> None:
    tasks = rm(0)
    assert tasks == checkout()
    assert tasks == []


def test_checkout() -> None:
    assert len(checkout(0)) == 1
    assert checkout(0)[0].name == 'Tarefa teste'
