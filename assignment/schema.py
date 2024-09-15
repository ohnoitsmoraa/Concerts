import sqlite3

CONN = sqlite3.connect('concerts.db')
CURSOR = CONN.cursor()

# Creating bands table
CURSOR.execute('''
CREATE TABLE IF NOT EXISTS bands (
    name TEXT PRIMARY KEY,
    hometown TEXT)
''')

# Creating venues table
CURSOR.execute ('''
CREATE TABLE IF NOT EXISTS venues (
    title TEXT PRIMARY KEY,
    city TEXT)
''')

# Creating concerts table to merge with data from bands and venues table
CURSOR.execute('''
CREATE TABLE IF NOT EXISTS concerts (
    id INTEGER PRIMARY KEY,
    band_name TEXT,
    venue_title TEXT,
    date TEXT,
    FOREIGN KEY (band_name) REFERENCES bands(name),
    FOREIGN KEY (venue_title) REFERENCES venues(title))
''')

CONN.commit()
CONN.close()
