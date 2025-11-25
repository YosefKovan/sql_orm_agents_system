import uvicorn
from backend.routes import app
from project.db.init_db import create_db_and_tables
from project.queries.create import *


if __name__ == "__main__":
    create_db_and_tables()
    #create_agent(name="yossi kovan", agent_id="123456789", password="1")
    uvicorn.run(app, host='localhost', port=8500)





