from flask import Flask 
from src.routes.routes import *

app = Flask(__name__)

# ruta de productos
app.add_url_rule(routes["index_route"], view_func=routes["index_controller"])
# ruta delete
app.add_url_rule(routes["delete_route"],view_func=routes["delete_controller"])
# ruta update
app.add_url_rule(routes["update_route"],view_func=routes["update_controller"])
#ruta usuarios
app.add_url_rule(routes["user_route"],view_func=routes["user_controller"])
#ruta trolley
app.add_url_rule(routes["trolley_route"],view_func=routes["trolley_controller"])
