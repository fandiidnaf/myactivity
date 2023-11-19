from flet import *
import flet


class RefHalamanUtama:
    APPBAR = Ref[AppBar]()
    CIRCLE_AVATAR = Ref[CircleAvatar]()
    TEXT_FIELD_SEARCH = Ref[TextField]()
    POPUPMENUBUTTON = Ref[PopupMenuButton]()
    POPUPMENUITEM_1 = Ref[PopupMenuItem]()
    POPUPMENUITEM_2 = Ref[PopupMenuItem]()
    POPUPMENUITEM_3 = Ref[PopupMenuItem]()
    # TEXT = Ref[Text]()
    LISTVIEW = Ref[ListView]()
    FLOATING_ACTION_BUTTON = Ref[FloatingActionButton]()


class RefHalamanTambahJadwal:
    APPBAR = Ref[AppBar]()
    ICONBUTTON_BACK = Ref[IconButton]()
    COLUMN = Ref[Column]()
    TEXTFIELD_NAMA_ACARA = Ref[TextField]()
    ROW_DATE_PICKER = Ref[Row]()
    ELEVATED_BUTTON_PICK_dATE = Ref[ElevatedButton]()
    DATE_PICKER = Ref[DatePicker]()
    TEXT_DATE_PICKER = Ref[Text]()
    TEXTFIELD_WAKTU = Ref[TextField]()
    FLOATING_ACTION_BUTTON = Ref[FloatingActionButton]()


class RefEditView:
    ROW_DATE_PICKER_EDIT = Ref[Row]()
    DATE_PICKER = Ref[DatePicker]()
    TEXTFIELD_NAMA_ACARA_EDIT = Ref[TextField]()
    TEXTFIELD_WAKTU_EDIT = Ref[TextField]()


class RefItemTask:
    ICON_EDIT = Ref[IconButton]()
    ALERT_DIALOG_DELETE = Ref[AlertDialog]()
    