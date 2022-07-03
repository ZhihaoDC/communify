CREATE DATABASE IF NOT EXISTS Networkly;
GRANT ALL ON Networkly.* TO 'user'@'%';

USE Networkly;

DROP TABLE IF EXISTS USERS;

CREATE TABLE USERS(
    id BIGINT(20) AUTO_INCREMENT,
    username VARCHAR(25) NOT NULL,
    email VARCHAR(50) NOT NULL,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(100),
    profile_description VARCHAR(250) ,
    PRIMARY KEY (id)
);

INSERT INTO USERS(username, email, firstname, lastname, profile_description)
VALUES  ("david19", "david19@gmail.com", "david", "fernandez", "data scientist"),
        ("isabel20", "isabel20@gmail.com", "isabel", "gomez", "product manager"),
        ("sandra21", "sandra21@gmail.com", "sandra", "hernandez", "biologist");
        
DROP TABLE IF EXISTS USER_EXPERIMENTS;

CREATE TABLE USER_EXPERIMENTS(
    user_id BIGINT(20) NOT NULL,
    experiment_id CHAR(32) NOT NULL,
    experiment_name VARCHAR(25), 
    creation_date DATE NOT NULL,
    category VARCHAR(50),
    description VARCHAR(300),
    network_json JSON NOT NULL,
    metrics JSON,
    PRIMARY KEY (experiment_id),
    FOREIGN KEY (user_id) REFERENCES USERS(id)
);

