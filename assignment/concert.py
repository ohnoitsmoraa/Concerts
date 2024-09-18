import sqlite3

CONN = sqlite3.connect('concert.db')
CURSOR = CONN.cursor()

class Concert:

    # Initialization
    def __init__(self, id, band_name, venue_title, date):
        self.id = id
        self.band_name = band_name
        self.venue_title = venue_title
        self.date = date

    # Object Relationship Method
    def band(self):
        CURSOR.execute("SELECT * FROM bands WHERE id = ?", (self.band_id,))
        return Band(*CURSOR.fetchone())

    def venue(self):
        CURSOR.execute("SELECT * FROM venues WHERE id = ?", (self.venue_id,))
        return Venue(*CURSOR.fetchone())
    
    # Aggregate and Relationship Methods
    def hometown_show(self):
        CURSOR.execute("""
            SELECT b.hometown, v.city
            FROM concerts c
            JOIN bands b ON c.band_id = b.id
            JOIN venues v ON c.venue_id = v.id
            WHERE c.id = ?
        """, (self.id,))
        band_hometown, venue_city = CURSOR.fetchone()
        return band_hometown == venue_city

    def introduction(self):
        CURSOR.execute("""
            SELECT b.name, b.hometown, v.city
            FROM concerts c
            JOIN bands b ON c.band_id = b.id
            JOIN venues v ON c.venue_id = v.id
            WHERE c.id = ?
        """, (self.id,))
        band_name, band_hometown, venue_city = CURSOR.fetchone()
        return f"Hello {venue_city}!!!!! We are {band_name} and we're from {band_hometown}"
    
# Defining classes passed
class Band:
     def __init__(self, id, name, hometown):
        self.id = id
        self.name = name
        self.hometown = hometown

class Venue:
       def __init__(self, id, title, city):
        self.id = id
        self.title = title
        self.city = city