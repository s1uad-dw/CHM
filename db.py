import sqlite3
import datetime 

class DB():
    def __init__(self, name):
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    first_name TEXT UNIQUE ON CONFLICT IGNORE,
    subscription_date TEXT DEFAULT "03.03.2022"
)""")

    def add_user(self, first_name):
        self.cursor.execute("""
INSERT INTO users(first_name) VALUES (?)
        """, (first_name))
        self.conn.commit()

    def check_subscriptions(self, first_name):
        if first_name != ('Jost221' or 's1uad_dw'):
            day = datetime.datetime.now()
            sub = self.cursor.execute("""
SELECT subscription_date FROM users WHEN first_name == {}
            """.format(first_name)).fetchall()
            
            difference = (sub-day).days

            print(difference)

            if difference < 30:
                return True
            else:
                return False
        else:
            return True

    def active_subscription(self, first_name):
        day = datetime.datetime.now()
        subscription_date = self.cursor.execute("""
UPDATE users SET subscription_date = {} WHERE first_name == {}
        """.format(day, first_name)).fetchall()