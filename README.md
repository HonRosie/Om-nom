# Om-nom
Om nom is a web application that helps me track my tasks, questions and learning and was built using Python and Flask. In this version, tasks can be created with (theoretically infinite) subtasks, marked done, and deleted recursively.

Jinja templates were used to display the UI, with JavaScript and jQuery used to send requests to the Flask server. The server updated the data, and sent back full HTML sections to swap out as a way of updating the page.



##Instructions to run
To run the trading module:
```console
python run.py
```

##Known issues
* If a user tries to subtask/subtask the task before pressing 'Enter', the task description will disapper upon subtasking/unsubtasking. Since the user never pressed 'Enter', the task description never gets saved before the task is subtasked/unsubtasked
