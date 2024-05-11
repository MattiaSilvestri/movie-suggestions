"""Define widgets"""

from textual.widgets import ListView


class MovieList(ListView):
    """Movie list widget"""

    def watch_index(self, old_index: int, new_index: int) -> None:
        """Update highlighted child when index changes"""
        self.children[old_index].remove_class("highlighted")
        self.children[new_index].add_class("highlighted")
