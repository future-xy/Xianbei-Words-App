--DatabaseName : database0
CREATE DATABASE database0;
CREATE TABLE USERS(
	UID CHAR(32) PRIMARY KEY NOT NULL,
	Uname CHAR(64) NOT NULL,
	PW CHAR(64) NOT NULL,
	Avatar VARCHAR(256),
	Mail CHAR(64),
	Pnumber CHAR(32),
	Sex BOOLEAN,
	Education CHAR(32),
	Grade int
);
-- USER IS NOT an available table name???

insert into users(UID,Uname,PW,Avatar,Mail,Pnumber,Sex,Education,Grade) VALUES
('0001'	,	'LM'	,	'123456'	,	Null,'LM@123.com','13900008888',	TRUE,'Undergraduate',3),
('0002'	,	'WM'	,	'123456'	,	Null,'WM@123.com','18900006666',	FALSE,'Senior',	2),
('0003'	,	'LW'	,	'123456'	,	Null,'LW@123.com','13800007777',	NULL,'Undergraduate',1);
-- TRUE IS MALE, FALSE IS FEMALE
CREATE TABLE DICTIONARY(
	WID CHAR(32) PRIMARY KEY NOT NULL,
	English CHAR(64) NOT NULL,
	Psymbol CHAR(32),
	Chinese TEXT[]
);

insert into DICTIONARY(WID,English,Psymbol,Chinese) VALUES
('0001','hello','[heˈləʊ]','{"int. 喂；哈罗","n. 表示问候， 惊奇或唤起注意时的用语"}'),
('0002','world','[wɜrld]','{"n. 世界；领域；世俗；全人类；物质生活"}'),
('0003','python','[''paɪθɑn]','{"n. 巨蟒"}'),
('0004','hasty','[''heɪsti]','{"adj. 轻率的；匆忙的","n. (Hasty)人名；(英)黑斯蒂"}'),
('0005','vanish','[ˈvæniʃ]','{"vi. 消失；突然不见；成为零","vt. 使不见，使消失","n. 弱化音"}');

CREATE TABLE VOCABULARY(
	VID CHAR(32) PRIMARY KEY NOT NULL,
	Vname CHAR(128) NOT NULL,
	Count INT NOT NULL,
	Day INT NOT NULL,
	Type CHAR(64)
);

insert into VOCABULARY VALUES
('0001','17天搞定GRE单词',	3500,	17,	'GRE'),
('0002','45天托福红宝书记忆计划',	5000,	45,	'托福'),
('0003','高考单词闪过',	3500,	100,	'高考');

CREATE TABLE TAKES(
	TID CHAR(32) PRIMARY KEY NOT NULL,
	VID CHAR(32) NOT NULL,
	WID CHAR(32) NOT NULL
);
insert into TAKES VALUES
('0001',	'0001',	'0003'),
('0002',	'0001',	'0004'),
('0003',	'0002',	'0005'),
('0004',	'0003',	'0001'),
('0005',	'0003',	'0002');

CREATE TABLE PLAN(
	UID CHAR(32)	,
	TID CHAR(32)	,
	WID CHAR(32)	NOT NULL,
	Proficiency int,
	PRIMARY KEY(UID, TID)
);
insert into PLAN VALUES
('0001',	'0001',	'0003',	100),
('0001',	'0002',	'0004',	0),
('0002',	'0004',	'0001',	99),
('0002',	'0005',	'0002',	99),
('0003',	'0003',	'0005',	23);

CREATE TABLE RECORD(
	SID CHAR(32) PRIMARY KEY NOT NULL,
	UID CHAR(32) NOT NULL,
	Dates char(32) NOT NULL,
	Count INT NOT NULL,
	Score int NOT NULL,
	Proficiency int[24],
	Ahour int
);
insert INTO RECORD VALUES
('0001',	'0001',	'2019-12-01',	0	,0	,'{10,0,0,0}',	0),
('0002',	'0002',	'2019-12-01',	100	,67	,'{10,0,0,0}',	12),
('0003',	'0003',	'2019-12-01',	30	,70	,'{10,0,0,0}',	23),
('0004',	'0001',	'2019-12-02',	1	,0	,'{10,0,0,0}',	23),
('0005',	'0002',	'2019-12-02',	100	,75	,'{10,0,0,0}',	12),
('0006',	'0003',	'2019-12-02',	20	,74	,'{10,0,0,0}',	22);

CREATE TABLE FEEDBACK(
	FID CHAR(32) PRIMARY KEY NOT null,
	UID CHAR(32) not null,
	Dates CHAR(32) NOT NULL,
	INFO TEXT
);

insert into FEEDBACK VALUES
('0001',	'0001',	'2019-12-10',	'OMG! I''v never seen such perfect APP!'),
('0002',	'0002',	'2019-12-13',	'Why didn''t I find such great software earlier!!!');
