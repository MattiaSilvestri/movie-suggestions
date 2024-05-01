"""Define textual widgets"""

from textual.app import ComposeResult
from textual.widgets import Button, Input


def get_titles():
    title = input("Insert movie title: ")

    return title


class TextInput(Input):
    """Textual widget to get movie title"""
