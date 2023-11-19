from datetime import datetime
from datetime import time

class Jadwal:
    def __init__(self, id: str, nama_acara: str, date: datetime, waktu: time):
        self.id = id
        self.nama_acara = nama_acara
        self.date = date
        self.waktu = waktu