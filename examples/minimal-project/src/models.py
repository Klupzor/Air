from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class Status(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


@dataclass
class Task:
    id: int
    title: str
    status: Status = Status.TODO
    created_at: datetime = field(default_factory=datetime.now)
