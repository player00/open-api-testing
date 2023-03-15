from dataclasses import dataclass


@dataclass
class Post:
    title: str
    body: str
    userId: int
    id: int = None
