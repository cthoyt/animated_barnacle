"""This is a test package."""

from .api import run_my_workflow

__all__ = [
    "run_my_workflow",
    "HELLO",
    "hello",
    "HelloFactory",
]

HELLO = 4


def hello(name: str):
    """Print a hello message.

    :param name: The name of the person to be greeted
    """
    print(f"Hello, {name}")  # noqa


class HelloFactory:
    """This factory makes hellos."""

    def __init__(self, name):
        """Instantiate a hello factory object.

        :param name: The name of the person to be factoried.
        """
        self.name = name

    def print(self):
        """Print a hello message."""
        print(f"Hello, {self.name}")  # noqa
