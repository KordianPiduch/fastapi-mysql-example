CREATE DATABASE main;

USE main;

CREATE TABLE items( 
    id int not null auto_increment, 
    name varchar(255) not null, 
    amount int not null default 0, 
    primary key (id) 
    );

INSERT INTO items (name, amount) VALUES ("test", 69)