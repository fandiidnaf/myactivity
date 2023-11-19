import flet 
from flet import *
from frontend.item_task import show_item_view
from reference.ref import RefHalamanUtama as ref
from backend import database as db

   
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
    ListView(
        ref=ref.LISTVIEW,
    ) if len(db.list_of_item) != 0 else Container(
        content=Text("Tambahkan Jadwal dengan menekan icon +"), alignment=alignment.center,
    ),
    FloatingActionButton(
        ref=ref.FLOATING_ACTION_BUTTON,
        icon=icons.ADD, 
        on_click=lambda _: page.go('/tambah_jadwal')
    ),
]






# def halaman_utama(page: Page):
#     page.appbar = flet.AppBar(
#         bgcolor='black',
#         leading=Row(
#             [
#                 CircleAvatar(
#                     content=Icon(icons.PEOPLE),
#                     color=colors.BLUE,
#                     bgcolor=colors.WHITE,
#                 ),
#                 Text("Nama Anda", color='white')
#             ]
#         ),
#         leading_width=40,
#         title=Text("SEMUA JADWAL", color='white'),
#         center_title=True,
#         actions=[
#             TextField(
#                 label='Cari jadwal Anda', 
#                 label_style=TextStyle(color='black'),
#                 bgcolor='white',
#                 suffix_icon=icons.SEARCH,
#                 border_radius=100,
#                 height=40,
#             ),
#             PopupMenuButton(
#                 items=[
#                     PopupMenuItem(text='Semua jadwal'),
#                     PopupMenuItem(text='Jadwal sudah dilakukan'),
#                     PopupMenuItem(text='Jadwal belum dilakukan')
#                 ],
#                 icon=icons.FILTER_ALT_OUTLINED
#             )
#         ]
#     )


#     page.floating_action_button = FloatingActionButton(
#         icon=icons.ADD,
#     )
#     page.add(Text("Body!"))

# flet.app(target=halaman_utama)
