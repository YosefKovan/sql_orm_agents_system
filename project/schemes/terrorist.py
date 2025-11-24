from sqlmodel import Field, SQLModel
from typing import Optional

class Terrorist(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    terrorist_id : Optional[int]
