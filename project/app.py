from project.db.init_db import create_db_and_tables, engine
from project.queries.create import *
from project.queries.get import *
from project.queries.delete import *




def main():

    #this will create the tables
    create_db_and_tables()

    #this will creat the agent
    create_agent(name="yossi kovan", agent_id="123456789", password="1")
    # create_terrorist(name="mohamad", terrorist_id="123456789")
    # create_report(agent_id = 1, terrorist_id = 1, report = "hello")
    # create_report(agent_id=1, terrorist_id=1, report="world")
    # create_report(agent_id=1, terrorist_id=1, report="world")
    # create_report(agent_id=1, terrorist_id=1, report="world")
    # create_report(agent_id=1, terrorist_id=1, report="world")
    # create_report(agent_id=1, terrorist_id=1, report="world")



    delete_report_by_report_id(2)

    get_dangerous_terrorists_ids()








