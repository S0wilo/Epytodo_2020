import pymysql as sql
from app import app

def get_users():
    connect = sql.connect(host=app.config["DATABASE_HOST"],
                          unix_socket=app.config["DATABASE_SOCK"],
                          user=app.config["DATABASE_USER"],
                          passwd=app.config["DATABASE_PASS"],
                          db=app.config["DATABASE_NAME"])
    cursor = connect.cursor()
    cursor.execute("SELECT * from user")
    result = cursor.fetchall()
    cursor.close()
    connect.close()
    return result

def add_user(username, password):
    connect = sql.connect(host=app.config["DATABASE_HOST"],
                          unix_socket=app.config["DATABASE_SOCK"],
                          user=app.config["DATABASE_USER"],
                          passwd=app.config["DATABASE_PASS"],
                          db=app.config["DATABASE_NAME"])
    cursor = connect.cursor()
    cmd = "INSERT INTO user (username, password) VALUES ('" + username + "', '" + password + "');"
    cursor.execute(cmd)
    connect.commit()
    cursor.close()
    connect.close()

def get_tasks():
    connect = sql.connect(host=app.config["DATABASE_HOST"],
                          unix_socket=app.config["DATABASE_SOCK"],
                          user=app.config["DATABASE_USER"],
                          passwd=app.config["DATABASE_PASS"],
                          db=app.config["DATABASE_NAME"])
    cursor = connect.cursor()
    cursor.execute("SELECT * from task")
    result = cursor.fetchall()
    cursor.close()
    connect.close()
    return result

def add_task(title, begin, end, status):
    connect = sql.connect(host=app.config["DATABASE_HOST"],
                          unix_socket=app.config["DATABASE_SOCK"],
                          user=app.config["DATABASE_USER"],
                          passwd=app.config["DATABASE_PASS"],
                          db=app.config["DATABASE_NAME"])
    cursor = connect.cursor()
    if begin != "":
        cmd = "INSERT INTO task (title, begin, end, status) VALUES ('" + title + "', '" + begin + "', '" + end + "', '" + status + "');"
    else:
        cmd = "INSERT INTO task (title, end, status) VALUES ('" + title  + "', '" + end + "', '" + status + "');" 
    cursor.execute(cmd)
    connect.commit()
    cursor.close()
    connect.close()

def del_task(id_task):
    connect = sql.connect(host=app.config["DATABASE_HOST"],
                          unix_socket=app.config["DATABASE_SOCK"],
                          user=app.config["DATABASE_USER"],
                          passwd=app.config["DATABASE_PASS"],
                          db=app.config["DATABASE_NAME"])
    cursor = connect.cursor()
    cmd = "DELETE FROM task WHERE task_id = " + id_task + ";"
    cursor.execute(cmd)
    connect.commit()
    cursor.close()
    connect.close()

def del_user_has_task(id_task):
    connect = sql.connect(host=app.config["DATABASE_HOST"],
                          unix_socket=app.config["DATABASE_SOCK"],
                          user=app.config["DATABASE_USER"],
                          passwd=app.config["DATABASE_PASS"],
                          db=app.config["DATABASE_NAME"])
    cursor = connect.cursor()
    cmd = "DELETE FROM user_has_task WHERE fk_task_id = " + id_task + ";"
    cursor.execute(cmd)
    connect.commit()
    cursor.close()
    connect.close()

def add_user_has_task(id_user, id_task):
    connect = sql.connect(host=app.config["DATABASE_HOST"],
                          unix_socket=app.config["DATABASE_SOCK"],
                          user=app.config["DATABASE_USER"],
                          passwd=app.config["DATABASE_PASS"],
                          db=app.config["DATABASE_NAME"])
    cursor = connect.cursor()
    cmd = "INSERT INTO user_has_task (fk_user_id, fk_task_id) VALUES ('" + str(id_user) + "', '" + str(id_task) + "');"
    cursor.execute(cmd)
    connect.commit()
    cursor.close()
    connect.close()

def get_user_has_task():
    connect = sql.connect(host=app.config["DATABASE_HOST"],
                          unix_socket=app.config["DATABASE_SOCK"],
                          user=app.config["DATABASE_USER"],
                          passwd=app.config["DATABASE_PASS"],
                          db=app.config["DATABASE_NAME"])
    cursor = connect.cursor()
    cursor.execute("SELECT * from user_has_task")
    result = cursor.fetchall()
    cursor.close()
    connect.close()
    return result

def mod_title(id_task, title):
    connect = sql.connect(host=app.config["DATABASE_HOST"],
                          unix_socket=app.config["DATABASE_SOCK"],
                          user=app.config["DATABASE_USER"],
                          passwd=app.config["DATABASE_PASS"],
                          db=app.config["DATABASE_NAME"])
    cursor = connect.cursor()
    cmd = "UPDATE task SET title = '" + title + "' WHERE task_id = " + id_task + ";"
    cursor.execute(cmd)
    connect.commit()
    cursor.close()
    connect.close()

def mod_begin(id_task, begin):
    connect = sql.connect(host=app.config["DATABASE_HOST"],
                          unix_socket=app.config["DATABASE_SOCK"],
                          user=app.config["DATABASE_USER"],
                          passwd=app.config["DATABASE_PASS"],
                          db=app.config["DATABASE_NAME"])
    cursor = connect.cursor()
    cmd = "UPDATE task SET begin = '" + begin + "' WHERE task_id = " + id_task + ";"
    cursor.execute(cmd)
    connect.commit()
    cursor.close()
    connect.close()

def mod_end(id_task, end):
    connect = sql.connect(host=app.config["DATABASE_HOST"],
                          unix_socket=app.config["DATABASE_SOCK"],
                          user=app.config["DATABASE_USER"],
                          passwd=app.config["DATABASE_PASS"],
                          db=app.config["DATABASE_NAME"])
    cursor = connect.cursor()
    cmd = "UPDATE task SET end = '" + end + "' WHERE task_id = " + id_task + ";"
    cursor.execute(cmd)
    connect.commit()
    cursor.close()
    connect.close()

def mod_status(id_task, status):
    connect = sql.connect(host=app.config["DATABASE_HOST"],
                          unix_socket=app.config["DATABASE_SOCK"],
                          user=app.config["DATABASE_USER"],
                          passwd=app.config["DATABASE_PASS"],
                          db=app.config["DATABASE_NAME"])
    cursor = connect.cursor()
    cmd = "UPDATE task SET status = '" + status + "' WHERE task_id = " + id_task + ";"
    cursor.execute(cmd)
    connect.commit()
    cursor.close()
    connect.close()
