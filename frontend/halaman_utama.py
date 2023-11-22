import asyncio
from flet import *
import flet 
from reference.ref import RefHalamanUtama as ref
from frontend.item_task import ItemTask
from backend import database as db
from datetime import datetime
from backend.notification import Notification
# from frontend.item_task import show_item_view     ## SEHARUSNYA DENGAN DATABASE IMPORT INI

   
def view_halaman_utama(page):
    return [
        AppBar(
        ref=ref.APPBAR,
        bgcolor='black',
        leading=Row(
            [
                Divider(),
                CircleAvatar(
                    ref=ref.CIRCLE_AVATAR,
                    content=Icon(icons.PEOPLE),
                    color=colors.BLUE,
                    bgcolor=colors.WHITE,
                ),
                Text("Nama Anda", color='white')
            ]
        ),
        # leading_width=40*page.width / 100,
        title=Text("SEMUA JADWAL", color='white'),
        center_title=True,
        actions=[
            TextField(
                ref=ref.TEXT_FIELD_SEARCH,
                label='Cari jadwal Anda', 
                label_style=TextStyle(color='black'),
                bgcolor='white',
                suffix_icon=icons.SEARCH,
                border_radius=100,
                height=40,
            ),
            PopupMenuButton(
                ref=ref.POPUPMENUBUTTON,
                items=[
                    PopupMenuItem(
                        ref=ref.POPUPMENUITEM_1,
                        text='Semua jadwal'),
                    PopupMenuItem(
                        ref=ref.POPUPMENUITEM_2,
                        text='Jadwal sudah dilakukan'),
                    PopupMenuItem(
                        ref=ref.POPUPMENUITEM_3,
                        text='Jadwal belum dilakukan')
                ],
                icon=icons.MENU
            ),
        ]
    ),
    # Text(ref=ref.TEXT,value='Halo'),
    # ListView(           ## refresh_halaman_utama
    #     ref=ref.LISTVIEW,
    #     auto_scroll=True,
    # ) if len(db.list_of_item) != 0 else Container(
    #     content=Text("Tambahkan Jadwal dengan menekan icon +"), alignment=alignment.center,
    # ),
    # refresh_halaman_utama(page),
    refresh_halaman_utama(page),
    FloatingActionButton(
        ref=ref.FLOATING_ACTION_BUTTON,
        icon=icons.ADD, 
        on_click=lambda e: route_to_tambah_jadwal(e, page),
        tooltip='Tambah Jadwal Anda'
    ),
]


def route_to_tambah_jadwal(e, page: Page):
    # page.route = '/tambah_jadwal'
    page.go("/tambah_jadwal")
    page.update()

def refresh_halaman_utama(page):
    result = db.object_db.get_all_data()

    # for x in result:
    #     print(x['id'])

    if len(result) > 0:
        # asyncio.run(Notification().schedule_notification())

        return ListView(
            ref=ref.LISTVIEW,
            auto_scroll=True,
            controls=[ItemTask(x['nama_jadwal'], x['waktu'], x['id'], datetime.strptime(x['tanggal'], '%Y-%m-%d'), page) for x in result]
        )
    
    
        
    else:
        return Text(
            value='OOPS SEPERTINYA DAFTAR ANDA MASIH KOSONG\nKLIK ICON + DI BAWAH'
        )


