"""
This script runs the Calculator application using a development server.
"""

from os import environ
from Calculator import app

if _name_ == '_main_':
    #HOST = environ.get('SERVER_HOST', 'localhost')
    #try:
    #    PORT = int(environ.get('SERVER_PORT', '5555'))
    #except ValueError:
    #    PORT = 5555
    #app.run(HOST, PORT)

    app.run(debug=True)