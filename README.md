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
	"errorcode":int	//([0:success,1:phone number error,2:mail error]
	"UID": ""
}
```

### Sign in

##### Post("./signin")

```
{
	"type":int //([0:UID,1:phone number,2:mail])
	"info":""
	"PW":""
}

return {
	"errorcode":int //[0:success,1:fail]
	"Uname":""
	"Pnumber":""
	"Mail":""
	"UID": ""
}
```



## Page 1

### Front Page

##### Get("./user/UID/overview")

```
return {
    "Vname":""				//用户选择的单词计划
    "alreadyRecite":int		//总共背（浏览过）的单词数
    "remained":int			//剩余单词数
    "today learn":int		//今天要学的单词数
    "today review":int		//今天需要复习的单词数
    "continuous":int		//连续多少天背单词
}
```

### Test Page

#####   Get("./plan/UID/\<int\>")

```
return{
	"todayLearn":[
		("TID",
		"WID",
		"Proficiency",		//熟练度
		"options"			//[A,B,C,D]
		)
	]
	"todayReview"[
		("TID",
		"WID",
		"Proficiency",		//熟练度
		"options"			//[A,B,C,D]
		)
	]
}
```

##### GET("./word/WID")

```
return{
	"English":""
	"Chinese":""
	"Psymbol":""	//phonetic symbol
}
```



#####   Post("./plan/UID")

```
{
	"result":[
		("TID":"",
		"WID":"",
		"Proficiency":int,	//(0,1,2,3)
		//"":"")
	]
	"start":"2019-12-01-10-30-12"
	"end":"2019-12-01-10-40-02"
}

return bool
```

## Page 2

### Information

##### Get(./info/UID)

```
return{
	"info":[
		(1,	
		2,
		3,
		active time,		//int 
		)
	]
	"Ahour":[				//active hours
		active degree:int
	]						//(24,1)
}
```
## Page 3

### record

##### Get("./plan/UID")

```
return{
	"plan":[
		("TID",
		"WID",
		"English",
		"Chinese",
		"Proficiency"
		)
	]
}
```

##### Post("./plan/UID")

```
{
	"newplan":[
		("TID",
		"WID",
		"Proficiency"
		)
	]
}
```


​	


## Page4

### user Info Full

##### Get("./user/UID/info")

```
return{
	"Avatar":"base64"	//default='0'
	"Sex":""			//M/F/U
	"Education":""		
	"Grade":""
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
