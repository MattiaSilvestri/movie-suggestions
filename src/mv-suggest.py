from utils.widgets import MovieList
import utils.helper as helper

import pandas as pd

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, ListItem, Label, Input
from textual.containers import ScrollableContainer
from textual.suggester import SuggestFromList

# from textual.reactive import reactive


class MvSuggest(App):
    """
    Textual app to suggest movies based on user input
    """

    CSS_PATH = "./styles/styles.tcss"
    BINDINGS = [
        ("r", "remove_list", "Remove list"),
        ("ctrl+j", "cursor_down", "Moves cursor down"),
        ("ctrl+k", "cursor_up", "Moves cursor up"),
    ]

    # titles = helper.get_input_suggestions("../data/movie_similarity.csv")
    titles = pd.read_csv("../data/titles.csv")["index"].values

    def compose(self) -> ComposeResult:
        """Create child widgets of the app."""
        yield Header()
        yield Footer()
        yield ScrollableContainer(
            Input("text", suggester=SuggestFromList(
                self.titles, case_sensitive=False)),
            id="list",
        )

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle submit action."""

        movie_query = event.input.value
        suggestions_df = helper.lookup_title(
            "../data/movie_similarity.csv", movie_query, 10
        )

        suggestions = [ListItem(Label(i))
                       for i in suggestions_df["index"].values]
        new_list = MovieList(*suggestions)
        # Mount the list view widget
        await self.query_one("#list").mount(new_list)
        # Focus the first item
        mounted_list = self.query_one("MovieList")
        mounted_list.focus()
        mounted_list.highlighted_child.add_class("highlighted")

    def action_remove_list(self) -> None:
        """Action to remove list."""
        list_item = self.query("MovieList")
        if list_item:
            list_item.last().remove()

    def action_cursor_down(self) -> None:
        """Action to move cursor down."""
        self.query_one("MovieList").action_cursor_down()

    def action_cursor_up(self) -> None:
        """Action to move cursor up."""
        self.query_one("MovieList").action_cursor_up()


if __name__ == "__main__":
    app = MvSuggest()
    app.run()
