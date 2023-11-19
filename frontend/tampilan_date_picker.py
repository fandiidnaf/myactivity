from datetime import datetime

def format_date_picker(tanggal: datetime) -> list:
    '''
    Return
    ======
    0.  `nama_hari`     :   `kamis`
    1.  `tanggal`       :   `10`
    2.  `nama_bulan`    :   `July`
    3.  `Tahun`         :   `2023`
    5.  `bulan`        :   `7`
    '''
    month_dict = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    nama_hari = tanggal.strftime('%A')
    nama_bulan = month_dict[tanggal.month]

    return [
        nama_hari,  # kamis
        tanggal.day,    # 20
        nama_bulan, # juli
        tanggal.year,    # 2023
        tanggal.month   # 7
    ]
