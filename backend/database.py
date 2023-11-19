### DATABASE SEMENTARA
# import sqlite3
import sqlite3
import uuid
from model.jadwal import Jadwal

list_of_item: list[Jadwal] = []

def connect_to_databse():
    conn = sqlite3.connect('scheduler.db')
    c = conn.cursor()

    c.execute(
        '''
    CREATE TABLE IF NOT EXISTS schedules (
    id TEXT,
    nama_tugas TEXT,
    tanggal TEXT,
    waktu TEXT
    )
    '''
    )

    conn.commit()
    conn.close()
    # return conn

def add_schedule(id_task, nama_tugas, tanggal, waktu):
    conn = sqlite3.connect('scheduler.db')
    c = conn.cursor()

    c.execute("""
INSERT INTO schedules (id, nama_tugas, tanggal, waktu) VALUES (?)
""", (id_task, nama_tugas, tanggal, waktu))

def view_schedule():
    conn = sqlite3.connect('scheduler.db')
    c = conn.cursor()

    c.execute('''
    SELECT * FROM schedules
''')


    schedules = c.fetchall()

    conn.close()

    for schedule in schedules:
        print(schedule[0])


def delete_schedule(id_task):
    conn = sqlite3.connect('scheduler.db')
    c = conn.cursor()

    c.execute('DELETE FROM schedules WHERE task = ?', (id_task),)

def generate_unique_id():
    unique_id = str(uuid.uuid4())
    return unique_id

# con = sqlite3.connect('database.db')

# cursor = con.cursor()

# cursor.execute(
#     '''
#     CREATE TABLE jadwal
#     ()
# '''
# )
