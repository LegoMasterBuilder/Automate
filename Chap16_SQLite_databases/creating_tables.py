import sqlite3
conn = sqlite3.connect('example.db', isolation_level=None)

# creating table
conn.execute('CREATE TABLE IF NOT EXISTS cats (name TEXT NOT NULL, birthdate TEXT, fur TEXT, weight_kg REAL) STRICT')

# listing tables and columns
conn.execute('SELECT name FROM sqlite_schema WHERE type="table"').fetchall()

# inserting data into the database
# using direct method
conn.execute('INSERT INTO cats VALUES ("Zophie", "2021-01-24", "black", 5.6)')

cat_name = 'Zophie'
cat_bday = '2021-01-24'
fur_color = 'black'
cat_weight = 5.6

# using indirect method
conn.execute('INSERT INTO cats VALUES (?, ?, ?, ?)', [cat_name, cat_bday, fur_color, cat_weight])

# reading data from the database
conn.execute('SELECT * FROM cats').fetchall()

# get only rowid and name columns
conn.execute('SELECT rowid name FROM cats').fetchall()

# print("--- USING FOR LOOP ---")
# Looping over Query Results
# for row in conn.execute('SELECT * FROM cats'):
#     print('Row data:', row)
#     print(row[0], 'is one of my favorite cats.')

# use of WHERE clause
conn.execute('SELECT * FROM cats WHERE fur = "black"').fetchall()

# print("--- USING PPRINT ---")
import pprint
matching_cats = conn.execute('SELECT * FROM cats WHERE fur = "black" OR birthdate >= "2024-01-01"').fetchall()
# pprint.pprint(matching_cats)

# Using % wildcard
# Right end
conn.execute('SELECT rowid, name FROM cats WHERE name LIKE "%y"').fetchall()
# Left end
conn.execute('SELECT rowid, name FROM cats WHERE name LIKE "Ja%"').fetchall()
# Middle
conn.execute('SELECT rowid, name FROM cats WHERE name LIKE "%ob%"').fetchall()

# case sensitive match GLOB *
conn.execute('SELECT rowid, name FROM cats WHERE name GLOB "*m*"').fetchall()

# Ordering the Results
conn = sqlite3.connect('sweigartcats.db', isolation_level=None)
# pprint.pprint(conn.execute('SELECT * FROM cats ORDER BY fur').fetchall())

# Order by multiple columns
cur = conn.execute('SELECT * FROM cats ORDER BY fur, birthdate')
# pprint.pprint(cur.fetchall())

# Order by ascending and descending order
cur = conn.execute('SELECT * FROM cats ORDER BY fur ASC, birthdate DESC')
# pprint.pprint(cur.fetchall())

# Limiting the Number of Results
conn.execute('SELECT * FROM cats LIMIT 3').fetchall()

# Limiting with WHERE and ORDER
conn.execute('SELECT * FROM cats WHERE fur="orange" ORDER BY birthdate LIMIT 4').fetchall()

# Creating Indexes for Faster Data Reading
conn.execute('CREATE INDEX idx_name ON cats (name)')
conn.execute('CREATE INDEX idx_birthdate ON cats (birthdate)')

conn.execute('SELECT name FROM sqlite_schema WHERE type = "index" AND tbl_name = "cats"').fetchall()

# Dropping indexes
conn.execute('SELECT name FROM sqlite_schema WHERE type = "index" AND tbl_name = "cats"').fetchall()
conn.execute('DROP INDEX idx_name')

conn.execute('SELECT name FROM sqlite_schema WHERE type = "index" AND tbl_name = "cats"').fetchall()

# Updating Data in Database