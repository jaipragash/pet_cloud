create database createuser;
use createuser;

create table cuser(
ID int NOT NULL auto_increment primary key,
NAME varchar (50) NOT NULL,
Email varchar (200) not null,
PASSWORD varchar(200) NOT NULL
);
show databases;
SELECT * FROM cuser;
describe cuser;
DROP DATABASE createuser;

