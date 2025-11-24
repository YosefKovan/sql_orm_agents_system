from sqlmodel import Field, SQLModel
from typing import Optional
import datetime

class Report(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    agent_id: Optional[int] = Field(default=None, foreign_key="agent.id")
    terrorist_id: Optional[int] = Field(default=None, foreign_key="terrorist.id")
    report : str
    date : datetime.datetime = datetime.datetime.now()



