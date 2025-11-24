from sqlmodel import Session
from project.db.init_db import engine
from project.schemes.agent import Agent
from project.schemes.terrorist import Terrorist
from project.schemes.report import Report



def session_wrapper(func):
    """this decorator will allow reuse of code no need to duplicate"""
    def inner(**kwargs):

        with Session(engine) as session:

            results = func(kwargs)

            for obj in results:
                session.add(obj)

            session.commit()

    return inner


@session_wrapper
def create_agent(data)->list[Agent]:
    return [Agent(name=data["name"], agent_id=data["agent_id"], password=data["password"])]


@session_wrapper
def create_terrorist(data)->list[Terrorist]:
    return [Terrorist(name=data["name"], terrorist_id=data["terrorist_id"])]


@session_wrapper
def create_report(data)->list[Report]:
    return [Report(terrorist_id=data["terrorist_id"], agent_id=data["agent_id"], report=data["report"])]





