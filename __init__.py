from flask import Flask

# Instantiate/Create new Flask object (web server)
app = Flask(__name__)

from WebApp import routes
