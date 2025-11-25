from sqlmodel import Field, SQLModel
from typing import Optional

class Agent(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    agent_id: str
    password: str
