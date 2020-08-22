CREATE TABLE IF NOT EXISTS NY(
	Year INT NOT NULL,
	Month VARCHAR(30),
	State VARCHAR(30),
	County VARCHAR(50) primary key,
	Unemployment_Rate double precision);

CREATE TABLE IF NOT EXISTS FL(
	Year INT NOT NULL,
	Month VARCHAR(30),
	State VARCHAR(30),
	County VARCHAR(50),
	Unemployment_Rate double precision,
	foreign key (County) references ny (County));
	
CREATE TABLE IF NOT EXISTS CA(
	Year INT NOT NULL,
	Month VARCHAR(30),
	State VARCHAR(30),
	County VARCHAR(50),
	Unemployment_Rate double precision,
	foreign key (County)  references ny (County));