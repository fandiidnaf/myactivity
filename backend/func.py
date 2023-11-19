from backend.database import list_of_item
# from myactivity.model.jadwal import Jadwal
# from myactivity.reference.ref import RefEditView as ref
# from myactivity.frontend.edit_view import edit_view

def search_by_id(id_task: str):
    for x in list_of_item:
        if x.id == id_task:
            return x
        

def delete_by_id(id_task: str):
    x = search_by_id(id_task)
    # del x
    list_of_item.remove(x)


# def open_dialog_view_edit(e, page, id_task):

#     result_jadwal = search_by_id(id_task)
#     obj = edit_view(result_jadwal)

#     page.dialog = obj
#     obj.open = True
#     page.update()