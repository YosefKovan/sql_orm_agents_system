from project.schemes.agent import Agent
from sqlmodel import Field, Session, SQLModel, create_engine, select, func


def get_agent_by_agent_id(session : Session, agent_id : str):
    statement = select(Agent).where(Agent.agent_id == agent_id)
    return session.exec(statement).one()

def get_agent_by_name_and_password(session : Session, username : str, password : str):
    statement = select(Agent).where(Agent.name == username and Agent.password == password).limit(1)
    return session.exec(statement).one()

def get_agent_password(session : Session, password : str):
    statement = select(Agent).where(Agent.password == password)
    return session.exec(statement).one()
