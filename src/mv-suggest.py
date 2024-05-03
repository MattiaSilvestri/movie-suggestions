import utils.widgets as widgets

# import utils.helper as helper
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, ListItem, ListView, Label, Input
from textual.containers import ScrollableContainer
from utils import helper

# from textual.reactive import reactive


class MvSuggest(App):
    """
    Textual app to suggest movies based on user input
    """

    CSS_PATH = "./tcss/styles.tcss"
    BINDINGS = []

    def compose(self) -> ComposeResult:
        """Create child widgets of the app."""
        yield Header()
        yield Footer()
        yield ScrollableContainer(Input("text"), id="list")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle submit action."""

        movie_query = event.input.value
        suggestions_df = helper.lookup_title(
            "../data/movie_similarity.csv", movie_query, 10
        )

        suggestions = [ListItem(Label(i))
                       for i in suggestions_df["index"].values]
        new_list = ListView(*suggestions)
        self.query_one("#list").mount(new_list)


if __name__ == "__main__":
    app = MvSuggest()
    app.run()
