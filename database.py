import mysql.connector

#database connections
db = mysql.connector.connect(
	host="",
	port=,
	user="",
	passwd="",
	database=""
	)

db2 = mysql.connector.connect(
	host="",
	port=,
	user="",
	passwd="",
	database=""
	)


#queries
select_query = "SELECT * FROM track_data WHERE track = %s AND artist = %s"
country_insert_query = """
				INSERT INTO country_data
				(	country,
					track,
					artist,
					date_added
				)
				VALUES(%s,%s,%s,%s)
				"""
track_data_query = """
				INSERT INTO track_data
				(	track,
					artist,
					sentiment,
					tempo,
					song_key,
					duration,
					time_signature,
					danceability,
					energy,
					loudness,
					speechiness,
					acousticness,
					liveness,
					valence
				)
				VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
				"""
country_update_query = """
				UPDATE country_data 
				SET date_added=%s 
				WHERE country=%s AND track=%s AND artist=%s
				""" 


def create_tables():
	db = mysql.connector.connect(
		host="",
		port=,
		user="",
		passwd="",
		database=""
		)
	mycursor = db.cursor()


	mycursor.execute("""
		CREATE TABLE track_data
		(	track VARCHAR(250),
			artist VARCHAR(100),
			sentiment FLOAT(10),
			tempo FLOAT(10),
			song_key INT,
			duration INT,
			time_signature INT,
			danceability FLOAT(10),
			energy FLOAT(10),
			loudness FLOAT(10),
			speechiness FLOAT(10),
			acousticness FLOAT(10),
			liveness FLOAT(10),
			valence FLOAT(10),
			PRIMARY KEY (track, artist)
		)""")

	mycursor.execute("""
		CREATE TABLE country_data
		(	country VARCHAR(50),
			track VARCHAR(250),
			artist VARCHAR(100),
			date_added DATETIME,
			PRIMARY KEY (country, track, artist)
		)""")

	db.commit()


