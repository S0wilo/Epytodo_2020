import pymysql as sql
from flask import render_template, request
from app import app, controller

@app.route('/', methods=['GET'])
def route_index():
    return render_template("homepage.html")

@app.route('/register', methods=['GET'])
def route_register():
    return render_template("register.html")

@app.route('/register', methods=['GET', 'POST'])
def route_register_post():
    username = request.form['username']
    password = request.form['password']
    password2 = request.form['password2']
    return controller.funct_register(username, password, password2)

@app.route('/signin', methods=['GET'])
def route_signin():
    return render_template("signin.html")

@app.route('/signin', methods=['GET', 'POST'])
def route_signin_post():
    username = request.form['username']
    password = request.form['password']
    return controller.funct_signin(username, password)

@app.route('/user', methods=['GET'])
def route_user():
    return render_template("user.html", username=request.args['username'])

@app.route('/user/task', methods=['GET'])
def route_task():
    username=request.args['username']
    tasks=controller.funct_task_list()
    return render_template("task.html", tasks=tasks, username=username)

@app.route('/user/task/add', methods=['GET'])
def route_add_task():
    return render_template("add_task.html")

@app.route('/user/task/add', methods=['GET', 'POST'])
def route_add_task_post():
    username=request.args['username']
    title=request.form['title']
    begin=request.form['begin']
    end=request.form['end']
    status=request.form['status']
    return controller.funct_add_task(username, title, begin, end, status)

@app.route('/user/task/del/id', methods=['GET'])
def route_del_task():
    tasks=controller.funct_task_list()
    return render_template("delete_task.html", tasks=tasks)

@app.route('/user/task/del/id', methods=['GET', 'POST'])
def route_del_task_post():
    username=request.args['username']
    id_task=request.form['id_task']
    return controller.funct_del_task(username, id_task)

@app.route('/user/task/id', methods=['GET'])
def route_mod_task():
    return render_template("update_task.html")

@app.route('/user/task/id', methods=['GET', 'POST'])
def route_mod_task_post():
    username=request.args['username']
    id_task=request.form['id_task']
    title=request.form['title']
    begin=request.form['begin']
    end=request.form['end']
    status=request.form['status']
    return controller.funct_mod_task(username, id_task, title, begin, end, status)
    
