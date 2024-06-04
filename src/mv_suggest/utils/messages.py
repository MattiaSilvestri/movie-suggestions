"""Define custom messages"""

from textual.messages import Message

# from utils.widgets import MovieList
# from textual.widgets import ListItem


class MoviesSuggested(Message):
    """Forcasted when the suggested movies are found and ordered"""

    def __init__(self, titles):
        self.titles = titles
        super().__init__()


class CursorChanged(Message):
    """Forcasted when the cursor is moved"""

    def __init__(self, item):
        self.item = item
        super().__init__()
