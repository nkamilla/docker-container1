import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://user:password@db:5432/movielens')
query = "SELECT COUNT(*) FROM movies"
df = pd.read_sql(query, engine)
print(df)
