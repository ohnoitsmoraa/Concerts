import sqlite3

CONN = sqlite3.connect('database.db')
CURSOR = CONN.cursor()

class Band:
    
    # Initialization 
    def __init__(self, id, name, hometown):
        self.id = id
        self.name = name
        self.hometown = hometown

    # Objet Relationship Methods
    def concerts(self):
        CURSOR.execute("""
            SELECT c.*
            FROM concerts c
            WHERE c.band_id = ?
        """, (self.id,))
        return [Concert(*row) for row in CURSOR.fetchall()]

    def venues(self):
        CURSOR.execute("""
            SELECT DISTINCT v.*
            FROM concerts c
            JOIN venues v ON c.venue_id = v.id
            WHERE c.band_id = ?
        """, (self.id,))
        return [Venue(*row) for row in CURSOR.fetchall()]
    
    # Aggregate and Relationship Methods
    def play_in_venue(self, venue_title, date):
        CURSOR.execute("""
            INSERT INTO concerts (band_id, venue_id, date)
            VALUES (?, (SELECT id FROM venues WHERE title = ?), ?)
        """, (self.id, venue_title, date))
        CONN.commit()

    def all_introductions(self):
        CURSOR.execute("""
            SELECT v.city
            FROM concerts c
            JOIN venues v ON c.venue_id = v.id
            WHERE c.band_id = ?
        """, (self.id,))
        cities = [row[0] for row in CURSOR.fetchall()]
        return [f"Hello {city}!!!!! We are {self.name} and we're from {self.hometown}" for city in cities]

    @classmethod
    def most_performances(cls):
        CURSOR.execute("""
            SELECT b.id, COUNT(c.id) as count
            FROM bands b
            JOIN concerts c ON b.id = c.band_id
            GROUP BY b.id
            ORDER BY count DESC
            LIMIT 1
        """)
        band_id, _ = CURSOR.fetchone()
        return cls(band_id, *CURSOR.execute("SELECT name, hometown FROM bands WHERE id = ?", (band_id,)).fetchone())
    
# Defining Concert and Venue classes
class Concert:
      def __init__(self, id, band_name, venue_title, date):
        self.id = id
        self.band_name = band_name
        self.venue_title = venue_title
        self.date = date

class Venue:
     def __init__(self, id, title, city):
        self.id = id
        self.title = title
        self.city = city
