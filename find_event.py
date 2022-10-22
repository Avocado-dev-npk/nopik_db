from .connection import ( get_database )

def get_events(user_id : str):
    dbname = get_database()
    db = dbname["events"]
    data = db.find({"user_id":user_id})
    if(data):
        datas = []
        for i in data:
            datas.append(i)
        return datas
    else:
        return False
    
def get_event(user_id : str , event_name : str):
    dbname = get_database()
    db = dbname["events"]
    data = db.find_one({"user_id":user_id , "event_name" : event_name})
    if(data):
        return data
    else:
        return False

if __name__ == "__main__":
    print(get_events("112233"))
    