import sqlite3

CONN = sqlite3.connect('concert.db')
CURSOR = CONN.cursor()

class Venue:

    # Initialization
    def __init__(self, id, title, city):
        self.id = id
        self.title = title
        self.city = city

    # Object Relationship Method
    def concerts(self):
        CURSOR.execute("""
            SELECT c.*
            FROM concerts c
            WHERE c.venue_id = ?
        """, (self.id,))
        return [Concert(*row) for row in CURSOR.fetchall()]

    def bands(self):
        CURSOR.execute("""
            SELECT DISTINCT b.*
            FROM bands b
            JOIN concerts c ON b.id = c.band_id
            WHERE c.venue_id = ?
        """, (self.id,))
        return [Band(*row) for row in CURSOR.fetchall()]
    
    # Aggregate and Relationship Methods
    def concert_on(self, date):
        CURSOR.execute("""
            SELECT c.*
            FROM concerts c
            WHERE c.venue_id = ? AND c.date = ?
        """, (self.id, date))
        concert = CURSOR.fetchone()
        if concert:
            return Concert(*concert)
        else:
            return None

    def most_frequent_band(self):
        CURSOR.execute("""
            SELECT b.id, COUNT(c.id) as count
            FROM bands b
            JOIN concerts c ON b.id = c.band_id
            WHERE c.venue_id = ?
            GROUP BY b.id
            ORDER BY count DESC
            LIMIT 1
        """, (self.id,))
        band_id, _ = CURSOR.fetchone()
        return Band(band_id, *CURSOR.execute("SELECT name, hometown FROM bands WHERE id = ?", (band_id,)).fetchone())

    