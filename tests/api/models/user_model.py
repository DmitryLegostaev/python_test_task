from dataclasses import dataclass


@dataclass
class CreatedUser:
    name: str
    job: str
    id: str
    createdAt: str


@dataclass
class ExistingUser:
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


@dataclass
class UpdatedUser:
    name: str
    job: str
    updatedAt: str
