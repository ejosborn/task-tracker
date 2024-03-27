import unittest
from unittest.mock import patch
from io import StringIO
import sys
from cli.commands import addTask, updateTask, deleteTask, helpCommand, exitCommand


# testing cli commands to make sure they are working correctly
class TestCommands(unittest.TestCase):
    # add command
    @patch("sys.stdout", new_callable=StringIO)
    def test_add_task(self, mock_stdout):
        addTask()
        self.assertEqual(mock_stdout.getvalue().strip(), "Add a Task")

    # update command
    @patch("sys.stdout", new_callable=StringIO)
    def test_update_task(self, mock_stdout):
        updateTask()
        self.assertEqual(mock_stdout.getvalue().strip(), "Update a task")

    # delete command
    @patch("sys.stdout", new_callable=StringIO)
    def test_delete_task(self, mock_stdout):
        deleteTask()
        self.assertEqual(mock_stdout.getvalue().strip(), "Delete a task")

    # help command
    @patch("sys.stdout", new_callable=StringIO)
    def test_help_command(self, mock_stdout):
        helpCommand()
        expected_output = """Here are the commands you can use:
help	 -    Displays Commands
add	 -    Add a task to the list
update	 -    Update a task
delete	 -    Delete a task from the list
exit	 -    Exit the program"""
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    # exit command
    @patch("sys.stdout", new_callable=StringIO)
    def test_exit_command(self, mock_stdout):
        with self.assertRaises(SystemExit) as cm:
            exitCommand()
        self.assertEqual(cm.exception.code, None)
        self.assertEqual(mock_stdout.getvalue().strip(), "Exiting Task Manager ...")


if __name__ == "__main__":
    unittest.main()
