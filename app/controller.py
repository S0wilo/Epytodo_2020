from flask import render_template, redirect, url_for, jsonify
from app import models

def funct_register(username, password, password2):
    if password != password2:
        return render_template("register.html")
    if len(username) <= 0 or len(password) <= 0:
        return render_template("register.html")
    try:
        users = models.get_users()
        for i in users:
            if i[1] == username:
                return render_template("register.html")
        models.add_user(username, password)
        return redirect(url_for('route_user', username=username))
    except:
        return render_template("register.html")

def funct_signin(username, password):
    if len(username) <= 0 or len(password) <= 0:
        return render_template("signin.html")
    try:
        users = models.get_users()
        for i in users:
            if i[1] == username and i[2] == password:
                return redirect(url_for('route_user', username=username))
        return render_template("signin.html")
    except:
        return render_template("signin.html")

def funct_task_list():
    try:
        tasks=models.get_tasks()
        return tasks
    except:
        return 0

def funct_add_task(username, title, begin, end, status):
    try:
        models.add_task(title, begin, end, status)
        tasks = models.get_tasks()
        users = models.get_users()
        for i in users:
            if i[1] == username and len(tasks) != 0:
                models.add_user_has_task(i[0], tasks[len(tasks) - 1][0])
                return redirect(url_for('route_task', username=username))
        return render_template("add_task.html")
    except:
        return render_template("add_task.html")

def funct_del_task(username, id_task):
    try:
        if id_task == "":
            return render_template("delete_task.html")
        models.del_task(id_task)
        models.del_user_has_task(id_task)
        return redirect(url_for('route_task', username=username))
    except:
        return render_template("delete_task.html")

def funct_mod_task(username, id_task, title, begin, end, status):
    try:
        if title != "":
            models.mod_title(id_task, title)
        if begin != "":
            models.mod_begin(id_task, begin)
        if end != "":
            models.mod_end(id_task, end)
        if status != "":
            models.mod_status(id_task, status)
        return redirect(url_for('route_task', username=username))
    except:
        return render_template("update_task.html")
