# from plyer import notification
# from datetime import datetime, timedelta
# import time

# def schedule_notification(task, tanggal ,scheduled_time):
#     # Mendapatkan tanggal dan waktu saat ini
#     now = datetime.now()
#     # print(now.date())

#     print(f'type tanggal : {type(tanggal)}')
#     print(f'tanggal : {tanggal}')

#     diff_tanggal = (tanggal.date() - now.date()).days
#     print(f'diff_tanggal {diff_tanggal}')

#     if diff_tanggal < 0:
#         diff_tanggal = 0

#     # diff_tanggal = max(diff_tanggal, 0)

#     # Membaca jam dan menit dari input pengguna
#     scheduled_hour, scheduled_minute = map(int, scheduled_time.split(':'))

#     # Membuat objek datetime untuk waktu yang dijadwalkan besok
#     # scheduled_datetime = datetime(now.year, now.month, now.day, scheduled_hour, scheduled_minute) + timedelta(days=1)
#     scheduled_datetime = datetime(now.year, now.month, now.day, scheduled_hour, scheduled_minute) + timedelta(days=diff_tanggal)

#     print(f'scheduled_datetime : {scheduled_datetime}')

#     # Hitung selisih waktu antara waktu saat ini dan waktu yang dijadwalkan
#     time_difference = scheduled_datetime - now

#     print(f'time_difference : {time_difference}')

#     # Konversi selisih waktu ke detik
#     time_in_seconds = time_difference.total_seconds()

#     print(f'tim_in_seconds : {time_in_seconds}')
#     # Tunggu sampai waktu yang dijadwalkan
#     time.sleep(time_in_seconds)

#     # Munculkan notifikasi
#     notification.notify(
#         title='Notifikasi Jadwal',
#         message=f'Waktunya untuk: {task}',
#         app_icon=None,  # e.g. 'C:\\icon_32x32.ico'
#         timeout=10,  # seconds
#     )

# # Contoh penggunaan:
# # task_name = input("Masukkan nama tugas: ")
# # scheduled_time = input("Masukkan waktu (HH:MM): ")

# # schedule_notification(task_name, scheduled_time)




import asyncio
from time import sleep
from unittest import result
from plyer import notification
from datetime import datetime, timedelta, time
from backend import database as db

class Notification:
    def __init__(self):
        # Fungsi untuk menjadwalkan notifikasi
        # self.schedule_notification()

        # Sisanya dari logika CRUD
        # ...
        pass

    async def schedule_notification(self):
        # Fungsi untuk menjadwalkan notifikasi sesuai jadwal
        # Anda perlu memanggil fungsi ini setelah setiap aktivitas CRUD

        # Ambil data jadwal dari database atau tempat penyimpanan lainnya
        jadwal1 = self.get_current_schedule()

        jadwal = {}
        for x in jadwal1:
            jadwal.update(x)

        if jadwal:
            # Hitung selisih waktu antara sekarang dan waktu jadwal
            
            for x,y in jadwal.items():
                print(f"{x} : {y}")

            now = datetime.now()
            scheduled_time = jadwal['waktu']
            time_difference = scheduled_time - now
            print(f'time_diff: {time_difference.total_seconds()}')

            # Hanya jadwalkan notifikasi jika waktu jadwal belum berlalu
            if time_difference.total_seconds() > 0:
                await self.schedule_notification_after(time_difference.total_seconds(), jadwal)
                # pass

    async def schedule_notification_after(self, delay, jadwal):
        # Fungsi untuk menjadwalkan notifikasi setelah sejumlah detik tertentu
        notification_title = "Pemberitahuan Jadwal"
        notification_message = f"Waktunya untuk {jadwal['nama_jadwal']} pada {jadwal['waktu']}"

        # sleep(delay)
        await asyncio.sleep(delay)

        notification.notify(
            title=notification_title,
            message=notification_message,
            timeout=10,
            # toast=True  # Membuat notifikasi sebagai toast (untuk Windows)
        )

        # Setelah menampilkan notifikasi, jadwalkan notifikasi berikutnya
        self.schedule_notification()

    def get_current_schedule(self):
        # Fungsi untuk mendapatkan data jadwal dari database atau penyimpanan lainnya
        # Gantilah ini dengan logika sesuai dengan struktur data Anda
        # Contoh: return {'nama_jadwal': 'Meeting', 'waktu': datetime.combine(datetime.now().date(), time(15, 0))}

        result = db.object_db.get_all_data()
        # a = dict()
        
        # for x in result:
        #     a.update((x['tanggal', ]))

 
        return [
    {
        'nama_jadwal': item['nama_jadwal'],
        'waktu': datetime.combine(datetime.strptime(item['tanggal'], '%Y-%m-%d'), datetime.strptime(item['waktu'], '%H:%M').time())
    } 
    for item in result
]

# Inisialisasi dan menjalankan aplikasi
# object_notification = Notification()
