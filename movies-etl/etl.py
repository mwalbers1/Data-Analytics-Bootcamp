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


class Wikipedia_Movie:
    def __init__(self, file_dir):
        """
        Initialize instance of Wikipedia_Movie class
        
        args:
            file_dir: path to source wikipedia file
        """
        self._file_dir = file_dir

    
    def read_raw_data(self):
        """
        Extract movie data from wikipedia json file

        return: raw data for wikipedia movies
        """
        
        with open(self._file_dir, mode='r') as file:
            wiki_movies_raw = json.load(file)

        return wiki_movies_raw

    
    def read_data_df(self, raw_data):
        """
        Extract movie data from wikipedia raw data and return as DataFrame
        
        args:
            raw_data: list of dictionaries containing raw wikipedia movie data 
        
        return: DataFrame of wikipedia movies
        """
        
        return pd.DataFrame(wiki_movies_raw)

    
    def filter_tv(raw_data):
        """
        filter out tv shows from raw movie data

        args:
            raw_data - list of dictionaries where each dictionary entry is for a movie

        return: list of transformed movies with no tv shows
        """
        
        return [movie for movie in raw_data if ('Director' in movie or 'Directed by' in movie) and 'imdb_link' in movie
                and 'No. of episodes' not in movie]
    
    
    def extract_imdb_id(df):
        """
        Extract the IMDb ID using a regular expression string and dropping any imdb_id duplicates. 
        If there is an error, capture and print the exception.
        
        args:
            wiki movies DataFrame
            
        return: wiki movies DataFrame with imdb id
        """
        pass
       
        
    def parse_dollars(s):
        """
        Turn extracted values into a numeric value

        args:
            s:  input value to parse against regular expression

        return:
            formatted value resulting from regex substitution
        """

        # if s is not a string, return NaN
        if type(s) != str:
            return np.nan

        # if input is of the form $###.# million
        if re.match(r'\$\s*\d+\.?\d*\s*milli?on', s, flags=re.IGNORECASE):

            # remove dollar sign and " million"
            s = re.sub('\$|\s|[a-zA-Z]','',s)

            # convert to float and multiply by a million
            value = float(s) * 10**6

            return value

        # if input is of the form $###.# billion
        elif re.match(r'\$\s*\d+\.?\d*\s*billi?on', s, flags=re.IGNORECASE):

            # remove dollar sign and " billion"
            s = re.sub('\$|\s|[a-zA-Z]','',s)

            # convert to float and multiply by a billion
            value = float(s) * 10**9

            return value

        # if input is of the form $###,###,###
        elif re.match(r'\$\s*\d{1,3}(?:[,|\.]\d{3})+(?!\s[mb]illion)', s, flags=re.IGNORECASE):

            # remove dollar sign and commas
            s = re.sub('\$|,','',s)

            # convert to float
            value = float(s)

            return value

        # otherwise, return NaN
        else:
            return np.nan


    def wiki_file(self):
        return self._file_dir


if '__main__' == '__name__':
    # file_dir = os.path.join('data', 'wikipedia-movies.json')
    pass
