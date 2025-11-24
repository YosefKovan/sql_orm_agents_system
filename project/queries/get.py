from sqlmodel import Field, Session, SQLModel, create_engine, select, func
from project.schemes.agent import Agent
from project.schemes.terrorist import Terrorist
from project.schemes.report import Report


def session_wrapper(func):

    def inner(engine, **kwargs):

        with Session(engine) as session:

            statement = func(kwargs["value"])
            results = session.exec(statement).all()

            for result in results:
                print(result.id)

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
def get_agent_by_primary_key(key : int):
    statement = select(Agent).where(Agent.id == key)
    return statement

def get_dangerous_terrorists_ids():
    select(func.count(Report)).column(Report.terrorist_id).group_by(Report.terrorist_id)


