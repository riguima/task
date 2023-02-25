from task.domain import add, checkout, rm, show


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


def test_show() -> None:
    expected = (f'{"ID": ^5}{"NAME": ^50}{"CHECKED": ^4}'
                f'\n{"1": ^5}{"Tarefa teste": <50}{"X": ^4}')
    assert show(checkout(0)) == expected
