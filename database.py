# import sqlite3
import psycopg2


class DB:
    def connection(self):
        return psycopg2.connect('postgres://postgres:asdf;lkj@localhost:5432/demo_db')

    def __init__(self):
        try:
            conn = self.connection()
            c = conn.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS students(
                    id BIGSERIAL NOT NULL PRIMARY KEY,
                    firstName VARCHAR(100) NOT NULL,
                    lastName VARCHAR(100) NOT NULL,
                    contactNumber BIGINT NOT NULL,
                    rollNo BIGINT NOT NULL,
                    email VARCHAR(200) NOT NULL,
                    dob DATE NOT NULL,
                    address VARCHAR(250) NOT NULL
                )""")
            
            # if self.run_query("SELECT * FROM students") == []:
            #     c.execute("INSERT INTO students(firstName, lastName, contactNumber, rollNo, email, dob, address ) VALUES( 'Dhanya', 'B', '9344859385', '210420243015', 'dhanyababu2003@gmail.com', '14-09-2002', 'RMK Chola Gardens')")
            conn.commit()
            conn.close()       
        except Exception as e:
            print("Bruh: ", e)
        

    def run_query(self, query: str, *kwargs):
        try:
            conn = self.connection()
            c = conn.cursor()
            c.execute(query, kwargs)
            conn.commit()
            result = c.fetchall()
            conn.close()
            return result
        except Exception as e:
            print("ERROR: bruh", e)