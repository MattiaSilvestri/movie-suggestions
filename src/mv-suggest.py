import utils.widgets as widgets
import utils.helper as helper
from textual.app import App, ComposeResult
from textual.widgets import Button, Footer, Header, Static
from textual.containers import ScrollableContainer
from textual.reactive import reactive

# # Get movie title from user
# title = widgets.get_titles()
#
# # Provide suggestions
# suggestions = helper.lookup_title("../data/movie_similarity.csv", title, 10)
# for i in suggestions["index"].values:
#     print(i)


class MvSuggest(App):
    """
    Textual app to suggest movies based on user input
    """

    CSS_PATH = "./tcss/styles.tcss"

    def compose(self) -> ComposeResult:
        """Create child widgets of the app."""
        yield Header()
        yield ScrollableContainer(widgets.TextInput("text"))


if __name__ == "__main__":
    app = MvSuggest()
    app.run()
