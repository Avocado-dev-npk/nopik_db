from .connection import ( get_database )
from .find_event import ( get_event )

def create_event(user_id : str , event_name : str):
    if(get_event(user_id,event_name)):
        return False
    else:
        dbname = get_database()
        db = dbname["events"]
        db.insert_one({"user_id":user_id , "event_name" : event_name})
        return True

if __name__ == "__main__":
    print(create_event("112233" , "112211"))
    print(create_event("112233" , "112rewf1"))