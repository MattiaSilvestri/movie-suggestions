"""General purpose helper functions"""

import pandas as pd


def format_data(data_path: str) -> dict:
    """Format data from csv file.

    Extract data from csv file and create a key-value pair for each movie, where
    the key is the movie title and the value is a string with info about the movie.

    Parameters
    ----------
    data_path : str
        Path to csv file.

    Returns
    -------
    formatted_data : dict
        Key-value pairs for each movie.
    """

    df = pd.read_csv(data_path)
    all_titles = list(df["title"].values)

    # Initialize empty dictionary to hold the title-vector pairs
    formatted_dict = dict.fromkeys(all_titles, None)

    # Remove the "title" column so it doesn't get into the vectorizer
    # algorithm
    df.drop("title", axis=1, inplace=True)

    # Loop throught the dataframe to convert columns to strings
    for i in range(len(all_titles)):
        # Convert values to string
        first = list(map(str, df.iloc[i].values))
        # Split the string
        second = list(map(str.split, first))
        str_value = ""
        # Add spaces between items to make them more readable
        for n in second:
            for j in n:
                str_value = str_value + " " + j

        formatted_dict[all_titles[i]] = str_value

    # Convert dictionary to dataframe
    formatted_data = pd.DataFrame.from_dict(
        formatted_dict, orient="index", columns=["info"]
    )
    formatted_data.reset_index(inplace=True)

    return formatted_data


def lookup_title(data_path: str, title: str, verbose: int) -> pd.DataFrame:
    """Lookup title in data.

    Parameters
    ----------
    data_path : str
        Path to csv file.
    title : str
        Title to lookup.

    Returns
    -------
    info : str
        Info about the movie.
    """

    # Get suggestions
    movies = pd.read_csv(data_path)
    suggestions = movies[["index", title]].sort_values(by=title, ascending=False)[
        1:verbose
    ]

    return suggestions


def get_input_suggestions(data_path: str) -> list:
    """Generate list to use for the input suggester.

    Parameters
    ----------
    data_path : str
        Path to csv file.

    Returns
    -------
    list
        List of titles to use for the input suggester.
    """

    movies = pd.read_csv(data_path)
    titles = list(movies["index"].values)

    return titles
