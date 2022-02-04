from ast import Delete
from os import name
from typing import Text, TextIO
from flask import json, request, render_template,redirect,flash,jsonify
from flask.views import MethodView
from pymysql.cursors import DictCursor
from werkzeug.exceptions import PreconditionFailed



from src.db import mysql


class indexController(MethodView):
    def get (self):
     
        with mysql.cursor (DictCursor) as cur:
            print("success")
            cur.execute ("SELECT * FROM productos")
            data = cur.fetchall()
            print (data)     
            print("holap")
            return jsonify (data)
    
    def post(self): 

        products = request.get_json() or {}
    


        img_url = products.get('img_url', False)
        caracteristicas = products.get('caracteristicas', False)
        precios = products.get('precios', False)
        nombre = products.get ('name',False)
        
        # if products:
        #     if 'img_url' in products:
        #         img_url = products ['img_url']

        with mysql.cursor() as cur:
            try:
               cur.execute("insert into productos(img_url, precios, caracteristicas, nombre) values(%s,%s,%s,%s)",
                            (img_url, precios, caracteristicas, nombre))
               cur.connection.commit()
            except: 
                print ["error"]
        print(products)
        return jsonify (products)

class DeleteController(MethodView):
    def delete(self,id):
      with mysql.cursor() as cur:
            try:
                cur.execute("delete from productos where id =%s",(id,))
                cur.connection.commit()
                print("el producto se elimino correctamente",'success')
            except:
                print("error")
            return ("se borro correctamente")

class UpdateController(MethodView):
    def get(self,id):
        with mysql.cursor(DictCursor) as cur:
            try:            
                cur.execute("SELECT * FROM productos WHERE id = %s", (id,))
                cur.connection.commit()
                productos = cur.fetchone()
            except:
                print("error")    
            return jsonify (productos)
    
    def patch(self, id):
        products = request.get_json() or {}

        img_url = products.get('img_url',False)
        caracteristicas = products.get('caracteristicas',False)
        precios = products.get('precios',False)
        nombre = products.get('category',False)

        with mysql.cursor() as cur:
            try:
                cur.execute("UPDATE productos SET img_url = %s, caracteristicas = %s, precios = %s, nombre = %s WHERE id = %s",
                             (img_url, caracteristicas, precios, nombre, id))
                cur.connection.commit()
                print(["El producto se ha actualizado", 'success'])
            except:
                print (['Un error ha ocurrido al actualizar el producto', 'error'])
            finally:
                cur.close()
        return jsonify (products)

class UserController(MethodView):
    def get(self):
        with mysql.cursor (DictCursor) as cur:
            print("success")
            cur.execute ("SELECT * FROM customer")
            data_user = cur.fetchall()  
            print (data_user)     
            print(["user"])
            return jsonify (data_user)

    def post(self):
        user = request.get_json() or {} 
        nombre = user.get('nombre',False)
        # id = user.get('id',False)
        with mysql.cursor() as cur:
            try:
               cur.execute("insert into customer (nombre) values(%s)",
                            (nombre))
               cur.connection.commit()
               print(["fue agregado correctamente"])
            except: 
                print (["error"])
        return (nombre)

# class DeleteController(MethodView):        
    
    def delete (self):     
        id_delete = request.get_json() or {}
        id = id_delete.get('id')
        with mysql.cursor() as cur:
            try:
                cur.execute("delete from customer where id =%s",(id,))
                cur.connection.commit()
                print("el producto se elimino correctamente",'success')
            except:
                print("error")
            return (id_delete)
#update            
    def patch (self):
        update = request.get_json() or {}
        id = update.get('id')
        nombre = update.get('nombre')
        with mysql.cursor() as cur:
            try:
                cur.execute("UPDATE customer SET nombre = %s WHERE id = %s",
                             (nombre, id))
                cur.connection.commit()
                print(["El producto se ha actualizado", 'success'])
            except:
                print (['Un error ha ocurrido al actualizar el producto', 'error'])
            finally:
                cur.close()
        return jsonify (nombre)

 #carrito
class TrolleyController(MethodView):
    def get (self): 
        with mysql.cursor (DictCursor) as cur:
            print("success")
            cur.execute ("SELECT * FROM carrito")
            data = cur.fetchall()
            print (data)     
            print("holap")
            return jsonify (data)


    def post(self): 
        shop = request.get_json() or {}
        productos_id = shop.get('productos_id', False)
        customer_id= shop.get('customer_id', False)
        with mysql.cursor() as cur:
            try:
               cur.execute("insert into carrito(productos_id, customer_id) values(%s,%s)",
                            (productos_id,customer_id)) 
               cur.connection.commit()
               print(["agregado al carrito"])
            except: 
                print (["error"])     
        return jsonify (["succes"])
       
    def delete(self):
        id_delete = request.get_json() or {}
        id = id_delete.get('id',False)
        with mysql.cursor() as cur:
            try:
                cur.execute("delete from carrito where id = %s",(id,))
                cur.connection.commit()
                print("el producto se elimino correctamente",'success')
            except:
                print("error")
            return jsonify(id_delete)
        