"""Command line interface for :mod:`animated_barnacle`.

Why does this file exist, and why not put this in ``__main__``?
You might be tempted to import things from ``__main__``
later, but that will cause problems--the code will get executed twice:

- When you run ``python3 -m animated_barnacle`` python will execute``__main__.py`` as a script.
  That means there won't be any ``animated_barnacle.__main__`` in ``sys.modules``.
- When you import __main__ it will get executed again (as a module) because
  there's no ``animated_barnacle.__main__`` in ``sys.modules``.

.. seealso:: https://click.palletsprojects.com/en/8.1.x/setuptools/#setuptools-integration
"""

import logging

import click

__all__ = [
    "main",
]

logger = logging.getLogger(__name__)


@click.command()
@click.option("--file1", type=click.Path(exists=True), required=True,
              help="The first file should be a proteomics experiment")
@click.option("--file2")
@click.option("--cutoff", type=int, default=0, help="The cutoff should be a positive integer")
@click.option("--output")
def main(file1, file2, output):
    """CLI for animated_barnacle."""
    from .api import run_my_workflow

    run_my_workflow(file1, file2, output)


if __name__ == "__main__":
    main()
