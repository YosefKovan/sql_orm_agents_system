from project.queries.agent_query import *
from fastapi import HTTPException
import json

#this function handles writing the user to the file
def add_user_to_file(user):

    try:
        with open("agents.json", 'r+') as file:

            json_data = json.loads(file.read())

            previous_agents = []


            new_json_data = {
                "current_agent" : {"name" : user.name, "agent_id" : user.agent_id},
                "previous_agents" : previous_agents
            }

            file.write(json.dumps(new_json_data))

    except Exception as e:
        print(e)
        print("Error occurred when adding a file")


#this handles the login to the system
def handle_login(session ,username, password):

    try:

       result = get_agent_by_name_and_password(session, username, password)
       print(result)
       add_user_to_file(result)
       return result

    except Exception as e:
        raise HTTPException(status_code=404, detail="password or username not correct!")