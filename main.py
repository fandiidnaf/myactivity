from flet import *
import flet

from frontend.halaman_utama import view_halaman_utama
from frontend.halaman_tambah_jadwal import view_halaman_tambah_jadwal
from frontend.edit_view import view_edit_jadwal
from frontend.item_task import show_item_view

def main(page: Page):
    page.title = 'myactivity'

    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                route="/",
                # appbar=appbar_root(page),
                # floating_action_button=floating_action_button_root(page),
                controls=view_halaman_utama(page),
            )
        )

        if page.route == "/tambah_jadwal":
            page.views.clear()
            page.views.append(
                View(
                    route="/tambah_jadwal",
                    # appbar=insert_view.appbar_insert_jadwal(page),
                    # floating_action_button=insert_view.floating_action_button_insert_jadwal(page),
                    controls=view_halaman_tambah_jadwal(page)

                )
            )

        elif page.route == "/edit_jadwal":
            page.views.clear()
            page.views.append(
                View(
                    route="/edit_jadwal",
                    # appbar=...,
                    # floating_action_button=...,
                    controls=view_edit_jadwal(page)
                )
            )


        page.update()


    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
        # page.views.clear()
        show_item_view(page)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    page.scroll = ScrollMode.ALWAYS


flet.app(target=main)
