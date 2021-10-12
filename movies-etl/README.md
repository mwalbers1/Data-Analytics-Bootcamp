## ETL (Extract, Transform and Load) Process

### Overview
Refactor [movies-etl notebook](movies-etl.ipynb) for Module 8 exercises into an automated data pipeline.

![](images/film_strip.png)<br/>
*Image source*: www.freepik.com

### Movie Source files 
- Wikipedia data

- Kaggle Metadata

- The ratings data comes from Movielens, extracted from a Kaggle dataset:
<a href="https://www.kaggle.com/rounakbanik/the-movies-dataset" target="_blank">https://www.kaggle.com/rounakbanik/the-movies-dataset</a>. The data contains over 26 million user ratings on a collection of movies.


## Automate ETL Data Pipeline

Three Python classes are created for each type of source file:
- Wikipedia_Movie
- Kaggle
- Ratings

The extract_transform_load function in the ETL_clean_wiki_movies notebook calls methods in each of these classes. Using Python classes allows for a "separation of concerns" design so that code specific to each source file can be tested and maintained in isolation of the other source files. Also, this makes it easier to add new source files in the future as new classes to the ETL data pipeline.

### Deliverable 1
[ETL_function_test](ETL_function_test.ipynb) - Reading movie source files into Pandas DataFrames


### Deliverable 2 
[ETL_clean_wiki_movies](ETL_clean_wiki_movies.ipynb) - Extract and Transform Wikipedia Data


### Deliverable 3
[ETL_clean_kaggle_data](ETL_clean_kaggle_data.ipynb) - Extract and Transform Kaggle Data


### Deliverable 4
Create the Movie Database




