from sqlmodel import Field, Session, SQLModel, create_engine, select
from project.schemes.agent import Agent
from project.schemes.terrorist import Terrorist
from project.schemes.report import Report
from project.db.init_db import engine


def delete_session_wrapper(func):

    def inner(key):

        with Session(engine) as session:
            statement = func(key)
            result = session.exec(statement).one()
            session.delete(result)
            session.commit()

    return inner


@delete_session_wrapper
def delete_report_by_report_id(report_id : int):
    return select(Report).where(Report.id == report_id)

