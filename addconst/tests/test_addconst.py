from addconst.addconst import ConstAdder


def test_addconst():
    add1 = ConstAdder(constant=1)
    assert add1(2) == 3
    assert add1(-1) == 0
    add2 = ConstAdder(constant=2)
    assert add2(2) == 4
    assert add2(-20) == -18
