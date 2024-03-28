import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


class TaskManager:
    def __init__(self):
        try:
            self.client = MongoClient(os.getenv("connection_string"))
            print("Connected to MongoDB successfully!")
        except Exception as e:
            print(f"Failed to connect to MongoDB: {e}")

    def add_task(self, task):
        try:
            db = self.client.get_database(os.getenv("DBNAME"))
            task_collection = db["tasks"]

            # Insert the task into collection
            result = task_collection.insert_one(task)

            # Print acknowledgment message
            print(f"Task added to database: {result.acknowledged}")
        except Exception as e:
            print(f"Failed to add task to database: {e}")

    def update_task(self, task):
        # update task in database
        print("updating task")

    def list_tasks(self):
        # lists tasks from the database
        print("listing tasks from database")

    def delete_task(self, task):
        # delete task from database
        print("delete task")

    def find_task(self, taskName):
        # find task from database
        print(f"finding {taskName}")
