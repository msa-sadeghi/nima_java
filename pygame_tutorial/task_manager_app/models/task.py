from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


class Priority:
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

    ALL = [LOW, MEDIUM, HIGH]


class Status:
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"

    ALL = [TODO, IN_PROGRESS, DONE]


@dataclass
class Task:
    title: str
    description: str = ""
    priority: str = Priority.MEDIUM
    status: str = Status.TODO
    due_date: Optional[str] = None

    id: Optional[int] = field(default=None)
    create_at: Optional[datetime] = field(default_factory=datetime.now)

    def is_done(self):
        return self.status == Status.DONE

    def is_overdue(self):
        if self.due_date is None:
            return False
        if self.is_done():
            return False

        due = datetime.strptime(self.due_date, "%Y-%m-%d")
        return datetime.now() > due

    def mark_done(self):
        self.status = Status.DONE

    def mark_in_progress(self):
        self.status = Status.IN_PROGRESS

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "due_date": self.due_date,
            "created_at": self.create_at.strftime("%Y-%m-%d %H:%M:%S"),
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            title=data.get("title"),
            description=data.get("description"),
            priority=data.get("priority"),
            status=data.get("status"),
            due_date=data.get("due_date"),
            created_at=data.get("created_at"),
        )
