# To-Do List Application

This is a simple command-line To-Do List application written in Python. The program allows you to add, edit, delete, and display tasks. The tasks are saved to a text file, so they can be accessed even after closing the application.

## Requirements

Python 3.x

import the `os` module

## How to Use

1. Make sure you have Python 3.x installed on your system.

2. Run the Python script from the command line or your preferred Python development environment.

## Functionality

The application provides the following functionalities:

1. **Add Task**: Allows you to add a new task to the To-Do List.
2. **Edit Task**: Lets you modify an existing task in the To-Do List.
3. **Delete Task**: Enables you to remove a task from the To-Do List.
4. **Display Tasks**: Shows all the tasks currently in the To-Do List.
5. **Quit**: Exits the application.

## How it Works

The To-Do List is stored in a text file called **tasks.txt**. When the application starts, it loads the tasks from the file into a list. As you perform operations (add/edit/delete), the list is updated, and the changes are saved back to the file.

The application will display a simple menu where you can select options to perform various actions on the tasks. The menu will continue to loop until you choose to quit the application.

## Data Persistence

The To-Do List is saved to the **tasks.txt** file when you make changes (add/edit/delete) using the application. This allows you to preserve your tasks even after closing the application.

## Disclaimer

This is a simple demonstration of a To-Do List application and does not include advanced features such as user authentication or task prioritization. It is meant for educational purposes and can be expanded upon to suit your specific needs.
