Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

The goal is to create a Postgres database with tables designed to optimize queries on song play analysis.

Project Description
In this project, I created a database (star) schema and ETL pipeline for this analysis using Python and SQL. The tables are defined below:

Fact Table
songplays - records in log data associated with song plays i.e. records with page NextSong
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

Dimension Tables
users - users in the app
user_id, first_name, last_name, gender, level

songs - songs in music database
song_id, title, artist_id, year, duration

artists - artists in music database
artist_id, name, location, latitude, longitude

time - timestamps of records in songplays broken down into specific units
start_time, hour, day, week, month, year, weekday

Project Design

Database Design is very optimized because with a few number of tables and doing specific joins, we can get the most information and perform analysis

ETL Design is also simplified to read json files and parse accordingly to store the tables into specific columns and proper formatting

Database Script

Writing "!python create_tables.py" command in the notebook, it is easier to create and recreate tables

Jupyter Notebook

etl.ipynb, a Jupyter notebook is given to verify each command and data. This also provides insights on the best way to create the tables and the constraints around the insert functions. The commands written in etl.ipnyb can be copied into into etl.py and run on a terminal using "python etl.py" to implement. The test.ipynb can then be run to check whether data has been loaded into all the tables and loaded appropraitely.

Relevant Files Provided

test.ipynb displays the first few rows of each table to let you check your database. It also helps check the structures of the tables and if the appropraite constraints were applied.

create_tables.py drops and creates the tables.

etl.ipynb reads and processes a single file from song_data and log_data and loads the data into the tables. This notebook contains detailed instructions on the ETL process for each of the tables.

etl.py reads and processes files from song_data and log_data and loads them into the tables. It somewhat replicates the etl.ipynb

sql_queries.py contains all your sql queries, and is imported into the last three files above.

