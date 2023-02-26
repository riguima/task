from task.domain import add, checkout, rm, show


def test_add() -> None:
    tasks = add('Tarefa teste')
    assert tasks == checkout()
    assert tasks[-1].name == 'Tarefa teste'
    assert tasks[-1].is_checked == False


def test_rm() -> None:
    tasks = rm(0)
    assert tasks == checkout()
    assert tasks == []


def test_checkout() -> None:
    assert len(checkout(0)) == 1
    assert checkout(0)[0].name == 'Tarefa teste'


def test_show() -> None:
    expected = (f'{"ID": ^4}{"NAME": ^50}CHECKED'
                f'\n{"1": ^3}{"Tarefa teste": <50}X')
    assert show(checkout(0)) == expected
