# Database Final Project_server
This a the server end of the final database project

###### NOTE: This is not the formal API. You should not trust theses APIs yet.

# API Command

## Login page

### Sign up

##### Post("./signup")

```
{
	"Uname":""		//user name
	"Pnumber":""	//phone number
	"Mail":""		//maill address
	"PW":""			//password
}

return {
	"message":int	//([0:success,1:phone number error,2:mail error]
	"data":""		//UID
}
```

### Sign in

##### Post("./signin")

```
{
	"type":int 	//([0:UID,1:phone number,2:mail])
	"info":""	//UID,Phone number,mail
	"PW":""		//password
}

return {
	"message":int	//[0:success,1:fail]
	"data":{
		"Uname":""
		"Pnumber":""
		"Mail":""
		"UID": ""
	}
}
```



## Page 1

### Front Page

##### Get("./user/UID/overview")

```
return {
	"message":int				//success=0, fail=1
	"data":{
	    "Vname":""				//用户选择的单词计划
        "alreadyRecite":int		//总共背（浏览过）的单词数
        "remained":int			//剩余单词数
        "today learn":int		//今天要学的单词数
        "today review":int		//今天需要复习的单词数
        "continuous":int		//连续多少天背单词
	}
}
```

### Test Page

#####   Get("./plan/UID/\<int\>")

```
return{
	"message":int				//success=0, fail=1
	"data":{
		"todayLearn":[(
            "TID",
            "WID",
            "Proficiency",		//熟练度
            "options"			//[A,B,C,D]
            )]
        "todayReview"[(
            "TID",
            "WID",
            "Proficiency",		//熟练度
            "options"			//[A,B,C,D]
            )]
	}
}
```

##### GET("./word/WID")

```
return{
	"message":int		//success=0, fail=1
	"data":{
		"English":""
		"Chinese":""
		"Psymbol":""	//phonetic symbol
	}
}
```



#####   Post("./plan/UID")

```
{
	"result":[(
		"TID":"",
		"WID":"",
		"Proficiency":int,	//(0,1,2,3)
		"Reserved":""		//预留一个位置，后面还想加一点信息
		)]
	"start":"2019-12-01-10-30-12"
	"end":"2019-12-01-10-40-02"
}

return{
	"message":int	//success=0, fail=1
	"data":{}
} 
```

## Page 2

### Information

##### Get(./info/UID)

```
return{
	"message":int				//success=0, fail=1
	"data":{
		"info":[(
			1,	
            2,
            3,
            active time,		//int 
        )]
        "Ahour":[				//active hours
            active degree:int
        ]						//(24,1) I will build an example to clarify this --fy
	}
}
```
## Page 3

### record

##### Get("./plan/UID")

```
return{
	"message":int	//success=0, fail=1
	"data":[(
		"TID",
		"WID",
		"English",
		"Chinese",
		"Proficiency"
	)]
}
```

##### Post("./plan/UID")

```
{
	"result":[(
		"TID",
		"WID",
		"Proficiency"
	)]
}
```


​	


## Page4

### user Info Full

##### Get("./user/UID/info")

```
return{
	"message":int			//success=0, fail=1
	"data":{
		"Avatar":"base64"	//default='0'
        "Sex":""			//M/F/U
        "Education":""		
        "Grade":""
	}
}
```

##### Post("./user/UID/info")

```
{
	"Uname":""
	"Avatar":"base64"	//default='0'
	"Sex":""
	"Education":""
	"Grade":""
}
```



### Change Book List

##### Post("./user/UID/plan")

```
{
	"Vname"
	"VID"
} // 然后更新个人信息
```

### Feedback Page

##### Post("./feedback")


```
{
	"Info":""
	"UId":""
}
```

## 关于SQL封装类的一些说明：
=======
- 所有select函数的返回都是一个list，每个元素都是一个tuple表示数据，即[( ),( ),( )]。list的第0项为表头，然后是询问的数据。
- 所有的condition都用map{item:value}表示，也就是目前只支持等值查询。**value必须是一个list**，表示item的有限的离散值域
- 具体用例参见test_sillySQL.py
- 由于Date和USER是PSQL中的保留字，原来的user改成users，Date改成Dates



### 当前所有表的信息:
          Table "public.dictionary"
 Column  |         Type          | Modifiers 
---------+-----------------------+-----------
 wid     | character varying(32) | not null
 english | character varying(64) | not null
 psymbol | character varying(32) | 
 chinese | text[]                | 
Indexes:
    "dictionary_pkey" PRIMARY KEY, btree (wid)

         Table "public.feedback"
 Column |         Type          | Modifiers 
--------+-----------------------+-----------
 fid    | character varying(32) | not null
 uid    | character varying(32) | not null
 dates  | character varying(32) | not null
 info   | text                  | 
Indexes:
    "feedback_pkey" PRIMARY KEY, btree (fid)


               Table "public.plan"
   Column    |         Type          | Modifiers 
-------------+-----------------------+-----------
 uid         | character varying(32) | not null
 tid         | character varying(32) | not null
 wid         | character varying(32) | not null
 proficiency | integer               | 
Indexes:
    "plan_pkey" PRIMARY KEY, btree (uid, tid)

              Table "public.record"
   Column    |         Type          | Modifiers 
-------------+-----------------------+-----------
 sid         | character varying(32) | not null
 uid         | character varying(32) | not null
 dates       | character varying(32) | not null
 count       | integer               | not null
 score       | integer               | not null
 proficiency | integer[]             | 
 ahour       | integer               | 
 aday        | integer               | 
Indexes:
    "record_pkey" PRIMARY KEY, btree (sid)


            Table "public.takes"
 Column |         Type          | Modifiers 
--------+-----------------------+-----------
 tid    | character varying(32) | not null
 vid    | character varying(32) | not null
 wid    | character varying(32) | not null
Indexes:
    "takes_pkey" PRIMARY KEY, btree (tid)


              Table "public.users"
  Column   |          Type          | Modifiers 
-----------+------------------------+-----------
 uid       | character varying(32)  | not null
 uname     | character varying(64)  | not null
 pw        | character varying(64)  | not null
 avatar    | character varying(256) | 
 mail      | character varying(64)  | 
 pnumber   | character varying(32)  | 
 sex       | character(1)           | 
 education | character varying(32)  | 
 grade     | integer                | 
Indexes:
    "users_pkey" PRIMARY KEY, btree (uid)


          Table "public.vocabulary"
 Column |          Type          | Modifiers 
--------+------------------------+-----------
 vid    | character varying(32)  | not null
 vname  | character varying(128) | not null
 count  | integer                | not null
 day    | integer                | not null
 type   | character varying(64)  | 
Indexes:
    "vocabulary_pkey" PRIMARY KEY, btree (vid)

## 关于SQL封装的一点建议：
服务器在初始化时可以给SQL类传入一个logger对象，最好在最终发布版本中把print输出的语句改为logger输出
