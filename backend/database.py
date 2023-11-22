import uuid
from model.jadwal import Jadwal
import json
import os


list_of_item: list[Jadwal] = []



class JSONDatabaseManager:
    def __init__(self, json_file='./backend/data.json'):
        self.json_file = json_file
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, 'r') as file:
                return json.load(file)
        return []

    def save_data(self):
        with open(self.json_file, 'w') as file:
            json.dump(self.data, file, indent=2)

    def generate_id(self):
        return str(uuid.uuid4())

    def insert_data(self, nama_jadwal, tanggal, waktu):
        id_jadwal = self.generate_id()
        new_schedule = {
            'id': id_jadwal,
            'nama_jadwal': nama_jadwal,
            'tanggal': tanggal.strftime('%Y-%m-%d'),
            'waktu': waktu.strftime('%H:%M')
        }
        self.data.append(new_schedule)
        self.save_data()
        print("Data berhasil disimpan.")
        return id_jadwal

    def edit_data(self, id_jadwal, nama_jadwal, tanggal, waktu):
        for schedule in self.data:
            if schedule['id'] == id_jadwal:
                schedule['nama_jadwal'] = nama_jadwal
                schedule['tanggal'] = tanggal.strftime('%Y-%m-%d')
                schedule['waktu'] = waktu.strftime('%H:%M')
                self.save_data()
                print("Data berhasil diubah.")
                return True
        print(f"Tidak dapat menemukan jadwal dengan ID {id_jadwal}.")
        return False

    def delete_data(self, id_jadwal):
        for schedule in self.data:
            if schedule['id'] == id_jadwal:
                self.data.remove(schedule)
                self.save_data()
                print("Data berhasil dihapus.")
                return True
        print(f"Tidak dapat menemukan jadwal dengan ID {id_jadwal}.")
        return False

    def get_all_data(self):
        return self.data

# Contoh penggunaan
# db_manager = JSONDatabaseManager()

# Contoh Insert
# schedule_id = db_manager.insert_data('Meeting', datetime(2023, 11, 16), time(14, 0))

# # Contoh Edit
# db_manager.edit_data(schedule_id, 'Updated Meeting', datetime(2023, 11, 17), time(15, 30))

# # Contoh Delete
# db_manager.delete_data(schedule_id)

# # Contoh Get All Data
# all_data = db_manager.get_all_data()
# print(all_data)


object_db = JSONDatabaseManager()


# def generate_unique_id():
#     unique_id = str(uuid.uuid4())
#     return unique_id
