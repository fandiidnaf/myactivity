from flet import *
import flet
from frontend.halaman_utama import view_halaman_utama
from frontend.halaman_tambah_jadwal import view_halaman_tambah_jadwal
from frontend.edit_view import view_edit_jadwal


def main(page: Page):
    page.title = 'myactivity'

    def route_change(routes):
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=view_halaman_utama(page),
            )
        )
        page.update()


        if page.route == "/tambah_jadwal":
            # page.views.clear()
            page.views.append(
                View(
                    route="/tambah_jadwal",
                    controls=view_halaman_tambah_jadwal(page)

                )
            )
            page.update()

        elif page.route == "/edit_jadwal":
            page.views.append(
                View(
                    route="/edit_jadwal",
                    controls=view_edit_jadwal(page)
                )
            )
            page.update()


        page.update()


    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        # page.go(top_view.route)
        page.go('/')
        # page.views.clear()
        # show_item_view(page)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go('/')
    page.scroll = ScrollMode.ALWAYS

    page.update()


flet.app(
    target=main,
)
