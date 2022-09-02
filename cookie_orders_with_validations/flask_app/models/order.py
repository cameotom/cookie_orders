from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# model the class after the user table from our database
class Order:
    def __init__( self , data ):
        self.id = data['id']
        self.box_count = data['box_count']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.name = data['name']
        self.type = data['type']

    @staticmethod
    def validate_order(order):
        is_valid = True
        if len(order['name']) < 2:
            flash("Name must be at least 2 characters")
            is_valid = False
        if int(order['box_count']) < 0:
            flash("Number of Boxes must be greater than 0")
            is_valid = False
        return is_valid

    @classmethod
    def get_all_orders(cls):
        query = "SELECT * FROM orders LEFT JOIN cookie ON orders.cookie_id = cookie.id;"
        results = connectToMySQL('cookie_orders').query_db(query)
        return results

    @classmethod
    def create_order(cls, data):
        # data is a dictionary that will be passed into the save method from server.py
        query = "INSERT INTO orders ( name , box_count, cookie_id, created_at, updated_at ) VALUES ( %(name)s , %(box_count)s, %(cookie_id)s, NOW() , NOW() );"
        return connectToMySQL('cookie_orders').query_db(query, data)

    @classmethod
    def get_one_order(cls , data):
        query = "SELECT * FROM orders LEFT JOIN cookie ON orders.cookie_id = cookie.id WHERE orders.id = %(id)s;"
        result = connectToMySQL('cookie_orders').query_db(query, data)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        print("B")
        print(data)
        query = "UPDATE orders SET name = %(name)s , box_count= %(box_count)s, cookie_id = %(cookie_id)s, updated_at = NOW() where id=%(id)s;"
        return connectToMySQL('cookie_orders').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM dojos WHERE id=%(id)s;"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)