from backend.database import list_of_item, object_db

def search_by_id(id_task: str):
    # for x in list_of_item:
    #     if x.id == id_task:
    #         return x
        
    for x in object_db.get_all_data():
        if x['id'] == id_task:
            return x
        