from .connection import ( get_database )
from .find_event import ( get_event )

def delete_event(user_id : str , event_name : str):
    if(get_event(user_id,event_name)):
        dbname = get_database()
        db = dbname["events"]
        element = get_event(user_id,event_name)
        db.delete_one({'_id':element['_id']})
        return True
    else:
        return False

if __name__ == "__main__":
    print(delete_event("112233" , "112211"))
    print(delete_event("112233" , "112rewf1"))