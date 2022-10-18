# Schema for Song Play Analysis

Using the song and event datasets, I created a star schema optimized for queries on song play analysis. This includes the following tables.

### Fact Table
`songplays` - records in event data associated with song plays i.e. records with page NextSong
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

### Dimension Tables
`users` - users in the app
user_id, first_name, last_name, gender, level
`songs` - songs in music database
song_id, title, artist_id, year, duration
`artists` - artists in music database
artist_id, name, location, lattitude, longitude
`time` - timestamps of records in songplays broken down into specific units
start_time, hour, day, week, month, year, weekday

## Project Template

The project template includes four files:

`create_table.py` is where you'll create your fact and dimension tables for the star schema in Redshift.
`etl.py` is where you'll load data from S3 into staging tables on Redshift and then process that data into your analytics tables on Redshift.
`sql_queries.py` is where you'll define you SQL statements, which will be imported into the two other files above.
`README.md` is where you'll provide discussion on your process and decisions for this ETL pipeline.


### Project Steps
Below are steps followed to complete each component of this project.

- Create Table Schemas
- Design schemas for your fact and dimension tables
- Write a SQL CREATE statement for each of these tables in sql_queries.py
- Complete the logic in create_tables.py to connect to the database and create these tables
- Write SQL DROP statements to drop tables in the beginning of create_tables.py if the tables already exist. This way, you can run create_tables.py whenever you want to reset your database and test your ETL pipeline.
- Launch a redshift cluster and create an IAM role that has read access to S3.
- Add redshift database and IAM role info to dwh.cfg.
- Test by running create_tables.py and checking the table schemas in your redshift database. You can use Query Editor in the AWS Redshift console for this.
- Build ETL Pipeline
- Implement the logic in etl.py to load data from S3 to staging tables on Redshift.
- Implement the logic in etl.py to load data from staging tables to analytics tables on Redshift.
- Test by running etl.py after running create_tables.py and running the analytic queries on your Redshift database to compare your results with the expected results.
- Delete your redshift cluster when finished.