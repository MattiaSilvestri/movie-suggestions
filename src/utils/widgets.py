"""Define widgets"""

from textual.widgets import ListView


class MovieList(ListView):
    """Movie list widget"""

    def action_cursor_down(self) -> None:
        """Action to move cursor down."""
        self.highlighted_child.remove_class("highlighted")
        self.index += 1
        self.highlighted_child.add_class("highlighted")

    def action_cursor_up(self) -> None:
        """Action to move cursor up."""
        self.highlighted_child.remove_class("highlighted")
        self.index -= 1
        self.highlighted_child.add_class("highlighted")
