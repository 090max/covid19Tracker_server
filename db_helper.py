from pymongo import MongoClient

#Helps eastablishing the connection with the mongo DB url...
class db_connection:
    def __init__(self):
        self.client = MongoClient("<Enter the conenction URL...>")
        self.db=self.client['covid19']

    def get_collection(self,name):
        if(name=="state_wise"):
            return self.db.state_wise
        elif(name=="general"):
            return self.db.general
