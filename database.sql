--DatabaseName : database0
CREATE DATABASE database0;
CREATE TABLE USERS(
	UID VARCHAR(32) PRIMARY KEY NOT NULL,
	Uname VARCHAR(64) NOT NULL,
	PW VARCHAR(64) NOT NULL,
	Avatar VARCHAR(4194304) NOT NULL,
	Mail VARCHAR(64) NOT NULL,
	Pnumber VARCHAR(32) NOT NULL,
	Sex CHAR(1) NOT NULL,
	Education VARCHAR(32) NOT NULL,
	Grade int NOT NULL
);
-- USER IS NOT an available table name???

insert into users(UID,Uname,PW,Avatar,Mail,Pnumber,Sex,Education,Grade) VALUES
('0001'	,	'LM'	,	'123456'	,	'','LM@123.com','13900008888',	'M','Undergraduate',3),
('0002'	,	'WM'	,	'123456'	,	'','WM@123.com','18900006666',	'F','Senior',	2),
('0003'	,	'LW'	,	'123456'	,	'','LW@123.com','13800007777',	'U','Undergraduate',1);
-- TRUE IS MALE, FALSE IS FEMALE
CREATE TABLE DICTIONARY(
	WID VARCHAR(32) PRIMARY KEY NOT NULL,
	English VARCHAR(64) NOT NULL,
	Psymbol VARCHAR(32),
	Chinese TEXT[]
);

insert into DICTIONARY(WID,English,Psymbol,Chinese) VALUES
('0001','hello','[heˈləʊ]','{"int. 喂；哈罗","n. 表示问候， 惊奇或唤起注意时的用语"}'),
('0002','world','[wɜrld]','{"n. 世界；领域；世俗；全人类；物质生活"}'),
('0003','python','[''paɪθɑn]','{"n. 巨蟒"}'),
('0004','hasty','[''heɪsti]','{"adj. 轻率的；匆忙的","n. (Hasty)人名；(英)黑斯蒂"}'),
('0005','vanish','[ˈvæniʃ]','{"vi. 消失；突然不见；成为零","vt. 使不见，使消失","n. 弱化音"}');

CREATE TABLE VOCABULARY(
	VID VARCHAR(32) PRIMARY KEY NOT NULL,
	Vname VARCHAR(128) NOT NULL,
	Count INT NOT NULL,
	Day INT NOT NULL,
	Type VARCHAR(64)
);

insert into VOCABULARY VALUES
('0001','17天搞定GRE单词',	3500,	17,	'GRE'),
('0002','45天托福红宝书记忆计划',	5000,	45,	'托福'),
('0003','高考单词闪过',	3500,	100,	'高考');

CREATE TABLE TAKES(
	TID VARCHAR(32) PRIMARY KEY NOT NULL,
	VID VARCHAR(32) NOT NULL,
	WID VARCHAR(32) NOT NULL
);
insert into TAKES VALUES
('0001',	'0001',	'0003'),
('0002',	'0001',	'0004'),
('0003',	'0002',	'0005'),
('0004',	'0003',	'0001'),
('0005',	'0003',	'0002');

CREATE TABLE PLAN(
	UID VARCHAR(32)	,
	TID VARCHAR(32)	,
	WID VARCHAR(32)	NOT NULL,
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
	SID VARCHAR(32) PRIMARY KEY NOT NULL,
	UID VARCHAR(32) NOT NULL,
	Dates VARCHAR(32) NOT NULL,
	Learned int not null,
	review int not null,
	Count INT NOT NULL,
	Score int NOT NULL,
	Proficiency int[4],
	Ahour numeric(10,3)[24],
	Aday int
);
insert INTO RECORD VALUES
('0001',	'0001',	'2019-12-01',	0	,0	,'{10,0,0,0}',	'{1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}',1),
('0002',	'0002',	'2019-12-01',	100	,67	,'{10,0,0,0}',	'{0,1.5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}',1),
('0003',	'0003',	'2019-12-01',	30	,70	,'{10,0,0,0}',	'{0,0,2.1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}',1),
('0004',	'0001',	'2019-12-02',	1	,0	,'{10,0,0,0}',	'{0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}',2),
('0005',	'0002',	'2019-12-02',	100	,75	,'{10,0,0,0}',	'{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}',2),
('0006',	'0003',	'2019-12-02',	20	,74	,'{10,0,0,0}',	'{0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}',2);

CREATE TABLE FEEDBACK(
	FID VARCHAR(32) PRIMARY KEY NOT null,
	UID VARCHAR(32) not null,
	Dates VARCHAR(32) NOT NULL,
	INFO TEXT
);

insert into FEEDBACK VALUES
('0001',	'0001',	'2019-12-10',	'OMG! I''v never seen such perfect APP!'),
('0002',	'0002',	'2019-12-13',	'Why didn''t I find such great software earlier!!!');






-------------------------------------------
select * from pg_stat_activity where state='active';
select pg_cancel_backend(27517);
alter table tb101 alter id type varchar;

SELECT 
    pg_terminate_backend(pid) 
FROM 
    pg_stat_activity 
WHERE 
    -- don't kill my own connection!
    pid <> pg_backend_pid()
    -- don't kill the connections to other databases
    AND datname = 'database_name'


CREATE TABLE RECORD as(
	select SID, UID, Dates,Learned,review, count,score, Proficiency,ahour, Aday
	from record_old
);