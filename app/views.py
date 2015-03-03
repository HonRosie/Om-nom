import pickle
import uuid
from flask import render_template, request, redirect, url_for
from app import app
from action import Action
import os.path

taskDict = {}

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

def writeToFile():
  with open('todo', 'wb') as f:
    pickle.dump(taskDict, f)

def createTask(description, parentId, insertLoc):
  newTask = Action(description)
  newTask.parentId = parentId
  newTaskId = str(uuid.uuid4())
  if insertLoc:
    taskDict[parentId].subTasksId.insert(insertLoc, newTaskId)
  else:
    taskDict[parentId].subTasksId.append(newTaskId)
  taskDict[newTaskId] = newTask

#adds todos to taskDict and saves to file
@app.route('/todo/<taskId>/edit', methods=['POST'])
def editTodos(taskId):
  task = request.form['editTask']
  existingTask = taskDict[taskId]
  existingTask.description = task
  taskOrder = taskDict[rootTaskId].subTasksId.index(taskId)

  createNew = request.form['createNew']
  if createNew == "true":
    createTask("", rootTaskId, taskOrder + 1)

  writeToFile()

  print "////////////////////Task Dict///////////////"
  for taskId in taskDict:
    print taskId + ":" + taskDict[taskId].description
    print taskDict[taskId].subTasksId

  taskIdList = taskDict[rootTaskId].subTasksId
  return render_template('taskList.html',
                         title="Todo",
                         taskDict = taskDict,
                         taskIdList = taskIdList
                        )


#adds todos to taskDict and saves to file
@app.route('/todo/add', methods=['POST'])
def addTodos():
  task = request.form['addTask']
  addTaskToDict(task, rootTaskId)
  return redirect(url_for('todos'))


#adds subtask to tasks and saves to file
@app.route('/todo/<parentId>/addSubTask', methods=['POST'])
def addSubTask(parentId):
  task = request.form['addSubTask']
  addTaskToDict(task, parentId)
  return redirect(url_for('todos'))


def addTaskToDict(task, parentId):
  taskIdUnique = True
  taskId = None
  #if there was something in the add task form field
  if task:
    while taskIdUnique:
      task = Action(task)
      task.parentId = parentId
      taskId = str(uuid.uuid4())

      #if the task does not already exist in taskDict
      if taskId not in taskDict:
        taskDict[taskId] = task
        taskDict[parentId].subTasksId.append(taskId)
        taskIdUnique = False

    with open('todo', 'wb') as f:
      pickle.dump(taskDict, f)

#add comment to task and saves to file
@app.route('/todo/<taskId>/addComment', methods=['POST'])
def addComment(taskId):
  comment = request.form['addComment']
  if comment:
    task = taskDict[taskId]
    task.comment.append(comment)
    with open('todo', 'wb') as f:
      pickle.dump(taskDict, f)
  return redirect(url_for('todos'))

#deletes todos when delete is clicked and saves to file
@app.route('/todo/<taskId>/delete', methods=['GET'])
def deleteTodo(taskId):
  parentId = taskDict[taskId].parentId
  taskDict[parentId].subTasksId.remove(taskId)

  delete(taskId)

  with open('todo', 'wb') as f:
    pickle.dump(taskDict, f)
  return redirect(url_for('todos'))

def delete(taskId):
  subTasksIds = taskDict[taskId].subTasksId
  if subTasksIds:
    for subId in subTasksIds:
      delete(subId)

  taskDict.pop(taskId)


#displays todos from taskDict
@app.route('/todo')
def todos():
  print "////////////////////Task Dict///////////////"
  for taskId in taskDict:
    print taskId + ":" + taskDict[taskId].description
    print taskDict[taskId].subTasksId

  taskIdList = taskDict[rootTaskId].subTasksId
  return render_template('todo.html',
                         title="Todo",
                         taskDict = taskDict,
                         taskIdList = taskIdList
                        )


#Loads todo from file into todoList
def loadTodos():
  global taskDict
  rootTaskId=""

  #create taskDict with root node
  if not os.path.isfile('todo'):
    task = Action("root")
    rootTaskId = str(uuid.uuid4())
    taskDict[rootTaskId] = task

    #first subTask
    createTask("", rootTaskId, None)

    with open('todo', 'wb') as f:
      pickle.dump(taskDict, f)
  with open('todo', 'rb') as f:
    taskDict = pickle.load(f)
  for taskId, task in taskDict.iteritems():
    if task.description == "root":
      rootTaskId = taskId

  return rootTaskId

rootTaskId = loadTodos()
