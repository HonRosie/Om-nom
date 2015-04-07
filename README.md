
# Om-nom
Om nom is a web application built using Python and Flask that is a personal life manager of sorts. It helps me track my tasks, and any questions or interesing learnings I come across as I work on my projects.

Jinja templates were used to display the UI, with JavaScript and jQuery used to send requests to the Flask server. The server updated the data, and sent back full HTML sections to swap out as a way of updating the page.

Continuing development for this web application is now under OmnomJS, a React and JavaScript version of the app.


##Instructions to run
To run the trading module:
```console
python run.py
```


##Supported features so far
* Task creation
    * Clicking the 'Add' button. This will create a top level task
    * <kbd>Enter</kbd> from any task. This will create a new task on the same level as the task you were just on.
* Subtask creation (theoretically you can create infinity levels of subtasks)
    * <kbd>Tab</kbd> on any task to subtask
    * <kbd>Shift</kbd>+<kbd>Tab</kbd> to unsubtask something
* Ability to mark tasks done
    * <kbd>Ctrl</kbd>+<kbd>d</kbd>
* Recursive delete
    * Clicking the 'delete' link will delete the task, as well as all it's subtasks


##Known issues
* If a user tries to subtask/subtask the task before pressing 'Enter', the task description will disapper upon subtasking/unsubtasking. Since the user never pressed 'Enter', the task description never gets saved before the task is subtasked/unsubtasked
