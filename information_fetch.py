from db_helper import db_connection
from pymongo import DESCENDING
import json
from datetime import date

class info_fetch:
    def __init__(self):
        self.db=db_connection()

    def get_general(self):
        today = date.today()
        db = self.db.get_collection("general")
        data=db.find({"date":str(today)},{"_id":0})
        for i in data:
            return json.dumps(i)

    def get_entire_general(self):
        db = self.db.get_collection("general")
        data = db.find({},{"_id": 0})
        json_data=[]
        for i in data:
            json_data.append(i)
        return json.dumps(json_data)


    def get_particular_state(self,state):
        db = self.db.get_collection("state_wise")
        data=db.find({"state":state},{"_id":0})
        for i in data:
            return (json.dumps(i))
        return json.dumps({})

    def get_states(self):
        db=self.db.get_collection("state_wise")
        data=db.find({},{"_id":0}).sort([("confirmed",DESCENDING)])
        json_data=[]
        for i in data:
            json_data.append(i)
        return json.dumps(json_data)




if __name__ == '__main__':
    i=info_fetch()
    i.get_general()