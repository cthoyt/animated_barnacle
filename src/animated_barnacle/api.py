"""This is a placeholder for putting the main code for your module.

If you don't want to keep ``api.py``, check the following places:

1. ``src/animated_barnacle/__init__.py`` contains a line
   ``from .api import *  # noqa``. You'll want to delete this and likely replace
   it with other imports for the most important functionality for your package
2. ``docs/usage.rst`` contains a line
   ``.. automodule:: animated_barnacle.api``.
   You'll want to delete this and replace it with other imports
3. You don't need to update any linting or testing configuration since it is agnostic
   to the contents of the package.
"""

__all__ = [
    "run_my_workflow",
    "run_my_workflow_helper",
]


def run_my_workflow(
        input_file1,
        input_file2,
        output_directory,
):
    """Run the full workflow.

    :param input_file1: First input file
    :param input_file2: Second input file
    :param output_directory: Output directory, given as a string or path
    """
    with open(input_file1) as f:
        print(f.read()[:50])  # noqa

    with open(input_file2) as f:
        print(f.read()[:50])  # noqa

    print(f"outputting to {output_directory}")  # noqa


def run_my_workflow_helper():
    """Help run the workflow."""
