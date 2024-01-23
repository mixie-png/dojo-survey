from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    DB = "dojo_survey_schema"
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # READ
    # show one record
    @classmethod
    def show_one(cls, id):
        query = """SELECT * FROM dojos WHERE id = %(id)s;"""
        result = connectToMySQL(cls.DB).query_db(query, {"id" : id})

        # Check if result is not empty before accessing the first element
        if result:
            one_survey = cls(result[0])
            return one_survey
        else:
            return None  # or handle the case where the dojo with the given id is not found

    # CREATE
    @classmethod
    def add(cls, data):
        query = """
            INSERT INTO dojos (name, location, language, comment)
    	    VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result

    #VALIDATE
    @staticmethod
    def validate_survey(survey):
        is_valid = True
        if len(survey['name']) < 3:
            flash("Name must be at least 3 characters")
            is_valid = False
        if len(survey['location']) < 1:
            flash("Must choose a location")
            is_valid = False
        if len(survey['language']) < 1:
            flash("Must choose a language")
            is_valid = False
        if len(survey['comment']) < 3:
            flash("Comment must be at least 3 characters")
            is_valid = False
        return is_valid