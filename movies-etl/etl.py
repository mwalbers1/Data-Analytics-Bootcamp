"""
ETL module for movie data -

Contains methods for :

- extracting movie data
- transformation of movie data
- loading new cleaned data into a database

"""

import json
import pandas as pd
import numpy as np
import os
import re


class Wikipedia_Movie:
    def __init__(self):
        """
        Initialize instance of Wikipedia_Movie class

        """
        return

    
    def read_raw_data(file_dir):
        """
        Extract movie data from wikipedia json file

        return: raw data for wikipedia movies
        """
        
        with open(file_dir, mode='r') as file:
            wiki_movies_raw = json.load(file)

        return wiki_movies_raw

    
    def filter_tv(raw_data):
        """
        filter out tv shows from raw movie data

        args:
            raw_data - list of dictionaries where each dictionary entry is for a movie

        return: list of transformed movies with no tv shows
        """
        
        return [movie for movie in raw_data if ('Director' in movie or 'Directed by' in movie) and 'imdb_link' in movie
                and 'No. of episodes' not in movie]  
           
        
    def clean_release_date_column(df):
        """
        Clean the release date column in wikipedia dataframe
        
        args:
            df: wikipedia data frame
            
        return: release date column as Pandas Series
        """
        release_date = df['Release date'].dropna().apply(lambda x: ' '.join(x) if type(x) == list else x)
        
        date_form_one = r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s[123]?\d,\s\d{4}'
        date_form_two = r'\d{4}.[01]\d.[0123]\d'
        date_form_three = r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}'
        date_form_four = r'\d{4}'
        
        return pd.to_datetime(release_date.str.extract(f'({date_form_one}|{date_form_two}|{date_form_three}|{date_form_four})')[0], infer_datetime_format=True)
        

    def clean_running_time_column(df):
        """
        Clean running time column
        
        args:
            df: wikipedia data frame
            
        """
        # non-null values of Release date in data frame
        running_time = df['Running time'].dropna().apply(lambda x: ' '.join(x) if type(x) == list else x)
        
        running_time_extract = running_time.str.extract(r'(\d+)\s*ho?u?r?s?\s*(\d*)|(\d+)\s*m')
        running_time_extract = running_time_extract.apply(lambda col: pd.to_numeric(col, errors='coerce')).fillna(0)
        
        return running_time_extract.apply(lambda row: row[0]*60 + row[1] if row[2] == 0 else row[2], axis=1)
        

class Kaggle_Movie:
    def __init__(self):
        """
        Initialize instance of Kaggle_Movie class

        """
        return        

    
    def fill_missing_kaggle_data(df, kaggle_column, wiki_column):
        """
        Utility function to fill in missing kaggle column with value from wiki column

        args:
            df: dataframe
            kaggle_column: name of kaggle column
            wiki_column: name of wikipedia column
        """
        df[kaggle_column] = df.apply(lambda row: row[wiki_column] if row[kaggle_column] == 0 else row[kaggle_column], axis=1)
        df.drop(columns=wiki_column, inplace=True)
        
        return df
        
        
if __name__ == '__main__':
    pass
