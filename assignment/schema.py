import sqlite3

CONN = sqlite3.connect('concerts.db')
CURSOR = CONN.cursor()

# Creating bands table
CURSOR.execute('''
CREATE TABLE IF NOT EXISTS band (
    id INTEGER PRIMARY KEY,
    name TEXT PRIMARY KEY,
    hometown TEXT)
''')

# Creating venues table
CURSOR.execute ('''
CREATE TABLE IF NOT EXISTS venue (
    id INTEGER PRIMARY KEY,
    title TEXT PRIMARY KEY,
    city TEXT)
''')

# Creating concerts table to merge with data from bands and venues table
CURSOR.execute('''
CREATE TABLE IF NOT EXISTS concert (
    id INTEGER PRIMARY KEY,
    band_name TEXT,
    venue_title TEXT,
    date TEXT,
    FOREIGN KEY (band_name) REFERENCES band(name),
    FOREIGN KEY (venue_title) REFERENCES venue(title))
''')

CONN.commit()
CONN.close()
