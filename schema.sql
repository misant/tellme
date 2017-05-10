CREATE DATABASE test;
USE test;
CREATE TABLE Results (
	timestamp date,
	script_path varchar(255),
	cpu_name varchar(255),
	total_mem int,
	multi_total float,
	multi_avg float,
	limit_execs int,
	limit_avg float
    );