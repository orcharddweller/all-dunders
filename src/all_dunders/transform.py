from __future__ import annotations

from typing import Any, Iterator


class Transform:
    """
    Notes:

        __closure__ is not possible to use in a class, but we'll have it in __call__
    """

    __slots__ = ("a", "b", "c", "d", "verbose_del")

    def __new__(cls, a: float, b: float, c: float, d: float, verbose_del: bool = False):
        instance = super().__new__(cls)

        return instance

    def __init__(
        self, a: float, b: float, c: float, d: float, verbose_del: bool = False
    ):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.verbose_del = verbose_del

    def __del__(self):
        if self.verbose_del:
            print(f"{self} was deleted")

    def __add__(self, other: object):
        match other:
            case float(x) | int(x):
                return Transform(self.a + x, self.b + x, self.c + x, self.d + x)
            case Transform():
                return Transform(
                    self.a + other.a,
                    self.b + other.b,
                    self.c + other.c,
                    self.d + other.d,
                )
            case _:
                raise NotImplementedError(
                    f"Cannot add an object of type {other} to a Transform!"
                )

    def __radd__(self, other: Transform | float):
        return self.__add__(other)

    def __iadd__(self, other: Transform | float | int):
        match other:
            case float(x) | int(x):
                self.a += x
                self.b += x
                self.c += x
                self.d += x
            case Transform():
                self.a += other.a
                self.b += other.b
                self.c += other.c
                self.d += other.d

        return self

    def __neg__(self):
        return Transform(-self.a, -self.b, -self.c, -self.d)

    def __sub__(self, other: Transform | float):
        return self + (-other)

    def __rsub__(self, other: Transform | float):
        return self.__sub__(other)

    def __isub__(self, other: Transform | float):
        self += -other
        return self

    def __bool__(self):
        return bool(self.a or self.b or self.c or self.d)

    def __hash__(self):
        return hash(tuple(self))

    def __iter__(self) -> Iterator[float]:
        yield from (self.a, self.b, self.c, self.d)

    def __reversed__(self) -> Iterator[float]:
        yield from (self.d, self.c, self.b, self.a)

    def __len__(self):
        return 4

    def __contains__(self, item: float):
        return (item) in (self.a, self.b, self.c, self.d)

    def __getitem__(self, k: int):
        match k:
            case 0:
                return self.a
            case 1:
                return self.b
            case 2:
                return self.c
            case 3:
                return self.d
            case _:
                raise NotImplementedError("Only 0, 1, 2 or 3 allowed.")

    def __getattr__(self, name: str) -> Any:
        raise AttributeError(f"Tranform doesn't have an attribute called {name}")

    def __getattribute__(self, name: str) -> Any:
        if name == "easter_egg":
            print("OH NO!")

        return object.__getattribute__(self, name)

    def __setattr__(self, name: str, value: Any):
        if name == "easter_egg":
            raise AttributeError("You cannot assign to an easter_egg!!!")

        object.__setattr__(self, name, value)

    def __delattr__(self, name: str):
        if name == "easter_egg":
            raise AttributeError("You cannot delete an easter_egg!!!")

        object.__delattr__(self, name)

    def __dir__(self):
        return reversed(list(object.__dir__(self)))

    def __eq__(self, other: object):
        match other:
            case Transform():
                return (
                    self.a == other.a
                    and self.b == other.b
                    and self.c == other.c
                    and self.d == other.d
                )
            case _:
                raise NotImplementedError(
                    f"Transform can only be equal to a transform, not {type(other)}"
                )

        return True

    def __repr__(self) -> str:
        return f"Transform({self.a}, {self.b}, {self.c}, {self.d})"

    def __str__(self) -> str:
        return f"Instance of {repr(self)}"

    def __format__(self, __format_spec: str) -> str:
        match __format_spec:
            case "s":
                return f"T({self.a}, {self.b}, {self.c}, {self.d})"
            case "l" | "":
                return repr(self)
            case _:
                raise NotImplementedError(
                    f"'{__format_spec}' is not a correct format spec,"
                    "please use either 's' or 'l'"
                )
