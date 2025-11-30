import datetime

class Task:
    def __init__(self,id,desc):
        self.id = id
        self.desc = desc
        self.status = "todo"
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()