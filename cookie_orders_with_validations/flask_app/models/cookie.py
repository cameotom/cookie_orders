from flask_app.config.mysqlconnection import connectToMySQL

# model the class after the user table from our database
class Cookie:
    def __init__( self , data ):
        self.id = data['id']
        self.type = data['type']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_types(cls):
        query = "SELECT * FROM cookie;"
        results = connectToMySQL('cookie_orders').query_db(query)
        return results
