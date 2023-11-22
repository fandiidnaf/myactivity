from datetime import datetime, timedelta
from flet import *
import flet
from frontend.tampilan_date_picker import format_date_picker
from frontend import item_task
from reference.ref import RefHalamanTambahJadwal as ref
from reference.ref import RefItemTask as ref2
from reference.ref import RefEditView as ref3
from backend.func import search_by_id as search
from backend.format_time import formatted_time
from backend import database as db


def view_edit_jadwal(page):
    # jadwal = search_by_id(id_task)
    # print(page.controls)
    print(f'icon : {page.data}')
    # jadwal = search(ref2.ICON_EDIT.current.data)
    jadwal = search(page.data)
    print(f'jadwal: {jadwal}')
    format_jadwal_date = format_date_picker(datetime.strptime(jadwal['tanggal'], '%Y-%m-%d'))
    # page.control.data
    banner(page)

    return [
        AppBar(
            # leading=IconButton(
            #     ref=ref.ICONBUTTON_BACK,
            #     icon=icons.ARROW_BACK,
            #     on_click=lambda e: open_banner(e, page)
            # ),
            title=Text('Edit Jadwal'),
        ),
        Column(
                controls=[
                    TextField(
                        ref=ref3.TEXTFIELD_NAMA_ACARA_EDIT,
                        value=str(jadwal['nama_jadwal']),
                        label='Nama Jadwal'
                    ),
                    Row(
                        ref=ref3.ROW_DATE_PICKER_EDIT,
                        controls=[
                            IconButton(
                                icon=icons.CALENDAR_MONTH,
                                on_click=lambda e:show_date_picker_edit(e, page, jadwal)
                            ),
                            Container(Text(f"{format_jadwal_date[0]}, {format_jadwal_date[1]} {format_jadwal_date[2]} {format_jadwal_date[3]}"))
                        ],
                        # ref=ref.ROW_DATE_PICKER
                    ),
                    TextField(
                        ref=ref3.TEXTFIELD_WAKTU_EDIT,
                        value=str(jadwal['waktu']),
                        label='Waktu Jadwal',
                        hint_text='HH:MM'
                    )
                ]
            ),
            FloatingActionButton(
                tooltip='Edit Jadwal',
                text='Edit',
                on_click=lambda e:edit_jadwal(e, page, jadwal, page.data)
            )

        
    ]

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


def show_date_picker_edit(e, page, jadwal):
    DatePicker(
        ref=ref3.DATE_PICKER,
        current_date=datetime.strptime(jadwal['tanggal'], "%Y-%m-%d"),
        first_date=datetime.now(),
        last_date=datetime.now() + timedelta(365),
        on_change=on_change_date_picker_edit
    )

    page.overlay.append(
        ref3.DATE_PICKER.current
    )

    page.add(ref3.DATE_PICKER.current)

    return ref3.DATE_PICKER.current.pick_date()

def on_change_date_picker_edit(e):
    result_format = format_date_picker(ref3.DATE_PICKER.current.value)

    del ref3.ROW_DATE_PICKER_EDIT.current.controls[1]

    ref3.ROW_DATE_PICKER_EDIT.current.controls.append(
        Container(
            Text(f"{result_format[0]}, {result_format[1]} {result_format[2]} {result_format[3]}")
        )
    )

    ref3.ROW_DATE_PICKER_EDIT.current.update()


def edit_jadwal(e, page, jadwal, id_jadwal):
    if ref3.DATE_PICKER.current is None:
        res_date = datetime.strptime(jadwal['tanggal'], '%Y-%m-%d')
    else:
        res_date = ref3.DATE_PICKER.current.value

    # DENGAN DATABASE
    db.object_db.edit_data(
        # ref2.ICON_EDIT.current.data,
        id_jadwal,
        ref3.TEXTFIELD_NAMA_ACARA_EDIT.current.value,
        ref3.DATE_PICKER.current.value if ref3.DATE_PICKER.current is not None else res_date,
        formatted_time(ref3.TEXTFIELD_WAKTU_EDIT.current.value)
    )

    print("EDIT PAGE BERHASIL")

    # jadwal.nama_acara = ref3.TEXTFIELD_NAMA_ACARA_EDIT.current.value
    # jadwal.date = ref3.DATE_PICKER.current.value if ref3.DATE_PICKER.current is not None else res_date
    # jadwal.waktu = formatted_time(ref3.TEXTFIELD_WAKTU_EDIT.current.value)

    # page.go("/")
    page.route = '/'
    page.update()

    # item_task.show_item_view(page)
