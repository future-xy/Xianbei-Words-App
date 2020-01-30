# 先背单词

###### *This the server end of the 先背单词 App*

We updated the C-S API.

Some message formats also changed

| Old                        | New                   | Method |
| -------------------------- | --------------------- | ------ |
| Post("./signup")           | "./signup"            | post   |
| Post("./signin")           | "./signin"            | post   |
|                            | "./logout"            | get    |
| Get("./plan)               | "./vocabulary"        | get    |
| Get("./word/WID")          | "./word/WID"          | get    |
| Get("./user/UID/overview") | "./user/overview"     | get    |
| Get("./user/UID/info")     | "./user/info"         | get    |
| Post("./user/UID/info")    |                       | post   |
| Post("./record/UID")       | "./user/record"       | post   |
| Get(./record/UID)          |                       | get    |
| Get("./plan/UID")          | "./user/plan"         | get    |
| Post("./plan/UID")         |                       | post   |
| Post("./user/UID/plan")    |                       | put    |
| Get("./plan/UID/\<int\>")  | "./user/plan/\<int\>" | get    |
| Post("./feedback")         | "./user/feedback"     | post   |
|                            |                       |        |



## Client-Server API

#### "./signup"

##### Post

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



#### "./signin"

##### Post

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



#### "./logout"

##### Get

```
return {
	"message":int	//[0:success,1:fail]
	"data":""
}
```



#### "./vocabulary"

##### Get

```
{
	"message":int
	"data":[(
		"VID"
		"Vname"
		"Count"
		"Day"
		"Type"
	)]
}
```



#### "./word/WID"

##### GET

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



#### "./user/overview"

##### Get

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



#### "./user/info"

##### Get

```
return{
	"message":int			//success=0, fail=1
	"data":{
		"Uname":""
		"Avatar":"base64"	//default=''
        "Sex":""			//M/F/U
        "Education":""		
        "Grade":""
	}
}
```

##### Post

```
{
	"Uname":""
	"Avatar":"base64"	//default='0'
	"Sex":""
	"Education":""
	"Grade":""
}
```



#### "./user/record"

#####   Post

```
{
	"count_learned":int		//新背的单词数量
	"count_reviewed":int	//复习的单词数量
	//起止时间
	"start":"2019-12-01-10-30-12"
	"end":"2019-12-01-10-40-02"
}

return{
	"message":int	//success=0, fail=1
	"data":{}
} 
```

##### Get

```
return{
	"message":int				//success=0, fail=1
	"data":{
		"proficiencyInfo":[
			(int,int,int,int), 	//counts of p=0,1,2,3
			...					//past 7 days
			(int,int,int,int)
			],
		"Forgetting curve":[], 	//长度为7的实数数组，无物理意义 
		"active time":[minute],	//(int)，过去7天每天在线(背单词)时长
        	"Ahour":[],			//长度为24的整数数组，表示过去7天每个小时的平均活跃度,从0时刻开始					
	}
}
```



#### "./user/plan"

##### Get

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

##### Post

```
{
	"result":[(
		"TID",
		"WID",
		"Proficiency"
	)]
}
```

##### Put

```
{
	"Vname"		//or VID 建议VID
} // 然后更新个人信息
```



#### "./user/plan/\<int\>"

#####   Get

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



#### "./user/feedback"

##### Post


```
{
	"Info":""
}
```



## Mail API

{
	"recv_addr":""		//Receiver mail address
	"mail_content":""	//email
}

return {
	"message":int	//([0:success,1:error]
}
