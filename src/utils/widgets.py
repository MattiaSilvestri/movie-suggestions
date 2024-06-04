"""Define widgets"""

from textual.widgets import ListView
from .messages import CursorChanged


class MovieList(ListView):
    """Movie list widget"""

    def watch_index(self, old_index: int, new_index: int) -> None:
        """Update highlighted child when index changes"""
        self.children[old_index].remove_class("highlighted")
        self.children[new_index].add_class("highlighted")
        self.post_message(CursorChanged(self.children[new_index]))
