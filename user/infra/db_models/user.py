from dataclasses import dataclass


@dataclass
class User:
    id: str
    name: str
    email: str
    password: str
    created_at: str
    updated_at: str