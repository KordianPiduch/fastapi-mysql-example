DROP DATABASE IF EXISTS `main`;
CREATE DATABASE main;

USE main;

CREATE TABLE test_table( 
    id int not null auto_increment, 
    column1 varchar(255) not null, 
    column2 int not null default 0, 
    primary key (id) 
    );

INSERT INTO test_table (column1, column2) VALUES ("test", 69)
