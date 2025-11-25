from sqlmodel import Field, Session, SQLModel, create_engine, select, func
from project.schemes.agent import Agent
from project.schemes.terrorist import Terrorist
from project.schemes.report import Report
from project.db.init_db import engine


def session_wrapper(func):

    def inner(**kwargs):

        with Session(engine) as session:

            statement = func(kwargs["value"])
            results = session.exec(statement).all()

            print(results)

            for result in results:
                print(result)

            return results

    return inner

@session_wrapper
def get_by_terrorist_id(terrorist_id : str):
    statement = select(Terrorist).where(Terrorist.terrorist_id == terrorist_id)
    return statement

@session_wrapper
def get_terrorist_by_primary_key(key : int):
    statement = select(Terrorist).where(Terrorist.id == key)
    return statement

@session_wrapper
def get_agent_by_agent_id(agent_id : str):
    statement = select(Agent).where(Agent.agent_id == agent_id)
    return statement

@session_wrapper
def get_agent_by_name(name : str):
    return select(Agent).where(Agent.name == name)

def get_agent_password(password : str):
    return select(Agent).where(Agent.password == password)


@session_wrapper
def get_agent_by_primary_key(key : int):
    statement = select(Agent).where(Agent.id == key)
    return statement

@session_wrapper
def get_dangerous_terrorists_ids():
    return select(Report.id, func.count()).group_by(Report.terrorist_id)


