# Introduction
A startup called `Sparkify` wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.

The goal is to create an Apache Cassandra with tables designed to which can create queries on song play data to answer the question of what customers are listening to  .

## Project Description
In this project, I would be applying data modelling with Apache Cassandra and complete an ETL pipeline using Python. I am provided with part of the ETL pipeline that transfers data from a set of CSV files within a directory to create a streamlined CSV file to model and insert data into Apache Cassandra tables.

### Datasets
I worked with the `event_data` dataset. The directory of contains CSV files partitioned by date. Here are examples of filepaths to two files in the dataset:
`event_data/2018-11-08-events.csv`
`event_data/2018-11-09-events.csv`


### Project Design

The project template includes one Jupyter Notebook file, in which:

- I processed the event_datafile_new.csv dataset to create a denormalized dataset
- I modelled the data tables keeping in mind the queries I needed to run
- I was provided queries that I will need to model my data tables for. This guided the tables created.
- I loaded the data into tables initially create in Apache Cassandra and ran your queries to test if the denormalised tables were properly created.



## Project Steps
Below are steps I followed to complete each component of this project.

#### Modeling your NoSQL database or Apache Cassandra database
- Design tables to answer the queries outlined in the project template
- Write Apache Cassandra CREATE KEYSPACE and SET KEYSPACE statements
- Develop your CREATE statement for each of the tables to address each question
- Load the data with INSERT statement for each of the tables
- Include IF NOT EXISTS clauses in your CREATE statements to create tables only if the tables do not already exist. We recommend you also include DROP TABLE statement for each table, this way you can run drop and create tables whenever you want to reset your database and test your ETL pipeline
- Test by running the proper select statements with the correct WHERE clause
#### Build ETL Pipeline
- Implement the logic in section Part I of the notebook template to iterate through each event file in event_data to process and create a new CSV file in Python
- Make necessary edits to Part II of the notebook template to include Apache Cassandra CREATE and INSERT statements to load processed records into relevant tables in your data model
- Test by running SELECT statements after running the queries on your database
