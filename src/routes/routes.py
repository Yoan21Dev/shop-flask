from src.controllers.controller import *

routes  = {
    #productos
    "index_route": "/", "index_controller": indexController.as_view("index"),
    "delete_route": "/delete/product/<int:id>","delete_controller": DeleteController.as_view("delete"),
    "update_route": "/update/product/<int:id>","update_controller": UpdateController.as_view("update"),
    #usuarios
    "user_route": "/user","user_controller": UserController.as_view("user"), 
    #carrito
    "trolley_route":"/trolley","trolley_controller": TrolleyController.as_view("trolley")
} 