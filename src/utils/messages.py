"""Define custom messages"""

from textual.messages import Message
from utils.widgets import MovieList
from textual import worker


class MoviesSuggested(Message):
    """Forcasted when the suggested movies are found and ordered"""

    def __init__(self, titles: MovieList | None):
        self.titles = titles
        super().__init__()
