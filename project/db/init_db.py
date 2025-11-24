from sqlmodel import SQLModel, create_engine
from project.schemes.agent import Agent
from project.schemes.terrorist import Terrorist
from project.schemes.report import Report

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()



