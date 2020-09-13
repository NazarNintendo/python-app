import psycopg2 as psc
from Include.config import config


class DbConnection:

    records = []

    def enable_connection(self):
        conn = psc.connect(f"dbname={config['database']} user={config['user']} password={config['pass']}")
        cur = conn.cursor()
        cur.execute("SELECT * FROM customer;")
        self.records = cur.fetchall()
        cur.close()
        conn.close()
        print(self.records)