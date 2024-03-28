import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

dbName = os.getenv("DBNAME")
dbPort = os.getenv("DBPORT")


def __init__(self, db_name=dbName, host="localhost", port=dbPort):
    self.client = MongoClient(host, port)
    self.db = self.client[db_name]
    self.task_collection = self.db["tasks"]


def add_task(self, task):
    # add task to database
    print("adding to database")


def update_task(self, task):
    # update task in database
    print("updating task")


def delete_task(self, task):
    # delete task from database
    print("delete task")


def list_tasks(self):
    # lists tasks from the database
    print("listing tasks from database")
