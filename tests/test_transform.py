import pytest
from all_dunders.transform import Transform


@pytest.fixture
def identity() -> Transform:
    return Transform(1, 0, 0, 1)


@pytest.fixture
def zero() -> Transform:
    return Transform(0, 0, 0, 0)


def test_identity_repr(identity: Transform):
    assert repr(identity) == "Transform(1, 0, 0, 1)"


def test_repr_with_negative():
    assert repr(Transform(-2, -1, 0, 1)) == "Transform(-2, -1, 0, 1)"


def test_repr_with_floats():
    t = Transform(1.5, 3.0, 0.2, 1e-02)

    assert eval(repr(t)) == t


def test_bool_positive(identity: Transform):
    assert bool(identity)


def test_bool_negative(zero: Transform):
    assert not bool(zero)


@pytest.mark.parametrize(
    "dunder_name",
    [
        "__doc__",
        "__init__",
        "__new__",
        "__del__",
        "__add__",
        "__radd__",
        "__iadd__",
        "__neg__",
        "__sub__",
        "__rsub__",
        "__isub__",
        "__bool__",
        "__iter__",
        "__reversed__",
        "__len__",
        "__contains__",
        "__getitem__",
        "__getattr__",
        "__getattribute__",
        "__setattr__",
        "__delattr__",
        "__dir__",
        "__eq__",
        "__repr__",
        "__str__",
        "__format__",
    ],
)
def test_dunders_in_class(identity: Transform, dunder_name: str):
    assert dunder_name in dir(identity)
