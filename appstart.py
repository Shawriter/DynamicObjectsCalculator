import os
from app import create_app
from config import Config

flask_config = 'development'
app = create_app(flask_config)


@app.shell_context_processor
def make_shell_context():
    return None