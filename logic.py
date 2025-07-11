import os
import json
from mysql_database import DatabaseCreds, Database
from vars import DATABASE_HOST, DATABASE_PORT, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME


db_creds = DatabaseCreds(DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_PORT)


def get_object(object_type, object_id):
    db = Database(DATABASE_NAME, db_creds)
    try: 
        object = db.get_object_by_id(object_type, object_id, as_dict=True)
    except:
        raise Exception(f"cant find {object_type} with id: {object_id}")
    return object

def create_object(object_type, object):
    db = Database(DATABASE_NAME, db_creds)
    id = db.add_object(object_type, object)
    return id

def update_object(object_type, object_id , object):
    db = Database(DATABASE_NAME, db_creds)
    db.update_object(object_type, object_id, object)

def delete_object(object_type, object_id):
    db = Database(DATABASE_NAME, db_creds)
    db.delete_object(object_type, object_id)

def check_object(object_type):
    is_valid = False
    databases = os.listdir('schemas')
    for database in databases:
        with open(os.path.join('schemas', database), 'r') as f:
            objects = json.loads(f.read())
            for object in objects:
                if object == object_type:
                    is_valid = True
    return is_valid
