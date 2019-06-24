from flask import Flask

import os
from dotenv import load_dotenv
from src.routes.webhook import hook_route


# from src.routes.webhook import hook_route

env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path)
# to see the full request and response objects
# set logging level to DEBUG
import logging

logging.getLogger('flask_assistant').setLevel(logging.DEBUG)

app = Flask(__name__)
app.register_blueprint(hook_route)

if __name__ == "__main__":
    app.run(
        host=os.environ.get("HOST"),
        port=os.environ.get("PORT"),
        debug=True if (os.environ.get("DEBUG") == 'on') else False
    )
