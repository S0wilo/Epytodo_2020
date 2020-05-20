Create DATABASE epytodo;
USE epytodo;

Create TABLE user
(
    user_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username CHAR(40) NOT NULL,
    password CHAR(20) NOT NULL
) ENGINE = Innodb;

Create TABLE task
(
    task_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    title CHAR(40) NOT NULL,
    begin DATETIME DEFAULT CURRENT_TIMESTAMP,
    end DATETIME NULL,
    status int NOT NULL DEFAULT 0
) ENGINE = Innodb;

Create TABLE user_has_task
(
    fk_user_id INT,
    fk_task_id INT
) ENGINE = Innodb;
