from flask import render_template, request, redirect, url_for
from app import app
import pickle
from action import Action

@app.route('/')
def index():
  return render_template('index.html',
                         title='Home',
                         helloLink='/helloworld',
                         todoLink='/todo')

@app.route('/helloworld')
def hello_world():
    return render_template('helloworld.html',
                          title="HelloWorld")

#adds todos to todoList and saves to file
@app.route('/todo/add', methods=['POST'])
def addTodos():
  task = request.form['addTask']
  if task:
    task = Action(task)
    todoList.append(task)
    print "addddddddddd//////////////////////////"
    print task.description
    if task.subTasks:
      for sub in task.subTasks:
        print sub

    with open('todo', 'wb') as f:
      pickle.dump(todoList, f)
  return redirect(url_for('todos'))

#adds subtask to tasks and saves to file
@app.route('/todo/<int:subTaskId>/addSubTask', methods=['POST'])
def addSubTask(subTaskId):
  subTask = request.form['addSubTask']
  if subTask:
    task = todoList[int(subTaskId)]
    print "subtask//////////////////////////////"
    print index
    print task.description
    task.subTasks.append(subTask)
    for sub in task.subTasks:
      print sub
    print "subtask full list/////////////////"
    for task in todoList:
      print task.description
      for sub in task.subTasks:
        print sub


    with open('todo', 'wb') as f:
      pickle.dump(todoList, f)
  return redirect(url_for('todos'))


#deletes todos when delete is clicked and saves to file
@app.route('/todo/<int:taskId>/delete', methods=['GET'])
def deleteTodo(taskId):
  deleteNum = taskId
  if deleteNum >= 0:
    todoList.pop(int(deleteNum))

    with open('todo', 'wb') as f:
      pickle.dump(todoList, f)
  return redirect(url_for('todos'))

#displays todos from todoList
@app.route('/todo')
def todos():
  for sec in todoList:
    print sec.description
    for sub in sec.subTasks:
      print sub
  return render_template('todo.html',
                         title="Todo",
                         todos=todoList)





#Loads todo from file into todoLIst
def loadTodos():
  #TODO need to account corrupt or missing file

  with open('todo', 'rb') as f:
    todoList = pickle.load(f)
  return todoList

todoList = loadTodos()
