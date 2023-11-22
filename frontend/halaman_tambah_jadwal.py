from datetime import datetime, timedelta
from flet import *
import flet
from frontend.tampilan_date_picker import format_date_picker
from reference.ref import RefHalamanTambahJadwal as ref
from backend import database as db
from backend.format_time import formatted_time
# from backend.notification import schedule_notification


def view_halaman_tambah_jadwal(page):
    banner(page)
    return [
        AppBar(
            ref=ref.APPBAR,
            # leading=IconButton(
            #     ref=ref.ICONBUTTON_BACK,
            #     icon=icons.ARROW_BACK,
            #     on_click=lambda e: open_banner(e, page)
            # ),
            title=Text("Tambahkan Jadwal Anda")
        ),
        Column(
            ref=ref.COLUMN,
            controls=[
                TextField(
                    ref=ref.TEXTFIELD_NAMA_ACARA,
                    label='Nama Jadwal',
                ),
                Row(
                    controls=[
                        ElevatedButton(
                            ref=ref.ELEVATED_BUTTON_PICK_dATE,
                            text='Pick DATE',
                            icon=icons.CALENDAR_MONTH,
                            on_click=lambda e:show_date_picker(e, page)
                        ),
                    ],
                    ref=ref.ROW_DATE_PICKER,
                ),
                TextField(
                    ref=ref.TEXTFIELD_WAKTU,
                    label='Tambahkan Waktu',
                    hint_text='HH:MM'
                )
            ]
        ),
        FloatingActionButton(
            ref=ref.FLOATING_ACTION_BUTTON,
            text='Tambah',
            on_click=lambda e: tambah_jadwal(e, page),
            data='Nama saya adalah',
            tooltip='Tambah Jadwal',
        ),
        
]
    
def tambah_jadwal(e, page: Page):
    #### DENGAN DATABASE
    id_jadwal = db.object_db.insert_data(
        ref.TEXTFIELD_NAMA_ACARA.current.value,
        ref.DATE_PICKER.current.value,
        formatted_time(ref.TEXTFIELD_WAKTU.current.value)
    )
    print("BERHASIL MEMASUKKAN DATA KE DATABASE")

    # schedule_notification(
    #     ref.TEXTFIELD_NAMA_ACARA.current.value,
    #     ref.DATE_PICKER.current.value,
    #     ref.TEXTFIELD_WAKTU.current.value
    # )
    

    # page.route = '/'
    page.go("/")
    page.update()


def show_date_picker(e, page):
    DatePicker(
        ref=ref.DATE_PICKER,
        first_date=datetime.now(),
        last_date=datetime.now() + timedelta(365),
        on_change=on_change_date_picker
    )

    page.overlay.append(
        ref.DATE_PICKER.current
    )

    page.add(ref.DATE_PICKER.current)

    return ref.DATE_PICKER.current.pick_date()


def on_change_date_picker(e):
    result_format = format_date_picker(ref.DATE_PICKER.current.value)

    if len(ref.ROW_DATE_PICKER.current.controls) < 2:
        ref.ROW_DATE_PICKER.current.controls.append(
            Container(
                content=Text(f"{result_format[0]}, {result_format[1]} {result_format[2]} {result_format[3]}")
            )
        )

        ref.ROW_DATE_PICKER.current.update()       

    else:
        del ref.ROW_DATE_PICKER.current.controls[1]


        ref.ROW_DATE_PICKER.current.controls.append(
            Container(
                content=Text(f"{result_format[0]}, {result_format[1]} {result_format[2]} {result_format[3]}")

            )
        )

        ref.ROW_DATE_PICKER.current.update()

def open_banner(e, page):
    page.banner.open = True
    page.update()

def banner(page):
    page.banner = Banner(
        bgcolor=colors.AMBER_100,
        leading=Icon(icons.WARNING_AMBER_ROUNDED, color=colors.AMBER, size=40),
        content=Text(
            "Oops, Sepertinya Ada Bug! Plis Jangan Repot Kami !!!",
        ),
        actions=[
            TextButton("OK, Saya Mengerti!", on_click=lambda e: close_banner(e, page)),
        ],
    )

def close_banner(e, page):
    page.banner.open = False
    page.update()
