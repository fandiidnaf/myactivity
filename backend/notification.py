from plyer import notification
from datetime import datetime, timedelta
import time

def schedule_notification(task, tanggal ,scheduled_time):
    # Mendapatkan tanggal dan waktu saat ini
    now = datetime.now()
    # print(now.date())

    print(f'type tanggal : {type(tanggal)}')
    print(f'tanggal : {tanggal}')

    diff_tanggal = (tanggal.date() - now.date()).days
    print(f'diff_tanggal {diff_tanggal}')

    if diff_tanggal < 0:
        diff_tanggal = 0

    # diff_tanggal = max(diff_tanggal, 0)

    # Membaca jam dan menit dari input pengguna
    scheduled_hour, scheduled_minute = map(int, scheduled_time.split(':'))

    # Membuat objek datetime untuk waktu yang dijadwalkan besok
    # scheduled_datetime = datetime(now.year, now.month, now.day, scheduled_hour, scheduled_minute) + timedelta(days=1)
    scheduled_datetime = datetime(now.year, now.month, now.day, scheduled_hour, scheduled_minute) + timedelta(days=diff_tanggal)

    print(f'scheduled_datetime : {scheduled_datetime}')

    # Hitung selisih waktu antara waktu saat ini dan waktu yang dijadwalkan
    time_difference = scheduled_datetime - now

    print(f'time_difference : {time_difference}')

    # Konversi selisih waktu ke detik
    time_in_seconds = time_difference.total_seconds()

    print(f'tim_in_seconds : {time_in_seconds}')
    # Tunggu sampai waktu yang dijadwalkan
    time.sleep(time_in_seconds)

    # Munculkan notifikasi
    notification.notify(
        title='Notifikasi Jadwal',
        message=f'Waktunya untuk: {task}',
        app_icon=None,  # e.g. 'C:\\icon_32x32.ico'
        timeout=10,  # seconds
    )

# Contoh penggunaan:
# task_name = input("Masukkan nama tugas: ")
# scheduled_time = input("Masukkan waktu (HH:MM): ")

# schedule_notification(task_name, scheduled_time)
