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
    formatted_data = dict.fromkeys(all_titles, None)

    # Remove to the "title" column so it doesn't get into the vectorizer
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

        formatted_data[all_titles[i]] = str_value

    return formatted_data
