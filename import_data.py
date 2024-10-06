import pandas as pd
from sqlalchemy import create_engine

# Połączenie z bazą danych PostgreSQL
engine = create_engine('postgresql://user:password@db:5432/movielens')

# Wczytanie danych z plików CSV
movies = pd.read_csv('/data/ml-latest-small/movies.csv')
ratings = pd.read_csv('/data/ml-latest-small/ratings.csv')

# Import danych do bazy danych PostgreSQL
movies.to_sql('movies', engine, if_exists='replace', index=False)
ratings.to_sql('ratings', engine, if_exists='replace', index=False)

print("Dane zostały zaimportowane!")
