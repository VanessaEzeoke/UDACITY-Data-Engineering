import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# GLOBAL VARIABLES
LOG_DATA = config.get("S3","LOG_DATA")
LOG_PATH = config.get("S3", "LOG_JSONPATH")
SONG_DATA = config.get("S3", "SONG_DATA")
IAM_ROLE = config.get("IAM_ROLE","ARN")

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events_table"
staging_songs_table_drop =  "DROP TABLE IF EXISTS staging_songs_table"
songplay_table_drop    =    "DROP TABLE IF EXISTS songplay_table"
user_table_drop       =     "DROP TABLE IF EXISTS user_table"
song_table_drop       =     "DROP TABLE IF EXISTS song_table"
artist_table_drop   =       "DROP TABLE IF EXISTS artist_table"
time_table_drop     =       "DROP TABLE IF EXISTS time_table"

# CREATE TABLES

staging_events_table_create= ("""
CREATE TABLE IF NOT EXISTS staging_events_table (
    artist          VARCHAR,
    auth            VARCHAR, 
    firstName       VARCHAR,
    gender          VARCHAR,   
    itemInSession   INTEGER,
    lastName        VARCHAR,
    length          FLOAT,
    level           VARCHAR, 
    location        VARCHAR,
    method          VARCHAR,
    page            VARCHAR,
    registration    BIGINT,
    sessionId       INTEGER,
    song            VARCHAR,
    status          INTEGER,
    ts              TIMESTAMP,
    userAgent       VARCHAR,
    userId          INTEGER
);
""")

staging_songs_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_songs_table (

);
""")

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplay_table (
    songplay_id          INTEGER IDENTITY(0,1) PRIMARY KEY sortkey,
    start_time           TIMESTAMP,
    user_id              INTEGER,
    level                VARCHAR,
    song_id              VARCHAR,
    artist_id            VARCHAR,
    session_id           INTEGER,
    location             VARCHAR,
    user_agent           VARCHAR
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS user_table (
    user_id INTEGER PRIMARY KEY distkey, 
    first_name VARCHAR, 
    last_name VARCHAR, 
    gender CHAR, 
    level VARCHAR
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS song_table (
    song_id      VARCHAR PRIMARY KEY distkey, 
    title        VARCHAR , 
    artist_id    VARCHAR NOT NULL, 
    year         INTEGER, 
    duration     FLOAT NOT NULL
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artist_table (
    artist_id          VARCHAR PRIMARY KEY distkey,
    name               VARCHAR,
    location           VARCHAR,
    latitude           FLOAT,
    longitude          FLOAT
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time_table (
    start_time TIMESTAMP PRIMARY KEY sortkey distkey, 
    hour       INTEGER, 
    day        INTEGER, 
    week       INTEGER, 
    month      INTEGER, 
    year       INTEGER, 
    weekday    INTEGER
);
""")

# STAGING TABLES

staging_events_copy = ("""
""").format()

staging_songs_copy = ("""
""").format()

# FINAL TABLES

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
INSERT TABLE 
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
