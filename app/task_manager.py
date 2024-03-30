import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv

load_dotenv()


class TaskManager:
    def __init__(self):
        try:
            self.client = MongoClient(os.getenv("conn_string"))
        except Exception as e:
            print(f"Failed to connect to database: {e}\n")
            exit()

    def add_task(self, task):
        try:
            db = self.client.get_database(os.getenv("DBNAME"))
            task_collection = db["tasks"]

            # Insert the task into collection
            task_collection.insert_one(task)

            # Print acknowledgment message
            return print("\nTask added to database")
        except Exception as e:
            return print(f"\nFailed to add task to database: {e}")

    def update_task(self, taskId):
        try:
            db = self.client.get_database(os.getenv("DBNAME"))
            task_collection = db["tasks"]

            task = task_collection.find_one({"_id": taskId})

            if task:
                newTitle = input("\nInput new title: \n")
                newDescription = input("\nInput new description: \n")
                newPriority = input("\nInput new priority: \n")
                newStatus = input("\nInput new status: \n")

                updatedFields = {
                    "$set": {
                        "title": newTitle,
                        "description": newDescription,
                        "priority": newPriority,
                        "status": newStatus,
                    }
                }

                updateTask = task_collection.update_one({"_id": taskId}, updatedFields)

                if updateTask.modified_count > 0:
                    return print("\nTask updated...")
            else:
                return print(f"\nTask not found.")

        except Exception as e:
            return print(f"\nFailed to update task: {taskId}")

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

            return
        except Exception as e:
            return print(f"\nFailed to list tasks from database: {e}")

    def delete_task(self, taskId):
        try:
            db = self.client.get_database(os.getenv("DBNAME"))
            task_collection = db["tasks"]

            deleteTask = task_collection.delete_one({"_id": taskId})

            if deleteTask.deleted_count > 0:
                # delete task from database
                return print(f"\nDeleted task: {taskId}")
            else:
                return print(f"\nFailed to find task: {taskId}")
        except Exception as e:
            return print(f"\nFailed to delete task {taskId}: {e}")

    def to_ObjectID(self, taskID_string):
        try:
            task_id = ObjectId(taskID_string)
            return task_id
        except Exception as e:
            return print(f"Not valid ObjectId: {e}")
