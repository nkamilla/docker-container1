
# MovieLens Data Analysis with Docker and PostgreSQL

## Overview

This project sets up a data analysis environment using Docker. It includes two containers:
1. A **PostgreSQL** database to store the MovieLens dataset.
2. A **Jupyter Notebook** container for running Python-based data analysis.

The dataset used is the MovieLens dataset (ml-latest-small), which contains information about movies, users, and ratings.

## Requirements

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/nkamilla/docker-container1.git
cd docker-container1
```

### 2. Download the MovieLens Dataset

Download the latest MovieLens dataset from [here](https://grouplens.org/datasets/movielens/latest/) (ml-latest-small.zip), extract it, and place the extracted `ml-latest-small` directory into the `data/` folder in the project root.

### 3. Build and Run Containers

To build and run the Docker containers, use the following command:

```bash
docker-compose up --build
```

This will:
- Set up a **PostgreSQL** container running the database.
- Set up a **Jupyter Notebook** container for running data analysis.

### 4. Access Jupyter Notebook

Once the containers are up and running, open a browser and go to:

```
http://localhost:8888
```

Jupyter Notebook will be accessible from this URL. You can create new notebooks or open existing ones.

### 5. Import Data to PostgreSQL

In the Jupyter Notebook, run the `import_data.py` script to import the MovieLens data into PostgreSQL:

```bash
!python /home/nkamill/import_data.py
```

This will load the `movies.csv` and `ratings.csv` data into the PostgreSQL database.

### 6. Query Data Using SQL

You can now run SQL queries to analyze the data. Below are some example queries that were used in the analysis:

#### Example SQL Queries

1. **How many movies are in the dataset?**
   ```sql
   SELECT COUNT(*) FROM movies;
   ```

2. **What is the most frequent movie genre?**
   ```sql
   SELECT genre, COUNT(*) as count
   FROM (
       SELECT unnest(string_to_array(movies.genres, '|')) as genre
       FROM movies
   ) AS genres
   GROUP BY genre
   ORDER BY count DESC
   LIMIT 1;
   ```

3. **What are the top 10 highest-rated movies?**
   ```sql
   SELECT movies.title, AVG(ratings.rating) as avg_rating
   FROM ratings
   JOIN movies ON ratings."movieId" = movies."movieId"
   GROUP BY movies.title
   ORDER BY avg_rating DESC
   LIMIT 10;
   ```

4. **Who are the top 5 users by number of ratings?**
   ```sql
   SELECT "userId", COUNT(*) as rating_count
   FROM ratings
   GROUP BY "userId"
   ORDER BY rating_count DESC
   LIMIT 5;
   ```

5. **When was the first and last rating made and what were the rated movies?**
   ```sql
   SELECT 
       MIN(ratings.timestamp) as first_rating, 
       MAX(ratings.timestamp) as last_rating,
       (SELECT title FROM movies WHERE "movieId" = (SELECT "movieId" FROM ratings ORDER BY timestamp ASC LIMIT 1)) as first_movie,
       (SELECT title FROM movies WHERE "movieId" = (SELECT "movieId" FROM ratings ORDER BY timestamp DESC LIMIT 1)) as last_movie
   FROM ratings;
   ```

6. **Find all movies released in 1990:**
   ```sql
   SELECT title 
   FROM movies
   WHERE title LIKE '%%(1990)%%';
   ```

### 7. Shutting Down

To stop and remove the containers, run the following command:

```bash
docker-compose down
```

This will stop the running containers and remove them.

## Project Structure

```
├── data/
│   └── ml-latest-small/         # MovieLens dataset directory (after extraction)
├── notebooks/                   # Jupyter notebooks for analysis
├── Dockerfile                   # Dockerfile for the analytics container
├── Dockerfile_python            # (Optional) Separate Dockerfile for Python-based processing
├── docker-compose.yml           # Docker Compose file to run both PostgreSQL and Jupyter
├── import_data.py               # Python script to import data into PostgreSQL
└── README.md                    # This file
```

## Notes

- Ensure that Docker and Docker Compose are installed on your system before running the project.
- The PostgreSQL database will be available on port `5432` (by default).
- The Jupyter Notebook will be accessible on port `8888`.

## License

This project is provided for educational purposes and is licensed under Kamilla
