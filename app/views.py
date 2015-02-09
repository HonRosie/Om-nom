from flask import render_template, request, redirect, url_for
from app import app
import pickle

# todoList = [
#   {'task': 'Buy milk',
#    'comment': 'From Trader Joes'
#   },
#   {'task': 'Bake cookies',
#    'comment': 'Snickerdoodles'
#   }
# ]

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

@app.route('/addTodo', methods=['POST'])
def addTodos():
  if request.method == 'POST':           #is this necessary?
    todo = request.form['addTask']
    if todo:
      task = {'task': todo}
      todoList.append(task)

      with open('todo', 'wb') as f:
        pickle.dump(todoList, f)
  return redirect(url_for('todos'))


@app.route('/deleteTodo', methods=['GET'])
def deleteTodo():

  print "Hello"
  deleteNum = request.args.get('indexOfTodo')
  if deleteNum:
    todoList.pop(int(deleteNum))

    with open('todo', 'wb') as f:
      pickle.dump(todoList, f)
  return redirect(url_for('todos'))


@app.route('/todo')
def todos():
  return render_template('todo.html',
                         title="Todo",
                         todos=todoList)

def loadTodos():
  with open('todo', 'rb') as f:
    todoList = pickle.load(f)
  return todoList

todoList = loadTodos()
