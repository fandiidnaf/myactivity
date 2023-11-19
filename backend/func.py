from backend.database import list_of_item

def search_by_id(id_task: str):
    for x in list_of_item:
        if x.id == id_task:
            return x
        

def delete_by_id(id_task: str):
    x = search_by_id(id_task)
    # del x
    #### WITH DATABASE
    # object_db.delete_data(id_task)
    ######### ##
    list_of_item.remove(x)
