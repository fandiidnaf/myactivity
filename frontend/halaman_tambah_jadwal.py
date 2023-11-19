from datetime import datetime, timedelta
import flet
from flet import *
from model.jadwal import Jadwal
from backend import database as db
from backend.format_time import formatted_time
from reference.ref import RefHalamanTambahJadwal as ref
from frontend import item_task
from frontend.tampilan_date_picker import format_date_picker
from backend.notification import schedule_notification



def view_halaman_tambah_jadwal(page):
    return [
        AppBar(
            ref=ref.APPBAR,
            title=Text("Tambahkan Jadwal Anda")
        ),
        Column(
            ref=ref.COLUMN,
            controls=[
                TextField(
                    ref=ref.TEXTFIELD_NAMA_ACARA,
                    label='Nama Acara',
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
            text='Setel',
            # on_click=lambda _:page.go('/'),
            on_click=lambda e: tambah_jadwal(e, page),
            data='Nama saya adalah',
        ),
        
]
    
def tambah_jadwal(e, page):
    db.list_of_item.append(
        Jadwal(
            db.generate_unique_id(),
            ref.TEXTFIELD_NAMA_ACARA.current.value,
            ref.DATE_PICKER.current.value,
            formatted_time(ref.TEXTFIELD_WAKTU.current.value)
        )
    )

    page.go("/")

    item_task.show_item_view(page)

    schedule_notification(
        ref.TEXTFIELD_NAMA_ACARA.current.value,
        ref.DATE_PICKER.current.value,
        ref.TEXTFIELD_WAKTU.current.value
    )
    print(db.list_of_item)

    for x in db.list_of_item:
        print(x.waktu)

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
