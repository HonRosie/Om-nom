from flask import render_template
from app import app
from flask import request, redirect

todoList = [
  {'task': 'Buy milk',
   'comment': 'From Trader Joes'
  },
  {'task': 'Bake cookies',
   'comment': 'Snickerdoodles'
  }
]


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

@app.route('/todo', methods=['GET','POST'])
def todos():

  if request.method == 'POST':
    todo = request.form['addTask']
    task = {'task': todo}
    todoList.append(task)


  return render_template('todo.html',
                         title="Todo",
                         todos=todoList)
