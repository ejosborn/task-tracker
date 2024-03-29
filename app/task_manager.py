import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv

load_dotenv()


class TaskManager:
    def __init__(self):
        try:
            self.client = MongoClient(os.getenv("connection_string"))
        except Exception as e:
            print(f"Failed to connect to database: {e}")

    def add_task(self, task):
        try:
            db = self.client.get_database(os.getenv("DBNAME"))
            task_collection = db["tasks"]

            # Insert the task into collection
            task_collection.insert_one(task)

            # Print acknowledgment message
            print("\nTask added to database")
        except Exception as e:
            print(f"Failed to add task to database: {e}")

    def update_task(self, task):
        # update task in database
        print("updating task")

    def list_tasks(self):
        try:
            db = self.client.get_database(os.getenv("DBNAME"))
            task_collection = db["tasks"]

            # queries db for all tasks
            tasks = task_collection.find({})

            taskNum = 1
            # lists tasks from the database
            for task in tasks:
                print(f"\nTask {taskNum}:")
                print(f"ID: {task['_id']}")
                print(f"Title: {task['title']}")
                print(f"Description: {task['description']}")
                print(f"Priority: {task['priority']}")
                print(f"Status: {task['status']}")
                taskNum += 1
        except Exception as e:
            print(f"Failed to list tasks from database: {e}")

    def delete_task(self, taskId):
        try:
            db = self.client.get_database(os.getenv("DBNAME"))
            task_collection = db["tasks"]

            deleteTask = task_collection.delete_one({"_id": taskId})

            if deleteTask.deleted_count > 0:
                # delete task from database
                print(f"\nDeleted task: {taskId}")
            else:
                print(f"\nFailed to find task: {taskId}")
        except Exception as e:
            print(f"\nFailed to delete task {taskId}: {e}")

    def to_ObjectID(self, taskID_string):
        task_id = ObjectId(taskID_string)
        return task_id
