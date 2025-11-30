import datetime

class Task:
    def __init__(self, id, desc, status="todo", created_at=None, updated_at=None):
        self.id = id
        self.desc = desc
        self.status = status
        self.created_at = created_at or datetime.datetime.now()
        self.updated_at = updated_at or datetime.datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "desc": self.desc,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def from_dict(data):
        return Task(
            id=data["id"],
            desc=data["desc"],
            status=data["status"],
            created_at=datetime.datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.datetime.fromisoformat(data["updated_at"])
        )