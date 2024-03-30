from datetime import datetime


class Task:
    def __init__(self, title, description, priority, status):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.created_at = datetime.utcnow()

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "created_at": self.created_at,
        }
