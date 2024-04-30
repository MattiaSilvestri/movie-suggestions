import utils.cli as cli
import utils.helper as helper

# Get movie title from user
title = cli.get_titles()

# Provide suggestions
suggestions = helper.lookup_title("../data/movie_similarity.csv", title, 10)
for i in suggestions["index"].values:
    print(i)
