# import asyncio
from datetime import datetime
from flet import *
import flet 
from frontend.item_task import ItemTask
from reference.ref import RefHalamanUtama as ref
from backend import database as db
# from backend.notification import Notification

   
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
                Text("My Activity", color='white')
            ]
        ),
        # leading_width=40*page.width / 100,
        title=Text("SEMUA JADWAL", color='white'),
        center_title=True,
        actions=[
            # TextField(
            #     ref=ref.TEXT_FIELD_SEARCH,
            #     label='Cari jadwal Anda', 
            #     label_style=TextStyle(color='black'),
            #     bgcolor='white',
            #     suffix_icon=icons.SEARCH,
            #     border_radius=100,
            #     height=40,
            # ),
            PopupMenuButton(
                ref=ref.POPUPMENUBUTTON,
                items=[
                    PopupMenuItem(
                        ref=ref.POPUPMENUITEM_2,
                        text='Terbaru -> Terlama'),
                    PopupMenuItem(
                        ref=ref.POPUPMENUITEM_3,
                        text='Terlama -> Terbaru',
                        checked=False,
                        # on_click=lambda e: show_jadwal_terlama_ke_terbaru(e, page)
                    )
                ],
                icon=icons.MENU
            ),
        ]
    ),
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



    if len(result) > 0:
        # asyncio.run(Notification().schedule_notification())
        
        return ListView(
            ref=ref.LISTVIEW,
            auto_scroll=True,
            controls=[ItemTask(x['nama_jadwal'], x['waktu'], x['id'], datetime.strptime(x['tanggal'], '%Y-%m-%d'), page) for x in result]
        )
    
        
    else:
        return Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    vertical_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Text(
                            value='OOPS SEPERTINYA DAFTAR JADWAL ANDA MASIH KOSONG\nKLIK ICON + DI BAWAH',
                            weight=FontWeight.BOLD
                        )
                    ]
                )
            ]
        )
    