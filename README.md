# 先背单词

###### *This a the server end of the 先背单词 App*

## Client-Server API

### Login page

#### Sign up

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

#### Sign in

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



### Page 1

#### Front Page

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

#### Test Page

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



#####   Post("./record/UID")

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

### Page 2

#### Information(visualization)

##### Get(./record/UID)

```
return{
	"message":int				//success=0, fail=1
	"data":{
		"proficiencyInfo":[
			(int,int,int,int), 	//counts of p=0,1,2,3
			...					//past 7 days
			(int,int,int,int)
			],
		"Forgetting curve":[], 					//长度为7的实数数组，无物理意义 
		"active time":[minute],		//(int)，过去7天每天在线(背单词)时长
        	"Ahour":[],			//长度为24的整数数组，表示过去7天每个小时的平均活跃度,从0时刻开始					
	}
}
```
### Page 3

#### record

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


### Page4

#### user Info Full

##### Get("./user/UID/info")

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



#### Change Book List

##### Get("./plan)

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



##### Post("./user/UID/plan")

```
{
	"Vname"		//or VID 建议VID
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



## Mail API

...