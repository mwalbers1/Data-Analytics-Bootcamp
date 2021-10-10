"""
ETL module for movie data =

Contains methods for :

- extracting movie data
- transformation of movie data
- loading new cleaned data into a database

"""

import json
import pandas as pd
import numpy as np
import os


def extract_wikipedia_movies():
    """
    Extract movie data from wikipedia json file

    return: list of raw wikipedia movies
    """
    file_dir = os.path.join('data', 'wikipedia-movies.json')

    with open(file_dir, mode='r') as file:
        wiki_movies_raw = json.load(file)

    return wiki_movies_raw


def transform_wiki_movies(raw_data):
    """
    transform raw movie data

    args:
        raw_data - list of dictionaries where each dictionary entry is for a movie

    return: list of transformed movies
    """
    return [movie for movie in raw_data if ('Director' in movie or 'Directed by' in movie) and 'imdb_link' in movie
            and 'No. of episodes' not in movie]


def change_column_name(old_name, new_name):
    """
    description: rename key called old_name to new_name

    args:
        old_name: old key name
        new_name: new key name
    """
    pass


if '__main__' == '__name__':
    pass
